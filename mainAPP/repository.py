from django.http import HttpResponseBadRequest
from mainAPP.models import Contest, Match,Player, PlayersMatchData,Team, User_Feature_Suggestion, UserTeam
from django.utils import timezone

from mainAPP.team_creation_rules import filter_team_data, finalize_team, follow_base_rules
from .serializers import ContestSerializer, FantasyScoreSerializer, FeatureRequestSerializer, MatchListSerializer,GameSquadSerializer, UserSerializer
from rest_framework.response import Response
from usermanagerAPP.models import User1
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password

class vision11:
    def get_match_list(self):
        matches = Match.objects.filter(time__gt=timezone.now())
        match = MatchListSerializer(matches,many=True)
        return Response({'status':200,'message':'success','data':match.data})

        

    def get_todays_squad(self,team1,team2):
        match = Match.objects.filter(team1=team1,team2=team2)[0]
        if (match.time-timezone.now()).days < 0:
            return Response({'status':404,'message':'Match has started.'})
        if (match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60:
            return Response({'status':404,'message':'Deadline has passed.'})
        t1 = Team.objects.get(team_name=team1)
        t2 = Team.objects.get(team_name=team2)
        p1 = Player.objects.filter(player_team=t1)
        p2 = Player.objects.filter(player_team=t2)
        gamesquad1 = GameSquadSerializer(p1,many=True)
        gamesquad2 = GameSquadSerializer(p2,many=True)
        return Response({'status':200,'message':'success','team1':gamesquad1.data,'team2':gamesquad2.data})


    def render_team_selection(self,request,mid):
        match = Match.objects.get(id=mid)
        if ((match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60) or (match.time - timezone.now()).days <= -1:
            return HttpResponseBadRequest('Deadline for the match has passed.')
        return render(request, 'selecting_team.html',{'team1':match.team1,'team2':match.team2})



    def get_fantasy_score(self,url):
        match = Match.objects.get(url=url)
        players = PlayersMatchData.objects.filter(match_url=match)
        serialized_players = FantasyScoreSerializer(players,many=True)
        return Response({'status':200,'message':'success','match':url,'data':serialized_players.data})


    def get_completed_matches(self):
        match = Match.objects.filter(is_match_end=True)
        serialized_matches = MatchListSerializer(match,many=True)
        return Response({'status':200,'message':'success','data':serialized_matches.data})


    def get_Live_matches(self):
        match = Match.objects.filter(is_match_end=False,time__lt=timezone.now())
        serialized_matches = MatchListSerializer(match,many=True)
        return Response({'status':200,'message':'success','data':serialized_matches.data})

    
    def get_upcoming_matches(self):
        match = Match.objects.filter(is_match_end=False,time__gt=timezone.now())
        data = []
        for i in match:
            match_data_individual = {}
            time_obj = (i.time)-timezone.now()
            match_time = (time_obj.days)*24*60*60+time_obj.seconds
            match_data_individual['id'] = i.id
            match_data_individual['url'] = i.url
            match_data_individual['title'] = i.title
            match_data_individual['time'] = match_time
            match_data_individual['name'] = i.name
            match_data_individual['team1'] = i.team1
            match_data_individual['team2'] = i.team2
            match_data_individual['is_match_end'] = i.is_match_end
            match_data_individual['team1_img'] = i.team1_img
            match_data_individual['team2_img'] = i.team2_img
            data.append(match_data_individual)
        return Response({'status':200,'message':'success','data':data})


    def get_age_verification_requests(self):
        users = User1.objects.filter(adult=False)
        user_obj = [user for user in users if user.aadhar_image!='']
        seralizer = UserSerializer(user_obj,many=True)
        return Response({'status':200,'data':seralizer.data,'message':'success'})


    def get_features_requests(self):
        features = User_Feature_Suggestion.objects.filter(is_seen=False)
        serializer = FeatureRequestSerializer(features,many=True)
        return Response({'status':200,'data':serializer.data,'message':'success'})


    def set_seen_fr(self,fid):
        obj = User_Feature_Suggestion.objects.get(id=fid)
        obj.is_seen = True
        obj.save()
        return redirect('/staff#absdash')

    # non api methods
    def create_user_team(self,data,user):
        players,captain,vicecaptain = filter_team_data(data)
        status,message = finalize_team(players,captain,vicecaptain,data["match_id"],user)
        if status:
            return Response({'status':200,'message':'success'})
        return Response({'status':200,'message':message})


    def is_strong(self,password):
        if len(set(password)) < 6 or password.isalnum() or password.isspace():
            return False
        return True


    def create_contest(self,data,user):
        if user.vision_credits < float(data["entry_fee"]):
            return Response({'status':200,'message':'Insufficient balance for creating contest.'})
        
        model = Contest()
        match = Match.objects.get(id=int(data['match_id']))
        if ((match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60) or (match.time - timezone.now()).days <= -1:
            return Response({'status':200,'message':'Deadline of Contest creation has passed'})
        userteam = UserTeam.objects.get(id=data["team"],user=user,match_id=match)
        model.match_id = match
        model.length = int(data["length"])
        model.fee_type = user.currency_type
        if data["type"].lower() == "private":
            if self.is_strong(data["password"]):
                model.password = make_password(data["password"])
                model.contest_type = 'private'
            else:
                return Response({'status':200,'message':'please use a strong password.'})
        model.entry_fee = max(1,float(data["entry_fee"]))
        user.vision_credits -= float(data["entry_fee"])
        user.save()
        model.save()
        model.teams.add(userteam)
        model.user.add(user)
        model.save()
        return Response({'status':200,'message':'success','contest_id':model.id})


    def search_contest(self,data):
        '''
            return a Response with object of the contest.
        '''
        model = Contest.objects.get(match_id=int(data["match_id"]),id=int(data["contest_id"]))
        flag = 0
        if model.contest_type == "private":
            if check_password(data["password"],model.password):
                flag = 1
        else:
            flag = 1
        if flag:
            if model.length > len(model.user.all()):
                serializer = ContestSerializer(model)
                return Response({'status':200,'data':serializer.data,'message':'success'})
            else:
                return Response({'status':200,'message':'contest already filled.'})
        else:
            return Response({'status':200,'message':'either contest id or password is invalid.'})


    
    def join_contest(self,data,user):
        team_id = data["team_id"]
        userteam = UserTeam.objects.get(id=int(team_id))
        contest_id = data["contest_id"]
        contest = Contest.objects.get(id=int(contest_id))
        all_users = contest.user.all()
        if contest.length > len(all_users):
            if user in all_users:
                return Response({'status':200,'message':'You have already joined the contest.'})
            else:
                match = contest.match_id
                if not ((match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60) and match == userteam.match_id and not ((match.time - timezone.now()).days <= -1):
                    if user.vision_credits >= contest.entry_fee and user.currency_type == contest.fee_type:
                        if contest.contest_type.lower() == "public":
                            user.vision_credits -= contest.entry_fee
                            user.save()
                            contest.user.add(user)
                            contest.teams.add(userteam)
                            contest.save()
                            return Response({'status':200,'message':'success','id':contest.id})
                        else:
                            password = data["password"]
                            if check_password(password,contest.password):
                                user.vision_credits -= contest.entry_fee
                                user.save()
                                contest.user.add(user)
                                contest.teams.add(userteam)
                                contest.save()
                                return Response({'status':200,'message':'success'})
                            else:
                                return Response({'status':200,'message':'Invalid password for provided contest.'})
                    else:
                        return Response({'status':200,'message':'Invalid currency type or Insufficient balance.'})
                else:
                    return Response({'status':200,'message':'Deadline for join this contest is passed, or you are using invalid data.'})
        else:
            return Response({'status':200,'message':'contest already filled up.'})


    def save_suggestion_form(self,request):
        model = User_Feature_Suggestion.objects.create(
            user = request.user,
            user_first_name = request.POST['first_name'],
            user_last_name = request.POST['last_name'],
            user_email = request.POST['email'],
            feature_title = request.POST['title'],
            feature_des = request.POST['description']
        )
        
        messages.success(request, 'Your Suggestions have been send successfullly.')
        return redirect('/dashboard')


class vision11_render:

    def render_userteam(self,request,mid,tid):
        match = Match.objects.get(id=int(mid))
        userteam = UserTeam.objects.get(match_id=match,id=int(tid))
        
        if userteam.user == request.user or ((match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60) or (match.time - timezone.now()).days <= -1:
            players = [userteam.player1,userteam.player2,userteam.player3,userteam.player4,userteam.player5,userteam.player6,userteam.player7,userteam.player8,userteam.player9,userteam.player10,userteam.player11]
            return render(request,'userteam.html',{'data':players,'captain':userteam.captain,'vice_captain':userteam.vice_captain})
        return HttpResponseBadRequest('You can view other teams only if deadline has passed.')


    def render_contestdetails(self,request,cid):
        return render(request,'contestdetails.html')
    

    def render_usercontest(self,request):
        return render(request,'usercontest.html')
    
    def render_age_adminportal(self,request):
        users = User1.objects.filter(adult=False)
        user_obj = [user for user in users if user.aadhar_image!='']
        len_obj = len(user_obj)
        return render(request,'admin_age_verification.html',{'data':user_obj,'len': len_obj})


    def render_contest(self,request,mid):
        match = Match.objects.get(id=mid)
        if ((match.time - timezone.now()).days == 0 and (match.time - timezone.now()).seconds < 15*60) or (match.time - timezone.now()).days <= -1:
            return HttpResponseBadRequest('Deadline has passed')
        userteams = UserTeam.objects.filter(match_id=match,user=request.user)
        if userteams:
            contests = Contest.objects.filter(match_id=match,contest_type="public")
            render_contest = []
            available_slots = []
            percentage_full =[]
            for contest in contests:
                length = len(contest.user.all())
                if contest.length > length:
                    render_contest.append(contest)
                    available_slots.append(contest.length-length)
                    num = round((length/contest.length)*100,2)
                    percentage_full.append(num)
            return render(request,'contest.html',{'contest':zip(render_contest,available_slots,percentage_full),'teams':userteams})
        else:
            raise ValueError("User Team Doesn't Exists.")
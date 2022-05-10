from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from mainAPP.repository import vision11, vision11_render

# Create your views here.


def RenderHomePage(request):
    '''
    This method is used for
    rendering home page.
    '''
    return render(request, 'home.html')


@login_required(login_url='/accounts/login')
def RenderDashboard(request):
    '''
    This method is used for
    rendering dashboard page.
    '''
    return render(request, 'dashboard.html')


@login_required(login_url='/accounts/login')
def RenderTodaysMatches(request):
    '''
    This method is used for
    rendering Today's Matches page.
    '''
    return render(request, 'Scheduled_matches.html')


def RenderAgeVerificationAdmin(request):
    if request.user.is_authenticated and request.user.is_staff:
        return vision11_render().render_age_adminportal(request)
    return redirect('/')


class GetAgeVerificationRequests(APIView):
    def get(self,request):
        try:
            if request.user.is_authenticated and request.user.is_staff:
                return vision11().get_age_verification_requests()
            return Response({'status':403,'message':'Invalid Credentials for admin.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})



class GetFeatureRequests(APIView):
    def get(self,request):
        try:
            if request.user.is_authenticated and request.user.is_staff:
                return vision11().get_features_requests()
            return Response({'status':403,'message':'Invalid Credentials for admin.'})
        except:
            return Response({'status':500,'message':'something went wrong.'})


def Set_Seen_FeatureRequest(request,fid):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return vision11().set_seen_fr(fid)
        return redirect('/')
    except:
        return redirect('/')


@login_required(login_url='/accounts/login')
def RenderTeamSelection(request,mid):
    '''
    This method is used for
    rendering Team selection page.
    '''
    try:
        return vision11().render_team_selection(request,mid)
    except:
        return redirect('/')

@login_required(login_url='/accounts/login')
def RenderContestPage(request,mid):
    '''
    This method is used for
    rendering Contest page.
    '''
    try:
        return vision11_render().render_contest(request,mid)
    except Exception as e:
        return redirect('/createteam/match='+str(mid))


@login_required(login_url='/accounts/login')
def RenderUserContest(request):
    '''
    This method is used for
    rendering User Contest page.
    '''
    try:
        return vision11_render().render_usercontest(request)
    except Exception as e:
        return redirect('/')


@login_required(login_url='/accounts/login')
def RenderContestDetails(request,cid):
    '''
    This method is used for
    rendering Contest details page.
    '''
    try:
        return vision11_render().render_contestdetails(request,cid)
    except Exception as e:
        print(e)
        return redirect('/userjoinedcontest')




@login_required(login_url='/accounts/login')
def RenderUserTeam(request,mid):
    '''
    This method is used for
    rendering User Team page.
    '''
    try:
        return vision11_render().render_userteam(request,mid)
    except Exception as e:
        return redirect('/createteam/match='+str(mid))



def handler_404(request, exception=None):
    '''
        view to handle 404 error
        attached in project level
        urls.py (vision11.urls)
    '''
    data = {}
    return render(request, '404error.html', data)




def handler_500(request,  exception=None):
    '''
        view to handle 500 error
        attached in project level
        urls.py (vision11.urls)
    '''
    data = {}
    return render(request, '500error.html', data)




def Save_Suggestion_Form(request):
    '''
        View Function to save suggesition
        in corresponding model
    '''
    try:
        if request.user.is_authenticated:
            return vision11().save_suggestion_form(request)
        return redirect('/')
    except:
        return redirect('/')




class GetTodaysMatchesListAPI(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return vision11().get_match_list()
        return Response({'status':403,'message':'Please authenticate yourself.'})





class GetFantasyScoreAPI(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                return vision11().get_fantasy_score(request.data['url'])
            except Exception as e:
                print(e)
                return Response({'status':500,'message':'Something went wrong please try again after some time.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})





class GetTodaysSquadList(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            try:
                return vision11().get_todays_squad(request.data['team1'],request.data['team2'])
            except Exception as e:
                print(e)
                return Response({'status':404,'message':'Either No contest available or timeline expired.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetCompletedMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_completed_matches()
            except:
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetLiveMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_Live_matches()
            except:
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




class GetUpcomingMatchesList(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                return vision11().get_upcoming_matches()
            except Exception as e:
                print(e)
                return Response({'status':500,'message':'something went wrong.'})
        return Response({'status':403,'message':'Please authenticate yourself.'})




def RenderStaffPage(request):
    try:
        if request.user.is_authenticated and request.user.is_staff:
            return render(request,'staff_page.html')
        return redirect('/')
    except:
        return redirect('/')




@login_required(login_url='/accounts/login')
def CreateUserTeam(request):
    try:
        return vision11().create_user_team(request.data)
    except:
        return redirect('/')




class FinalizeUserTeam(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().create_user_team(request.data,request.user)
            return Response({'status':403,'message':'unauthorized access please authenticated yourself.'})
        except Exception as e:
            print(e)
            return Response({'status':500,'message':'something went wrong.'})




class ContestCreateJoinAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().create_contest(request.data,request.user)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except Exception as e:
            print(e)
            return Response({'status':500,'message':'something went wrong.'})



class ContestSearchAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().search_contest(request.data)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except Exception as e:
            print(e)
            return Response({'status':500,'message':'something went wrong.'})



class ContestJoinAPI(APIView):
    def post(self,request):
        try:
            if request.user.is_authenticated:
                return vision11().join_contest(request.data,request.user)
            return Response({'status':403,'message':'please authenticate yourself.'})
        except Exception as e:
            print(e)
            return Response({'status':500,'message':'something went wrong.'})
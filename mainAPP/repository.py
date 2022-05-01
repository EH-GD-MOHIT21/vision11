from mainAPP.models import Match,Player,Team
from django.utils import timezone
from .serializers import MatchListSerializer,GameSquadSerializer
from rest_framework.response import Response

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

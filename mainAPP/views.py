from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from mainAPP.repository import vision11

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
def Render_show_league(request):
    return render(request, 'leagues.html')


@login_required(login_url='/accounts/login')
def RenderTodaysMatches(request):
    '''
    This method is used for
    rendering Today's Matches page.
    '''
    return render(request, 'Scheduled_matches.html')


@login_required(login_url='/accounts/login')
def RenderTeamSelection(request):
    '''
    This method is used for
    rendering Team selection page.
    '''
    return render(request, 'selecting_team.html')

@login_required(login_url='/accounts/login')
def RenderFeatureSuggestion(request):
    '''
    This method is used for
    rendering Feature Suggestion page.
    '''
    return render(request, 'feature_suggestion.html')


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



import json
from venv import create
from django.http import HttpResponse
from django.shortcuts import redirect, render
from chatsupportAPP.models import Queue
from django.contrib.auth.decorators import login_required
import requests
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from mainAPP.models import Team

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


class get_leagues(APIView):
    def get(self, request):
        url = 'https://apiv2.api-cricket.com/cricket/?method=get_leagues&APIkey=9bc453870544fc489f861bc5cac3646ad83f8782fef306adac0d22f66940b6ad'
        data = requests.get(url)
        return Response({'status': 200, 'data': json.loads(data.text)})


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
        pass


class GetLiveScoreAPI(APIView):
    def get(self, request):
        pass


class GetTeamsSquadList(APIView):
    def get(self, request):
        pass


     


 
        
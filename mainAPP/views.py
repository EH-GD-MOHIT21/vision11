import json
from django.shortcuts import redirect, render
from chatsupportAPP.models import Queue 
from django.contrib.auth.decorators import login_required
import requests
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

# Create your views here.


def RenderHomePage(request):
    '''
    This method is used for
    rendering home page.
    '''
    return render(request,'home.html')


@login_required(login_url='/login')
def RenderDashboard(request):
    '''
    This method is used for
    rendering dashboard page.
    '''
    return render(request,'dashboard.html')


def Calculate_Points_For_Match():
    pass


@login_required(login_url='/login')
def Render_show_league(request):
    return render(request,'leagues.html')


class get_leagues(APIView):
    def get(self,request):
        url = 'https://apiv2.api-cricket.com/cricket/?method=get_leagues&APIkey=9bc453870544fc489f861bc5cac3646ad83f8782fef306adac0d22f66940b6ad'
        data = requests.get(url)
        return Response({'status':200,'data':json.loads(data.text)})
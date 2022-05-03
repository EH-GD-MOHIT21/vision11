from django.urls import path
from . import views

urlpatterns = [
    path('',views.RenderHomePage),   
    path('dashboard',views.RenderDashboard),
    path('today_matches', views.RenderTodaysMatches),
    path('team_selection',views.RenderTeamSelection),   
    path('gettodaysmatchlist',views.GetTodaysMatchesListAPI.as_view()),  
    path('gettodayssquadlist',views.GetTodaysSquadList.as_view()),  
    path('getfantasyscore',views.GetFantasyScoreAPI.as_view()),
]

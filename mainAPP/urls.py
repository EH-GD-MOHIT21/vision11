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
    path('getcompletedmatches',views.GetCompletedMatchesList.as_view()),
    path('getlivematches',views.GetCompletedMatchesList.as_view()),
    path('getupcomingmatches',views.GetCompletedMatchesList.as_view()),
    path('ageverification/admin_portal',views.RenderAgeVerificationAdmin),
    path('suggestions',views.Save_Suggestion_Form),
    path('staff',views.RenderStaffPage),
    path('getageverificationrequests',views.GetAgeVerificationRequests.as_view()),
    path('getfeaturerequests',views.GetFeatureRequests.as_view()),
    path('fr/mark_as_seen/fid=<int:fid>',views.Set_Seen_FeatureRequest),
]

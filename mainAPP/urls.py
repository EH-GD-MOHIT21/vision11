from django.urls import path
from . import views

urlpatterns = [
    path('',views.RenderHomePage),   
    path('dashboard',views.RenderDashboard),
    path('play', views.RenderTodaysMatches),
    path('createteam/match=<int:mid>',views.RenderTeamSelection),   
    path('gettodaysmatchlist',views.GetTodaysMatchesListAPI.as_view()),  
    path('gettodayssquadlist',views.GetTodaysSquadList.as_view()),  
    path('getfantasyscore',views.GetFantasyScoreAPI.as_view()),
    path('getcompletedmatches',views.GetCompletedMatchesList.as_view()),
    path('getlivematches',views.GetLiveMatchesList.as_view()),
    path('getupcomingmatches',views.GetUpcomingMatchesList.as_view()),
    path('ageverification/admin_portal',views.RenderAgeVerificationAdmin),
    path('suggestions',views.Save_Suggestion_Form),
    path('staff',views.RenderStaffPage),
    path('getageverificationrequests',views.GetAgeVerificationRequests.as_view()),
    path('getfeaturerequests',views.GetFeatureRequests.as_view()),
    path('fr/mark_as_seen/fid=<int:fid>',views.Set_Seen_FeatureRequest),
    path('contest/match=<int:mid>',views.RenderContestPage),
    path('finalizeteam',views.FinalizeUserTeam.as_view()),
    path('createcontestapi',views.ContestCreateJoinAPI.as_view()),
    path('searchcontestapi',views.ContestSearchAPI.as_view()),
    path('joincontestapi',views.ContestJoinAPI.as_view()),
    path('userteam/match=<int:mid>',views.RenderUserTeam),
    path('userjoinedcontest',views.RenderUserContest),
    path('contestdetails/contest=<int:cid>',views.RenderContestDetails),
]

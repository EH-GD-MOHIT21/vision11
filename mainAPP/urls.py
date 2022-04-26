from django.urls import path
from . import views

urlpatterns = [
    path('',views.RenderHomePage),   
    path('dashboard',views.RenderDashboard),
    path('get_leagues',views.get_leagues.as_view()),
]

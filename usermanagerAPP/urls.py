from django.urls import path
from . import views

urlpatterns = [
    path('check/username',views.CheckForUsername.as_view()),
    path('check/email',views.CheckForEmail.as_view()),
]

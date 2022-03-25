from django.urls import path
from . import views

urlpatterns = [
    path('paymenthandler/', views.paymenthandler),
    path('home', views.homepage),
]

from django.urls import path
from . import views

urlpatterns = [
    path('purchase/paymenthandler/', views.paymenthandler),
    path('home', views.render_offer_page),
    path('purchase/offer=<int:offerid>',views.homepage),
]

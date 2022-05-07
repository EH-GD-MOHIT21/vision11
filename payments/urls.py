from django.urls import path
from . import views

urlpatterns = [
    path('purchase/paymenthandler/', views.paymenthandler),
    path('purchase/offer=<int:offerid>',views.homepage),
    path('getplans',views.GetOfferListAPI.as_view())
]

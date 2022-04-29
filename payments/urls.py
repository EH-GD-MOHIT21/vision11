from django.urls import path
from . import views

urlpatterns = [
    path('purchase/paymenthandler/', views.paymenthandler),
    path('purchase', views.render_offer_page),
    path('purchase/offer=<int:offerid>',views.homepage),
]

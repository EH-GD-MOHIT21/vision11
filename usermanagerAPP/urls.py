from django.urls import path
from . import views

urlpatterns = [
    path('check/username',views.CheckForUsername.as_view()),
    path('check/email',views.CheckForEmail.as_view()),
    path('upload_valid_age_doc',views.AgeVerificationUploadDocument),
    path('accept_request/pid=<int:pid>',views.accept_age_verification_request),
    path('deny_request/pid=<int:pid>',views.deny_age_verification_request),
]

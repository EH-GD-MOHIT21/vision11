from django.shortcuts import render
from .models import User1
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_406_NOT_ACCEPTABLE,HTTP_400_BAD_REQUEST
import re


class CheckForUsername(APIView):
    def post(self,request,*args):
        data = request.data
        try:
            User1.objects.get(username=data["username"])
            return Response({'status':HTTP_406_NOT_ACCEPTABLE,'message':'Username not available.'})
        except User1.DoesNotExist:
            if len(data["username"]) and data["username"].isalnum():
                return Response({'status':HTTP_200_OK,'message':'Username Available.'})
            return Response({'status':HTTP_200_OK,'message':'Please enter valid username of alpha num values.'})
        except:
            return Response({'status':HTTP_400_BAD_REQUEST,'message':'Invalid Request.'})


class CheckForEmail(APIView):
    def post(self,request,*args):
        data = request.data
        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.fullmatch(regex, data["email"])):
                return Response({'status':HTTP_200_OK,'message':'Please enter valid Email.'})
            User1.objects.get(email=data["email"])
            return Response({'status':HTTP_406_NOT_ACCEPTABLE,'message':'Email not available.'})
        except User1.DoesNotExist:
            return Response({'status':HTTP_200_OK,'message':'Email Available.'})
        except:
            return Response({'status':HTTP_400_BAD_REQUEST,'message':'Invalid Email.'})
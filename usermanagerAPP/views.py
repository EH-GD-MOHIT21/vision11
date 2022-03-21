from django.shortcuts import render
from .models import User1
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_406_NOT_ACCEPTABLE,HTTP_400_BAD_REQUEST



class CheckForUsername(APIView):
    def post(self,request,*args):
        data = request.data
        try:
            User1.objects.get(username=data["username"])
            return Response({'status':HTTP_406_NOT_ACCEPTABLE,'message':'Username not available.'})
        except User1.DoesNotExist:
            if len(data["username"]):
                return Response({'status':HTTP_200_OK,'message':'Username Available.'})
            return Response({'status':HTTP_200_OK,'message':'Please enter username.'})
        except:
            return Response({'status':HTTP_400_BAD_REQUEST,'message':'Invalid Request.'})


class CheckForEmail(APIView):
    def post(self,request,*args):
        data = request.data
        try:
            User1.objects.get(email=data["email"])
            return Response({'status':HTTP_406_NOT_ACCEPTABLE,'message':'Email not available.'})
        except User1.DoesNotExist:
            if len(data["email"]):
                return Response({'status':HTTP_200_OK,'message':'Email Available.'})
            return Response({'status':HTTP_200_OK,'message':'Please enter Email.'})
        except:
            return Response({'status':HTTP_200_OK,'message':'Email Available.'})
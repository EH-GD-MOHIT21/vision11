from django.shortcuts import redirect
from .models import User1
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_406_NOT_ACCEPTABLE, HTTP_400_BAD_REQUEST
import re
from vision11.email.send_email import send_mail
from .serializers import UserSerializer
from payments.models import Order
from payments.serializers import OrderSerializer

class UserValidation:
    '''
        Utility class to check if a mail/username is valid
        or not or either it already exists or not.\n
        methods:
            validate_username(instance,data) -> Response object\n
            validate_email(instance,data) -> Response object

        Response object contains:
            {
                "status": status_code (200,404,500 etc.)
                "message": log about username or email.
            }
    '''

    def validate_username(self, data):
        '''
            Method for check if username already exists
            or not and validates username.
        '''
        try:
            User1.objects.get(username=data["username"])
            return Response({'status': HTTP_406_NOT_ACCEPTABLE, 'message': 'Username not available.'})

        except User1.DoesNotExist:
            if len(data["username"]) and data["username"].isalnum():
                return Response({'status': HTTP_200_OK, 'message': 'Username Available.'})

            return Response({'status': HTTP_200_OK, 'message': 'Please enter valid username of alpha num values.'})

        except:
            return Response({'status': HTTP_400_BAD_REQUEST, 'message': 'Invalid Request.'})

    def validate_email(self, data):
        '''
            Method for check if email already exists
            or not and validates email.
        '''
        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            if not (re.fullmatch(regex, data["email"])):
                return Response({'status': HTTP_200_OK, 'message': 'Please enter valid Email.'})

            User1.objects.get(email=data["email"])
            return Response({'status': HTTP_406_NOT_ACCEPTABLE, 'message': 'Email not available.'})

        except User1.DoesNotExist:
            return Response({'status': HTTP_200_OK, 'message': 'Email Available.'})

        except:
            return Response({'status': HTTP_400_BAD_REQUEST, 'message': 'Invalid Email.'})
    
    
    def upload_age_verification_document(self,data,user):
        '''
            Uploads the provided file to static/imgs/other
            folder
        '''
        try:
            file = data['age_validation_doc']
            user.aadhar_image = file
            user.save()
            return redirect('/dashboard')
        except Exception as e:
            print(e)
            return redirect('/dashboard')


class admin_user_roles:
    
    def accept_age_verification_request(self,pid):
        user = User1.objects.get(id=pid)
        user.adult = True
        user.save()
        send_mail(to=[user.email],subject=f'Hurry {user.username}! Your request for age verification is Approved.',message=f'Hey {user.username}!\n\nYour age verification request finally got approved today. You can now make purchase on vision11, can earn money, can play paid contests and many more features are unlocked now for you. See you in vision11\n\n\n Thanks and regards\n\n\nVision11.com')

        return redirect('/staff')


    def deny_age_verification_request(self,pid):
        user = User1.objects.get(id=pid)
        user.aadhar_image = None
        user.save()
        send_mail(to=[user.email],subject=f'Sorry {user.username}! Your request for age verification is rejected.',message=f'Sorry {user.username}!\n\nWe understand about your efforts but this time your age verification request has been removed by our admin support either the document you\'ve uploaded is invalid or you are not 18+ years old. please try after some time with a legal document that can prove your age is 18+.\n\n\n Thanks and regards\n\n\nVision11.com')
        return redirect('/staff')


class UserDetails:

    def get_user_details(self,user):
        real_user = User1.objects.get(username=user)
        serializer = UserSerializer(real_user)
        orders = Order.objects.filter(user=real_user)
        serializer1 = OrderSerializer(orders,many=True)
        return Response({'status':200,'message':'success','user':serializer.data,'orders':serializer1.data})
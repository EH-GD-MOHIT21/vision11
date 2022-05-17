from rest_framework.serializers import ModelSerializer
from .models import User1

class UserSerializer(ModelSerializer):
    class Meta:
        model = User1
        fields = ['id','username','email','age','aadhar_image','country']
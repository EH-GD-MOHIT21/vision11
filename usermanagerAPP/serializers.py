from rest_framework.serializers import ModelSerializer
from .models import User1,VisionCurrencyDetails

class UserSerializer(ModelSerializer):
    class Meta:
        model = User1
        fields = ['id','username','email','age','aadhar_image','country']


class VisionCurrencyDetailsSeraializer(ModelSerializer):
    class Meta:
        model = VisionCurrencyDetails
        fields = "__all__"
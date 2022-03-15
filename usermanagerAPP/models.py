from django.db import models
from .models_manager import UserManager
from django.contrib.auth.models import AbstractUser,User

Currency_Choices=[
    ('vision coins', 'vision coins'),
    ('vision candies' ,'vision candies')
]
Gender_Choices=[
    ('Male', 'Male'),
    ('Female', 'Female')
]
class User1(AbstractUser):
    first_name = models.CharField(max_length=100)   
    second_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)
    vision_credits=models.FloatField(default=0)
    currency_type = models.CharField(choices=Currency_Choices,default=Currency_Choices[1],max_length=50)
    gender_type = models.CharField(choices=Gender_Choices,null=True,max_length=10)
    country = models.CharField(max_length=100)
    is_adult = models.BooleanField('Adult_status',default=False)
    is_staff = models.BooleanField('Staff_status',default=False)
    is_superuser = models.BooleanField('super_user_status',default=False)
    aadhar_image = models.FileField(upload_to='imgs',null=True,blank=True)
    objects=UserManager()


    
from django import forms

Currency_Choices=[
    ('vision coins', 'vision coins'),
    ('vision candies' ,'vision candies')
]
Gender_Choices=[
    ('Male', 'Male'),
    ('Female', 'Female')
]

# Signup fields other than default in allauth package
class Signup_details(forms.Form):
    first_name = forms.CharField(max_length=100)   
    second_name = forms.CharField(max_length=100)
    username=forms.CharField(max_length=30,unique=True)
    age = forms.IntegerField(null=True,blank=True)
    email=forms.EmailField()
    vision_credits=forms.FloatField(default=0)
    currency_type = forms.CharField(choices=Currency_Choices,default=Currency_Choices[1],max_length=50)
    gender_type = forms.CharField(choices=Gender_Choices,null=True,max_length=10)
    country = forms.CharField(max_length=100)
    adult = forms.BooleanField('Adult_status',default=False)
    staff = forms.BooleanField('Staff_status',default=False)
    superuser = forms.BooleanField('super_user_status',default=False)
    aadhar_image = forms.FileField(upload_to='others',null=True,blank=True)
      
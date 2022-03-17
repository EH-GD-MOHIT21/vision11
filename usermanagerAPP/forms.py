from django import forms
from django.contrib.auth.forms import UserCreationForm

Currency_Choices=[
    ('vision coins', 'vision coins'),
    ('vision candies' ,'vision candies')
]
Gender_Choices=[
    ('Male', 'Male'),
    ('Female', 'Female')
]

# Signup fields other than default in allauth package
class Signup_details(UserCreationForm):
    first_name = forms.CharField(max_length=20)   
    second_name = forms.CharField(max_length=20)
    username=forms.CharField(max_length=20)
    age = forms.IntegerField()
    email=forms.EmailField()
    gender_type = forms.CharField(max_length=10)
    country = forms.CharField(max_length=50)
    Id_proof = forms.FileField()

    def signup(self, request):
        user = super(Signup_details, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.second_name = self.cleaned_data['second_name']
        user.username = self.cleaned_data['username']
        user.age = self.cleaned_data['age']
        user.email = self.cleaned_data['email']
        user.gender_type = self.cleaned_data['gender_type']
        user.country = self.cleaned_data['country']
        user.aadhar_image = self.cleaned_data['Id_proof']
        user.save()
        return user
      
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


Currency_Choices = [
    ('vision candies', 'vision candies'),
    ('vision coins', 'vision coins')
]


Gender_Choices = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

# Signup fields other than default in allauth package


class Signup_details(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    age = forms.IntegerField()
    email = forms.EmailField()
    gender_type = forms.ChoiceField(choices=Gender_Choices)
    country = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'username',
                  'email', 'gender_type', 'country')

    def signup(self, request):
        user = super(Signup_details, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.age = self.cleaned_data['age']
        user.email = self.cleaned_data['email']
        user.gender_type = self.cleaned_data['gender_type']
        user.country = self.cleaned_data['country']
        user.save()
        return user

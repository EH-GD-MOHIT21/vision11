from django import forms

# Signup fields other than default in allauth package
class Signup_details(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)   
    second_name = forms.CharField(label='Second name', max_length=100)
      
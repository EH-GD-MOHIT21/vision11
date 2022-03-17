from django.shortcuts import render

# Create your views here.

def RenderLoginPage(request):
    return render(request,'vision_login.html')


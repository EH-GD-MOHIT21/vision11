from django.shortcuts import render

# Create your views here.


def RenderHomePage(request):
    '''
    This method is used for
    rendering home page.
    '''
    return render(request,'home.html')


def RenderDashboard(request):
    '''
    This method is used for
    rendering dashboard page.
    '''
    return render(request,'dashboard.html')
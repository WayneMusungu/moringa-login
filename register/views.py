from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the login page')

@login_required
def welcome(request):
    return render(request, 'welcome.html')



@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('welcome')

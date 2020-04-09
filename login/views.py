from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    
    return render(request,'login/login.html',{'status':'none'})

def logout(request):
    return render(request,'login/login.html',{'status':'none'})

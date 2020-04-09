from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import csv
from django.contrib.auth import authenticate
# Create your views here.

def welcome(request):
    user=authenticate(username=request.POST['username'],password=request.POST['password'])
    if user is not None:
        statfields=[]
        statlist=[]
        with open("statics/csv/distance_up.csv", 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            statfields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                statlist.append(row[0])
        return render(request, 'welcome/welcome.html',{"statlist":statlist})

    else:
        return render(request, 'login/login.html',{'status':'block'})
    
def welcome_logged_in(request):
    statfields=[]
    statlist=[]
    with open("statics/csv/distance_up.csv", 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        statfields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            statlist.append(row[0])
    return render(request, 'welcome/welcome.html',{"statlist":statlist})

def index(request):
    template=loader.get_template('welcome/index.html')
    context={

    }
    return render(request, 'welcome/index.html',context)

def services(request):
    template=loader.get_template('welcome/services.html')
    context={

    }
    return render(request, 'welcome/services.html',context)

def update_log(request):
    template=loader.get_template('welcome/blog.html')
    context={

    }
    return render(request, 'welcome/blog.html',context)
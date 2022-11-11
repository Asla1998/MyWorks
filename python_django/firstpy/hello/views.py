from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')   


def login(request):
    return render(request,'login.html') 


def registration(request):
    return render(request,'registration.html') 

# from django.http import HttpResponse


# def helloworld(request):
#     return HttpResponse("<h2>Hello, Welcome to django</h2>")

# Create your views here.

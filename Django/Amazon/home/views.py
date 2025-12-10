from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my home page!")

def contact(request):
    return HttpResponse("This is my Contact page!")

def about(request):
    return HttpResponse("This is my about page!")

def login(request):
    return HttpResponse("This is my login page!")

def register(request):
    return HttpResponse("This is my Register Page!")



from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def index(request,age):
    return HttpResponse("Hi, my age  is $age :" %age)

from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    response = []
    response.append("Rango says hey there partner!")
    url_about = "<a href='/rango/about/'>About</a>"
    response.append(url_about)
    return HttpResponse(response)

def about(request):
    response = []
    url_index = "<a href='/rango/'>Index</a>"
    response.append("Rango says here is the about page.")
    response.append(url_index)
    return HttpResponse(response)

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world<br/> <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says this is the about page<br/>"
                        " <a href='/rango/'>Index</a><br/>Made by Jim Walker<br/>2096502w")
from django.shortcuts import render

# Create your views here.from django.http import HttpResponse
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!")
def about(request):
    return HttpResponse("Rango says here is the about page! <br/> <a href= '/rango'> Main Page</a>")

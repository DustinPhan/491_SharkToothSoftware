from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(HttpRequest):
    print(HttpRequest.path)
    return HttpResponse("<body><h1>test</h1></body>")
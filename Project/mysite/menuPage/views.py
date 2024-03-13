from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    print(request)
    return HttpResponse("<body><h1>test</h1></body>")


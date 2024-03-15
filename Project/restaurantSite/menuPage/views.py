from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(HttpRequest):
    print(HttpRequest.path)
    #return HttpResponse("<head><title>" + HttpRequest.path[1:-1] + "</title></head><body><h1>test</h1></body>")
    return render(HttpRequest, "index.html")
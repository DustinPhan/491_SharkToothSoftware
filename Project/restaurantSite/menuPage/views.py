from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Person
from .forms import PersonForm

# Create your views here.
def index(HttpRequest):
    print(HttpRequest.path)
    #return HttpResponse("<head><title>" + HttpRequest.path[1:-1] + "</title></head><body><h1>test</h1></body>")
    return render(HttpRequest, "index.html")

# Mayhaps something...
# def person(request):
#     if request.method == 'POST':
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect or do something else
#     else:
#         form = PersonForm()
#     return render(request, 'person.html', {'form': form})
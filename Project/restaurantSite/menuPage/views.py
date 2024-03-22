# Unneeded?
# from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import PersonForm

# Create your views here.
def index(request):
    print(request.path)
    #return HttpResponse("<head><title>" + HttpRequest.path[1:-1] + "</title></head><body><h1>test</h1></body>")
    return render(request, "index.html")

def person_data_view(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'person_data.html', {'form': form})

def success(request):
    return render(request, 'success.html')
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse('<h1>Good start</h1>')
    return render(request, 'pages/home.html', {})

def contact_view(request, *args, **kwargs):
    print(request)
    return render(request, 'pages/contact.html', {})
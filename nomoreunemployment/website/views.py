from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me': "Hello I'm from website views.py !"}
    return render(request, 'index.html', context=my_dict)


def about(request):
    my_dict = {'insert_me': "Hello I'm from website views.py !"}
    return render(request, 'about.html', context=my_dict)


def contact(request):
    my_dict = {'insert_me': "Hello I'm from website views.py !"}
    return render(request, 'contact.html', context=my_dict)

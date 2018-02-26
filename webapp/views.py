from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'webapp/home.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def about(request):
    return render(request, 'webapp/about.html')
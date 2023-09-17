from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

def index(request): 
    return render(request, 'index.html')

def service(request): 
    return render(request, 'services.html')
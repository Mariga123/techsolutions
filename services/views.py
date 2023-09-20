from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from techsolutions.forms import ContactForm

def index(request): 
    return render(request, 'index.html')

def service(request): 
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request):
    return render(request, 'index.html')

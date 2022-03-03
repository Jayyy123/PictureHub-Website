from django.shortcuts import render
import requests

def home(request):
    
    
    return render(request, 'rphbase/home.html')

def about(request):

    return render(request, 'rphbase/about.html')

def contact(request):

    return render(request, 'rphbase/contact.html')

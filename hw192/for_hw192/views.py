from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'hw192/home.html')

def contacts(request):
    return render(request, 'hw192/contacts.html')
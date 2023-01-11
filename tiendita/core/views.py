from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, "core/partesuperior.html")

def about(request):
     return render (request, "core/parteinferior.html")

def contact(request):
     return render (request, "core/contact.html")



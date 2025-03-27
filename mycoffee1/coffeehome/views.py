from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def locations(request):
    return render(request,'locations.html')

def menu(request):
    return render(request,'menu.html')
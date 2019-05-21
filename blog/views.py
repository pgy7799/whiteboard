from django.shortcuts import render, redirect
from .models import Blog

def home(request):
    saves = Blog.objects
    return render(request, 'home.html', {'saves': saves})

def submit(request):
    k = Blog()
    k.message = request.GET['message']
    k.name= request.GET['name']
    k.date= request.GET['date']
    k.save()
    return redirect('/')
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return redirect('/books/')

def about(request):
    return render(request, 'about.html')

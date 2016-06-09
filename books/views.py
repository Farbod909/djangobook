from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books/index.html', {'books':books})
    elif request.method == 'POST':
        try:
            Book(
                title=request.POST['title'],
                author=request.POST['author'],
                page_count=request.POST['page_count']
            ).save()
        except:
            return HttpResponse('fail')
        else:
            return HttpResponse('success')

def create(request):
    return render(request, 'books/create.html')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from library_app.models import Book

books = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladie\'s Detective Agency', 'author': 'Alexander McCall Smith'}
]

def index(req):
    context = {'books': Book.objects.all()}
    return render(req, 'library_app/index.html', context )

def show(req, id):
    context = {'book': Book.objects.get(pk=id)}
    return render(req, 'library_app/show.html', context )

def not_found_404(req, exception):
    return render(req, 'library_app/error404.html')

def server_error_500(req, exception):
    return render(req, 'library_app/error404.html')
    
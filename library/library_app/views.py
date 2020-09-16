from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

books = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladie\'s Detective Agency', 'author': 'Alexander McCall Smith'}
]

def index(req):
    # return HttpResponse("<h1>Test View<h1>")
    context = {'books': books}
    return render(req, 'library_app/index.html', context )

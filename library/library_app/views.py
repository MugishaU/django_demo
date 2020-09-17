from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from library_app.models import Book as Books

@login_required
def index(req):
    context = {'books': Books.objects.all()}
    return render(req, 'library_app/index.html', context )

@login_required
def show(req, id):
    context = {'book': Books.objects.get(pk=id)}
    return render(req, 'library_app/show.html', context )

def not_found_404(req, exception):
    return render(req, 'library_app/error404.html')

def server_error_500(req, exception):
    return render(req, 'library_app/error404.html')
    
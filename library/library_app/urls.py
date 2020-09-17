from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='library_app.index'),
    path('book/<int:id>/', views.show, name='library_app.show'),
]
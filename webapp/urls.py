from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('blog', views.Blog_Post, name='blog'),
]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.suk, name='suk'),
    path('sukaldariak/', views.suk, name='suk'),
    path('sukaldariak/add', views.suk, name='suk'),
]
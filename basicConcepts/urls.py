# basicConcepts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome,name='Welcome'),
    path('User', views.User, name='User')
]

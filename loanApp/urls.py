from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    path('data-analysis/', views.data_analysis, name='data_analysis'),
    path('about-project/', views.about_project, name='about_project'),
]

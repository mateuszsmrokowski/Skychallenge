from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_exams', views.add_exams, name='add_exams')
]

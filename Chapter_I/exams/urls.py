from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_exams', views.add_exams, name='add_exams'),
    path('modify_exams', views.modify_exams, name='modify_exams'),
    path('save_exam', views.save_exam, name='save_exam')
]

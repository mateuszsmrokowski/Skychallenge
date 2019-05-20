from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_exams', views.add_exams, name='add_exams'),
    path('<int:exam_id>/modify_exam/', views.save_exam_edit, name='save_exam_edit'),
    path('save_exam', views.save_exam, name='save_exam'),
    path('<int:exam_id>/', views.modify_exams, name='modify_exams'),
    path('<int:exam_id>/delete_exam', views.delete_exam, name="delete_exam"),
    path('login_view', views.login_view, name="login_view"),
    path('login', views.login, name="login"),
    path('log_out', views.log_out, name="log_out")
]

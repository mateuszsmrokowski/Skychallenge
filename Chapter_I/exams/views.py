from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Exams, Grade
from django.template import loader
from django.contrib import messages

def index(request):
    exams_list = Exams.objects.all()
    template = loader.get_template('exams/index.html')
    context = {
        'exams_list': exams_list
    }
    #output = ', '.join([q.name for q in students_list])
    return HttpResponse(template.render(context, request))

def add_exams(request):
    exams_list = Exams.objects.all()
    students_list = Students.objects.all()
    template = loader.get_template('exams/add_exams.html')
    context = {
        'exams_list': exams_list,
        'students_list': students_list
    }
    return HttpResponse(template.render(context, request))

def save_exam(request, *args, **kwargs):
    students_list = Exams.objects.all()
    exam_name = request.GET.get('exam_name')
    sok = request.GET.get('exam_sok')
    exam_date = request.GET.get('exam_date')
    points_list = request.GET.getlist('points')
    grades_list = request.GET.getlist('grade')
    print (exam_name, sok, exam_date, points_list, grades_list)
    E = Exams(name=exam_name, scope_of_knowledge=sok, date=exam_date)
    E.save()
    for i in range(1, len(grades_list)+1):
        Stud = Students.objects.get(pk=i)
        G = Grade(student=Stud.name+""+Stud.surname, points = points_list[i-1], grade = grades_list[i-1], exam = E)
        G.save()
    #stud_grades = []
    return HttpResponse(request)

def modify_exams(request):
    return HttpResponse(request)

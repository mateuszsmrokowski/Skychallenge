from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Exams, Grade
from django.template import loader


def index(request):
    students_list = Exams.objects.all()
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

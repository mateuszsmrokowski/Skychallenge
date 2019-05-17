from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
from django.template import loader


def index(request):
    students_list = Students.objects.all()
    template = loader.get_template('exams/index.html')
    context = {
        'students_list': students_list
    }
    #output = ', '.join([q.name for q in students_list])
    return HttpResponse(template.render(context, request))

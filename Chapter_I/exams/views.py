from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Exams, Grade, ExamsOwners
from django.template import loader
from django.contrib import messages
from django.http import HttpResponseRedirect

def index(request):
    exams_list = Exams.objects.all()
    template = loader.get_template('exams/index.html')
    user_type = request.session.get('user')

    if not user_type:
       request.session['user_id'] = -1
       request.session['user'] = 'normal'
    context = {
        'exams_list': exams_list,
        'user_type': user_type
    }
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
    i = 1
    students_list = Students.objects.all()
    exam_name = request.GET.get('exam_name')
    sok = request.GET.get('exam_sok')
    exam_date = request.GET.get('exam_date')
    points_list = request.GET.getlist('points')
    grades_list = request.GET.getlist('grade')
    Owner = ExamsOwners.objects.get(pk=request.session['user_id'])
    E = Exams(name=exam_name, scope_of_knowledge=sok, date=exam_date, owner=Owner)
    E.save()
    for stud in students_list:
        G = Grade(student_id = stud.id, points = points_list[i-1], grade = grades_list[i-1], exam = E)
        G.save()
        i += 1
    return home(request)

def modify_exams(request, exam_id):
    students_list = []
    template = loader.get_template('exams/modify_exams.html')
    Exam = Exams.objects.get(pk=exam_id)
    grade_list = Grade.objects.filter(exam=Exam)
    for i in grade_list:
        Stud = Students.objects.get(pk=i.student_id)
        students_list.append({"name": Stud.name, "surname": Stud.surname , "points": i.points, "grade": i.grade, "id": Stud.id})
    user_type = request.session.get('user')
    if not user_type:
       request.session['user_id'] = -1
       request.session['user'] = 'normal'
    if user_type == 'owner' and not Exam.owner.id == request.session['user_id']:
        user_type = "normal"

    context = {
        'exam_name': Exam.name,
        'exam_sok': str(Exam.scope_of_knowledge),
        'exam_date': Exam.date,
        'students_list': students_list,
        'user_type': user_type

    }
    return HttpResponse(template.render(context, request))

def save_exam_edit(request, exam_id):
    i = 0
    students_list = Students.objects.all()
    Exam = Exams.objects.get(pk=exam_id)
    grade_list = Grade.objects.filter(exam=Exam)
    Exam.name = Exam.name
    Exam.scope_of_knowledge = request.GET.get('exam_sok')
    Exam.date = request.GET.get('exam_date')
    Exam.save()
    points_list = request.GET.getlist('points')
    grades_list = request.GET.getlist('grade')
    Grades = Grade.objects.filter(exam = Exam)
    for stud in students_list:
        for Grad in Grades:
            if Grad.student_id == stud.id:
                Grad.points = points_list[i]
                Grad.grade = grades_list[i]
                Grad.save()
                i += 1
    return home(request)

def delete_exam(request, exam_id):
    Exams.objects.get(pk=exam_id).delete()
    exams_list = Exams.objects.all()
    return home(request)


def login_view(request):
    template = loader.get_template('exams/login.html')
    return render(request, 'exams/login.html')

def login(request):
    username = request.GET.get('user_name')
    password = request.GET.get('user_password')
    accounts = ExamsOwners.objects.all()
    for acc in accounts:
        if acc.user_name == username and acc.user_password == password:
            request.session['user'] = 'owner'
            request.session['user_id'] = acc.id
            print (acc.id)

    return home(request)

def log_out(request):
    request.session['user'] = 'normal'
    request.session['user_id'] = -1
    return home(request)

def home(request):
      return HttpResponseRedirect('/exams/')

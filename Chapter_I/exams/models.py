from django.db import models

class Exams(models.Model):
    scope_of_knowledge = models.CharField(max_length=200)
    date = models.DateTimeField('Date of exam')


class Grade(models.Model):
    student = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)

class Students(models.Model):
    Name = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Age = models.IntegerField(default=0)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

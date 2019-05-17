from django.db import models

class Exams(models.Model):
    scope_of_knowledge = models.CharField(max_length=200)
    date = models.DateTimeField('Date of exam')


class Grade(models.Model):
    student = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    def __str__(self):
        return self.student, self.points, self.grade

class Students(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    def __str__(self):
        return self.name, self.surname
    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

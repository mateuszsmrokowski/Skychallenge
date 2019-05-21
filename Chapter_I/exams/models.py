from django.db import models

class ExamsOwners(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)

class Exams(models.Model):
    scope_of_knowledge = models.CharField(max_length=200)
    date = models.DateTimeField('Date of exam')
    name = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(ExamsOwners, on_delete=models.CASCADE, blank=True, null=True)

class Grade(models.Model):
    student_id = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    grade = models.FloatField(default=0)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)

class Students(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name, self.surname

from django.db import models

class Exams(models.Model):
    scope_of_knowledge = models.CharField(max_length=200)
    date = models.DateTimeField('Date of exam')
    name = models.CharField(max_length=200, null=True)

class Grade(models.Model):
    student_id = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    grade = models.FloatField(default=0)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)

    #def __str__(self):
    #    return self.student_id, self.points, self.grade

class Students(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name, self.surname
    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

# Generated by Django 2.2.1 on 2019-05-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0006_remove_students_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student_id',
            field=models.IntegerField(default=0),
        ),
    ]

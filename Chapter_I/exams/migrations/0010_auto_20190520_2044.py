# Generated by Django 2.2.1 on 2019-05-20 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_exams_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exams',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Exams_owners',
        ),
    ]

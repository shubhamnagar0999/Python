# Generated by Django 3.2.9 on 2022-01-26 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutns', '0002_rename_students_teacher_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='Student',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]

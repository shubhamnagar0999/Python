# Generated by Django 3.2.9 on 2022-01-26 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutns', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='students',
            new_name='Student',
        ),
    ]

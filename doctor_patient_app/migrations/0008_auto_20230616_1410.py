# Generated by Django 3.2.18 on 2023-06-16 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_patient_app', '0007_doctor_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='CheckBox',
        ),
        migrations.RemoveField(
            model_name='petient',
            name='CheckBox',
        ),
    ]

# Generated by Django 3.2.18 on 2023-06-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_patient_app', '0004_auto_20230615_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Profile_Pic',
            field=models.ImageField(upload_to='profile_pic_doc'),
        ),
        migrations.AlterField(
            model_name='petient',
            name='Pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='petient',
            name='Profile_Pic',
            field=models.ImageField(upload_to='profile_pic_doc'),
        ),
    ]

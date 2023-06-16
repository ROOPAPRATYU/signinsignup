from django.db import models

# Create your models here.
class Doctor(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Profile_Pic=models.ImageField(upload_to="profile_pic_doc",null=True,default=None)
    Username=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    Address_line1=models.CharField(max_length=200)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pincode=models.IntegerField()

    def _str__(self) -> str:
        return self.Username


# Create your models here.
class Petient(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Profile_Pic=models.ImageField(upload_to="profile_pic_doc")
    Username=models.CharField(max_length=100)
    Email_Id=models.EmailField(max_length=100)
    Password=models.CharField(max_length=100)
    Confirm_Password=models.CharField(max_length=100)
    Address_line1=models.CharField(max_length=200)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Pincode=models.IntegerField()

    def _str__(self)->str:
        return self.Username

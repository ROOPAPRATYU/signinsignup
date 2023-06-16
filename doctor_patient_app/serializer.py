from rest_framework import serializers
from .models import Doctor,Petient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields=["First_Name","Last_Name","Profile_Pic","Username","Email_Id","Password","Confirm_Password","Address_line1","City","State","Pincode"]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Petient
        fields=["First_Name","Last_Name","Profile_Pic","Username","Email_Id","Password","Confirm_Password","Address_line1","City","State","Pincode"]
    
class LoginDoctorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Doctor
        fields =['email', 'password']

class LoginPatientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Petient
        fields =['email', 'password']

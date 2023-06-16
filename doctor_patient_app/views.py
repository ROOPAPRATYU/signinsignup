from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import mixins,generics,status
from rest_framework.request import Request
from .models import Doctor,Petient
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializer import DoctorSerializer,PatientSerializer,LoginPatientSerializer,LoginDoctorSerializer
from .form import DoctorForm,PatientForm,PatientLoginForm,DoctorLoginForm

# Create your views here.
#Create Sign up view for Doctor
class DoctorRegisterView(generics.CreateAPIView):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

    def get(self, request:Request, *args, **kwargs):
        form = DoctorForm()
        return render(request, 'Doctor_signup.html', {'form': form})
    
    def post(self, request:Request,*args,**kwargs):
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.data.get('Password')
            confirm_password = form.data.get('Confirm_Password')
        
            if password != confirm_password:
                error_message = "Password and Confirm Password do not match"
                return render(request, 'Patient_signup.html', {'form': form, 'error_message': error_message})
            else:
                patient = form.save()
                message="Registered Successufylly!!!"
                return render(request, 'Patient_signup.html', {'form': form,"message":message})
        else:
            response = {"message": "Invalid data or registration failed"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
        
#create Patient Sign Up View
class PatientRegisterView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Petient.objects.all()

    def get(self, request:Request, *args, **kwargs):
        form = PatientForm()
        return render(request, 'Patient_signup.html', {'form': form})
    
    def post(self, request:Request,*args,**kwargs):
        form = PatientForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            password = form.data.get('Password')
            confirm_password = form.data.get('Confirm_Password')
        
            if password != confirm_password:
                error_message = "Password and Confirm Password do not match"
                return render(request, 'Patient_signup.html', {'form': form, 'error_message': error_message})
            else:
                patient = form.save()
                message="Registered Successufylly!!!"
                return render(request, 'Patient_signup.html', {'form': form,"message":message})
        else:
            response = {"message": "Invalid data or registration failed"}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

#create Login View for Doctor 
class DoctorLoginView(generics.CreateAPIView):
    serializer_class=LoginDoctorSerializer
    queryset=Doctor.objects.all()
    def get(self, request:Request, *args, **kwargs):
        form = DoctorLoginForm()
        return render(request, 'Doctor_login.html', {'form': form})
    
    def post(self, request:Request,format=None):
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            data=request.data
            email=data.get("email",None)
            password=data.get("password",None)
            user=Doctor.objects.filter(Email_Id=email,Password=password)
            if user:
                message="login succcessfully"
                data_for_user=user
                return render(request,"data_extract.html",{"message":message,"data_for_user":data_for_user})
            else:
                form=DoctorLoginForm()
                message="User Does Not Exist Or Check Email id and Password"
                return render(request,"Doctor_login.html",{"form":form,"message":message})
            
        else: 
            response={
                "message":"Not Valid User Information",
               
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        
#create login view for patient   
class PatientLoginView(generics.CreateAPIView):
    serializer_class=LoginPatientSerializer
    queryset=Petient.objects.all()
    def get(self, request:Request, *args, **kwargs):
        form = PatientLoginForm()
        return render(request, 'Patient_login.html', {'form': form})
    
    def post(self, request:Request,format=None):
        form = PatientLoginForm(request.POST)
        
        if form.is_valid():
            
            data=request.data
            email=data.get("email",None)
            password=data.get("password",None)
            #check wether the data present in the database
            user=Petient.objects.filter(Email_Id=email,Password=password)
            if user:
                message="login succcessfully and user details are!!!"
                data_for_user=user
                return render(request,"data_extract.html",{"message":message,"data_for_user":data_for_user})
            else:
                form=PatientLoginForm(request.POST)
                message="User Does Not Exist Or Check Email id and Password"
                return render(request,"Patient_login.html",{"form":form,"message":message})
        else:
            
            response={
                "message":"Not Valid User Information",
               
            }
            return Response(data=response,status=status.HTTP_400_BAD_REQUEST)
        
    
def register_doctor(request):
    form=DoctorForm()
    return render(request,'selectuser.html')

from django.urls import path
from .views import DoctorRegisterView,PatientRegisterView,DoctorLoginView,PatientLoginView,register_doctor

urlpatterns=[
    path("doctor_register/",DoctorRegisterView.as_view(),name="doctor_register"),
    path("patient_register/",PatientRegisterView.as_view(),name="patient_register"),
    path("doctor_login/",DoctorLoginView.as_view(),name="doctor_login"),
    path("patient_login/",PatientLoginView.as_view(),name="patient_login"),
    path("",register_doctor,name="doc_reg")
]
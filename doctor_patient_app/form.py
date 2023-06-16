from django import forms
from rest_framework import serializers
from .serializer import DoctorSerializer,PatientSerializer,LoginDoctorSerializer,LoginPatientSerializer

class DoctorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = DoctorSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data):

        if isinstance(field_data, serializers.ImageField):
            return forms.ImageField(label=field_data.label)
        elif isinstance(field_data, serializers.IntegerField):
            return forms.IntegerField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.BooleanField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
    
        else:
            return forms.CharField(label=field_data.label)

    

    def save(self):
        data = self.cleaned_data

        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)

class PatientForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = DoctorSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data):

        if isinstance(field_data, serializers.ImageField):
            return forms.ImageField(label=field_data.label)
        elif isinstance(field_data, serializers.IntegerField):
            return forms.IntegerField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.BooleanField(label=field_data.label)
        elif isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
    
        else:
            return forms.CharField(label=field_data.label)

    

    def save(self):
        data = self.cleaned_data

        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)
#create form for Doctor Login  
class DoctorLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = LoginDoctorSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data): 
        if isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
        else:
            return forms.CharField(label=field_data.label)
    def save(self):
        data = self.cleaned_data
        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)
    
#create form for Doctor Login  
class PatientLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer = LoginPatientSerializer()
        self.fields = {
            field_name: self.get_form_field(field_data)
            for field_name, field_data in self.serializer.fields.items()
        }

    def get_form_field(self, field_data): 
        if isinstance(field_data,serializers.BooleanField):
            return forms.EmailField(label=field_data.label)
        else:
            return forms.CharField(label=field_data.label)
    def save(self):
        data = self.cleaned_data
        # Create an instance of the serializer with the form data
        serializer = DoctorSerializer(data=data)

        # Validate the serializer data
        if serializer.is_valid():
            # Save the validated data and return the doctor object
            return serializer.save()

        # If data is not valid, raise an exception or handle the error as desired
        raise forms.ValidationError(serializer.errors)
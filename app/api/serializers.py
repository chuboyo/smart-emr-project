# from dataclasses import fields
# from pyexpat import model 
# just a test comment
from rest_framework import serializers

from main.models import Patient, DoctorAppointmentHistory, LabAppointmentHistory
from users.models import CustomUser

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'hospital_id', 
        'age', 'sex', 'nationality', 'state_of_origin', 'marriage_status', 
        'address', 'religion', 'tribe',)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointmentHistory
        fields = ('id', 'patient', 'date', 'hospital_section', 'presenting_complain', 
        'history_of_presenting_complain', 'past_medical_and_surgical_history', 
        'drugs_and_allergies', 'family_and_social_history', 'other_history', 
        'provisional_diagnosis', 'physical_examination', 'created_by', 
        'lab_appointment', 'next_appointment_date',)

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabAppointmentHistory
        fields = ('id', 'patient', 'date', 'created_by', 
        'report', 'image_report', 'next_appointment_date',)

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username','is_doctor', 'is_lab_staff', 'is_clerical_staff',)
        
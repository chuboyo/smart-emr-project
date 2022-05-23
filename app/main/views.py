from django.shortcuts import render

from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

"""patient table views """
class PatientListView(ListView):
    model = Patient
    context_object_name = 'patient_list'
    template_name = 'patient/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patient/patient_detail.html'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient/new_patient.html'
    fields = '__all__'

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient/edit_patient.html'
    fields = ['first_name', 'last_name', 'middle_name', 'hospital_number',
        'age', 'gender_choices', 'sex', 'nationality', 'state_of_origin',
        'marriage_choices', 'marriage_status', 'address', 'religion', 
        'tribe',
    ]

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/delete_patient.html'
    success_url = reverse_lazy('')


"""doctor appointment history views """
class DoctorAppointmentListView(ListView):
    model = DoctorAppointmentHistory
    context_object_name = 'doctor_appointment_list'
    template_name = 'doctor/doctor_appointment_list.html'

class DoctorAppointmentDetailView(DetailView):
    model = DoctorAppointmentHistory
    context_object_name = 'doctor_appointment'
    template_name = 'doctor/doctor_appointment_detail.html'

class DoctorAppointmentCreateView(CreateView):
    model = DoctorAppointmentHistory
    template_name = 'doctor/new_doctor_appointment.html'
    fields = '__all__'

class DoctorAppointmentUpdateView(UpdateView):
    model = DoctorAppointmentHistory
    template_name = 'doctor/edit_doctor_appointment.html'
    fields = [
        'hospital_section', 'presenting_complain', 'history_of_presenting_complain',
        'past_medical_and_surgical_history', 'drugs_and_allergies', 
        'family_and_social_history', 'other_history', 'provisional_diagnosis',
        'physical_examination', 'lab_appointment', 'next_appointment_date',
    ]

class DoctorAppointmentDeleteView(DeleteView):
    model = DoctorAppointmentHistory
    template_name = 'doctor/delete_doctor_appointment.html'
    success_url = reverse_lazy('')


"""lab report views """
class LabAppointmentListView(ListView):
    model = LabAppointmentHistory
    context_object_name = 'lab_appointment_list'
    template_name = 'lab/lab_appointment_list.html'

class LabAppointmentDetailView(DetailView):
    model = LabAppointmentHistory
    context_object_name = 'lab_appointment'
    template_name = 'lab/lab_appointment_detail.html'

class LabAppointmentCreateView(CreateView):
    model = LabAppointmentHistory
    template_name = 'lab/new_lab_appointment.html'
    fields = '__all__'

class LabAppointmentUpdateView(UpdateView):
    model = LabAppointmentHistory
    template_name = 'lab/edit_lab_appointment.html'
    fields = [
        'report', 'image_report', 'next_appointment_date',
    ]

class LabAppointmentDeleteView(DeleteView):
    model = LabAppointmentHistory
    template_name = 'lab/delete_lab_appointment.html'
    success_url = reverse_lazy('')
# Create your views here.

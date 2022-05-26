from django.shortcuts import render, get_object_or_404

from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from datetime import datetime

from .forms import PatientUpdateForm, CreateDoctorAppointmentHistoryForm, CreateLabAppointmentHistoryForm

"""patient table views """
class PatientListView(ListView):
    model = Patient
    context_object_name = 'patient_list'
    template_name = 'patient/patient_list.html'

class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patient/patient_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.get_object()
        doc_appointments = DoctorAppointmentHistory.objects.filter(patient=patient.pk).all()
        lab_appointments = LabAppointmentHistory.objects.filter(patient=patient.pk).all()
        context.update({'doctor_appointments': doc_appointments, 'lab_appointments':lab_appointments})
        return context

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient/new_patient.html'
    fields = '__all__'

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'patient/edit_patient.html'
    '''fields = ['first_name', 'last_name', 'middle_name', 'hospital_number',
        'age', 'sex', 'nationality', 'state_of_origin', 'marriage_status', 
        'address', 'religion', 'tribe',
    ]'''
    form_class = PatientUpdateForm

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient/delete_patient.html'
    context_object_name = 'patient'
    success_url = reverse_lazy('patient_list')


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
    form_class = CreateDoctorAppointmentHistoryForm

    def dispatch(self, request, *args, **kwargs): # get patient data that you're creating appointment for (via url)
        self.patient = get_object_or_404(Patient, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    # Overriding get_initial method to pre-populate the patient field of our form
    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.patient
        return initial

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
    context_object_name = 'doctor_appointment'
    success_url = reverse_lazy('doctor_list')


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
    form_class = CreateLabAppointmentHistoryForm

    def dispatch(self, request, *args, **kwargs): # get patient data that you're creating appointment for (via url)
        self.patient = get_object_or_404(Patient, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.patient
        return initial


class LabAppointmentUpdateView(UpdateView):
    model = LabAppointmentHistory
    template_name = 'lab/edit_lab_appointment.html'
    fields = [
        'report', 'image_report', 'next_appointment_date',
    ]

class LabAppointmentDeleteView(DeleteView):
    model = LabAppointmentHistory
    template_name = 'lab/delete_lab_appointment.html'
    context_object_name = 'lab_appointment'
    # success_url = reverse_lazy('lab_list')

    def get_success_url(self):
        lab_appointment = self.get_object()
        pk = lab_appointment.patient.id
        return reverse_lazy('patient_detail', kwargs={'pk': pk})

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_patients = Patient.objects.all().count()
        doctor_appointments_today = DoctorAppointmentHistory.objects.filter(date = datetime.today().date()).count()
        context.update({'total_patients': total_patients, 'doctor_appointments_today': doctor_appointments_today})
        return context


class PatientSearchResultsListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patient/patient_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Patient.objects.filter(hospital_number=query)
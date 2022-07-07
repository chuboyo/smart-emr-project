from django.shortcuts import render, get_object_or_404, redirect

from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

from django.views.generic import ListView, DetailView, TemplateView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from datetime import datetime

from .forms import (
                    PatientUpdateForm, CreateDoctorAppointmentHistoryForm, CreateLabAppointmentHistoryForm, CreateLabAppointmentUpdateForm, 
                    PatientCreateForm, CreateDoctorAppointmentUpdateForm
                )

from django.core.files.storage import FileSystemStorage

from django.contrib.auth.mixins import ( 
    LoginRequiredMixin, PermissionRequiredMixin 
)

from datetime import datetime, timedelta


"""patient table views """
class PatientListView(LoginRequiredMixin, ListView):
    #permission_required = 'main.view_patient'
    model = Patient
    context_object_name = 'patient_list'
    template_name = 'patient/patient_list.html'

class PatientDetailView(LoginRequiredMixin, DetailView):
    #permission_required = 'main.view_patient'
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

class PatientCreateView(LoginRequiredMixin, CreateView):
    #permission_required = 'main.add_patient'
    model = Patient
    form_class = PatientCreateForm
    template_name = 'patient/new_patient.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_clerical_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)
    

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    #permission_required = 'main.change_patient'
    model = Patient
    template_name = 'patient/edit_patient.html'
    form_class = PatientUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    #permission_required = 'main.delete_patient'
    model = Patient
    template_name = 'patient/delete_patient.html'
    context_object_name = 'patient'
    success_url = reverse_lazy('patient_list')

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)


"""doctor appointment history views """
class DoctorAppointmentListView(LoginRequiredMixin, ListView):
    #permission_required = 'main.view_doctorappointmenthistory'
    model = DoctorAppointmentHistory
    context_object_name = 'doctor_appointment_list'
    template_name = 'doctor/doctor_appointment_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class DoctorAppointmentDetailView(LoginRequiredMixin, DetailView):
    #permission_required = 'main.view_doctorappointmenthistory'
    model = DoctorAppointmentHistory
    context_object_name = 'doctor_appointment'
    template_name = 'doctor/doctor_appointment_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class DoctorAppointmentCreateView(LoginRequiredMixin, CreateView):
    #permission_required = 'main.add_doctorappointmenthistory'
    model = DoctorAppointmentHistory
    template_name = 'doctor/new_doctor_appointment.html'
    form_class = CreateDoctorAppointmentHistoryForm

    def dispatch(self, request, *args, **kwargs): # get patient data that you're creating appointment for (via url)
        self.patient = get_object_or_404(Patient, pk=kwargs['pk'])
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

    # Overriding get_initial method to pre-populate the patient field of our form
    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.patient
        return initial

    def form_valid(self, form): 
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class DoctorAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    #permission_required = 'main.change_doctorappointmenthistory'
    model = DoctorAppointmentHistory
    template_name = 'doctor/edit_doctor_appointment.html'
    form_class = CreateDoctorAppointmentUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class DoctorAppointmentDeleteView(LoginRequiredMixin, DeleteView):
    #permission_required = 'main.delete_doctorappointmenthistory'
    model = DoctorAppointmentHistory
    template_name = 'doctor/delete_doctor_appointment.html'
    context_object_name = 'doctor_appointment'
    success_url = reverse_lazy('doctor_list')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)


"""lab report views """
class LabAppointmentListView(LoginRequiredMixin, ListView):
    #permission_required = 'main.view_labappointmenthistory'
    model = LabAppointmentHistory
    context_object_name = 'lab_appointment_list'
    template_name = 'lab/lab_appointment_list.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class LabAppointmentDetailView(LoginRequiredMixin, DetailView):
    #permission_required = 'main.view_labappointmenthistory'
    model = LabAppointmentHistory
    context_object_name = 'lab_appointment'
    template_name = 'lab/lab_appointment_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_doctor or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class LabAppointmentCreateView(LoginRequiredMixin, CreateView):
    #permission_required = 'main.add_labappointmenthistory'
    model = LabAppointmentHistory
    template_name = 'lab/new_lab_appointment.html'
    form_class = CreateLabAppointmentHistoryForm

    def model_form_upload(request):
        if request.method == 'POST':
            form = CreateLabAppointmentHistoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('lab_detail')
        else:
            form = CreateLabAppointmentHistoryForm()
        return render(request, 'lab_new', {
            'form': form
        })

    def dispatch(self, request, *args, **kwargs): # get patient data that you're creating appointment for (via url)
        self.patient = get_object_or_404(Patient, pk=kwargs['pk'])
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['patient'] = self.patient
        return initial

    def form_valid(self, form): 
        form.instance.created_by = self.request.user 
        return super().form_valid(form)


class LabAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    #permission_required = 'main.change_labappointmenthistory'
    model = LabAppointmentHistory
    template_name = 'lab/edit_lab_appointment.html'
    form_class = CreateLabAppointmentUpdateForm

    def model_form_upload(request):
        if request.method == 'POST':
            form = CreateLabAppointmentUpdateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('lab_detail')
        else:
            form = CreateLabAppointmentUpdateForm()
        return render(request, 'lab_edit', {
            'form': form
        })

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class LabAppointmentDeleteView(LoginRequiredMixin, DeleteView):
    #permission_required = 'main.delete_labappointmenthistory'
    model = LabAppointmentHistory
    template_name = 'lab/delete_lab_appointment.html'
    context_object_name = 'lab_appointment'
    # success_url = reverse_lazy('lab_list')

    def get_success_url(self):
        lab_appointment = self.get_object()
        pk = lab_appointment.patient.id
        return reverse_lazy('patient_detail', kwargs={'pk': pk})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not (request.user.is_superuser or request.user.is_lab_staff):
                return render(request, template_name='errors/404.html', status=404)
        else:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_patients = Patient.objects.all().count()
        doctor_appointments_today = DoctorAppointmentHistory.objects.filter(date = datetime.today().date()).count()
        context.update({'total_patients': total_patients, 'doctor_appointments_today': doctor_appointments_today})
        return context


class PatientSearchResultsListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patient/patient_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Patient.objects.filter(hospital_id=query)

class AdvancedSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'search.html'

class DoctorAppointmentFilterView(LoginRequiredMixin, ListView):
    model = DoctorAppointmentHistory
    context_object_name = 'doctor_appointments'
    template_name = 'doctor/appointment_search_results.html'

    def get_queryset(self):
        days = self.request.GET.get('range')
        try:
            duration = datetime.today() - timedelta(days=int(days)) # get days difference
            return DoctorAppointmentHistory.objects.filter(date__gte=duration)
        except:
            return DoctorAppointmentHistory.objects.all()

class LabAppointmentFilterView(LoginRequiredMixin, ListView):
    model = LabAppointmentHistory
    context_object_name = 'lab_appointments'
    template_name = 'lab/appointment_search_results.html'

    def get_queryset(self):
        days = self.request.GET.get('range')
        try:
            duration = datetime.today() - timedelta(days=int(days)) # get days difference
            return LabAppointmentHistory.objects.filter(date__gte=duration)
        except:
            return LabAppointmentHistory.objects.all()
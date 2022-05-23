from django.urls import path

from .views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView
from .views import DoctorAppointmentListView, DoctorAppointmentDetailView, DoctorAppointmentCreateView, DoctorAppointmentUpdateView, DoctorAppointmentDeleteView
from .views import LabAppointmentListView, LabAppointmentDetailView, LabAppointmentCreateView, LabAppointmentUpdateView, LabAppointmentDeleteView

urlpatterns = [
    path('patient/', PatientListView.as_view(), name='patient_list'),
    path('patient/<uuid:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/new/', PatientCreateView.as_view(), name='patient_new'),
    path('patient/<uuid:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<uuid:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('doctor/', DoctorAppointmentListView.as_view(), name='doctor_list'),
    path('doctor/<uuid:pk>/', DoctorAppointmentDetailView.as_view(), name='doctor_detail'),
    path('doctor/new/', DoctorAppointmentCreateView.as_view(), name='doctor_new'),
    path('doctor/<uuid:pk>/edit/', DoctorAppointmentUpdateView.as_view(), name='doctor_edit'),
    path('doctor/<uuid:pk>/delete/', DoctorAppointmentDeleteView.as_view(), name='doctor_delete'),
    path('lab/', LabAppointmentListView.as_view(), name='lab_list'),
    path('lab/<uuid:pk>/', LabAppointmentDetailView.as_view(), name='lab_detail'),
    path('lab/new/', LabAppointmentCreateView.as_view(), name='lab_new'),
    path('lab/<uuid:pk>/edit/', LabAppointmentUpdateView.as_view(), name='lab_edit'),
    path('lab/<uuid:pk>/delete/', LabAppointmentDeleteView.as_view(), name='lab_delete'),
]
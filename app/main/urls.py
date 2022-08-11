from django.urls import path

from .views import (PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView,
                    DoctorAppointmentListView, DoctorAppointmentDetailView, DoctorAppointmentCreateView, DoctorAppointmentUpdateView, 
                    DoctorAppointmentDeleteView, LabAppointmentListView, LabAppointmentDetailView, LabAppointmentCreateView, 
                    LabAppointmentUpdateView, LabAppointmentDeleteView, PatientSearchResultsListView, HomePageView, AdvancedSearchView,
                    LabAppointmentFilterView, DoctorAppointmentFilterView)

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patient/<uuid:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('patient/new/', PatientCreateView.as_view(), name='patient_new'),
    path('patient/<uuid:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('patient/<uuid:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('doctor/appointments', DoctorAppointmentListView.as_view(), name='doctor_list'),
    path('doctor/<uuid:pk>/', DoctorAppointmentDetailView.as_view(), name='doctor_detail'),
    path('doctor/<uuid:pk>/new/', DoctorAppointmentCreateView.as_view(), name='doctor_new'),
    path('doctor/<uuid:pk>/edit/', DoctorAppointmentUpdateView.as_view(), name='doctor_edit'),
    path('doctor/<uuid:pk>/delete/', DoctorAppointmentDeleteView.as_view(), name='doctor_delete'),
    path('lab/appointments', LabAppointmentListView.as_view(), name='lab_list'),
    path('lab/<uuid:pk>/', LabAppointmentDetailView.as_view(), name='lab_detail'),
    path('lab/<uuid:pk>/new/', LabAppointmentCreateView.as_view(), name='lab_new'),
    path('lab/<uuid:pk>/edit/', LabAppointmentUpdateView.as_view(), name='lab_edit'),
    path('lab/<uuid:pk>/delete/', LabAppointmentDeleteView.as_view(), name='lab_delete'),

    path('patient_search/', PatientSearchResultsListView.as_view(), name='patient_search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('advanced_search/', AdvancedSearchView.as_view(), name='advanced_search'),
    path('doctor_search/', DoctorAppointmentFilterView.as_view(), name='doctor_search'),
    path('lab_search/',LabAppointmentFilterView.as_view(), name='lab_search')
]
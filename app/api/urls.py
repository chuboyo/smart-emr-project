from django.urls import path

from .views import PatientList, PatientCreate,PatientDetail, DoctorList, DoctorCreate, DoctorDetail, LabList, LabCreate, LabDetail, UserList, UserDetail

urlpatterns = [
    path('patients/', PatientList.as_view()),
    path('patients/new/', PatientCreate.as_view()),
    path('patient/<uuid:pk>/', PatientDetail.as_view()),
    path('doctors/', DoctorList.as_view()),
    path('doctors/new/', DoctorCreate.as_view()),
    path('doctors/<uuid:pk>', DoctorDetail.as_view()),
    path('lab/', LabList.as_view()),
    path('lab/new/', LabCreate.as_view()),
    path('lab/<uuid:pk>', LabDetail.as_view()),
    path('users/', UserList.as_view()),
    path('user/<uuid:pk>', UserDetail.as_view()),
]
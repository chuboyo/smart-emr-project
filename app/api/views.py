# from django.shortcuts import render

# # Create your views here.
from django.http import Http404

from rest_framework import generics


from main.models import Patient, DoctorAppointmentHistory, LabAppointmentHistory
from users.models import CustomUser

from .serializers import PatientSerializer, DoctorSerializer, LabSerializer, CustomUserSerializer

class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientCreate(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class DoctorList(generics.ListAPIView):
    queryset = DoctorAppointmentHistory.objects.all()
    serializer_class = DoctorSerializer

class DoctorCreate(generics.CreateAPIView):
    queryset = DoctorAppointmentHistory.objects.all()
    serializer_class = DoctorSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_doctor):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorAppointmentHistory.objects.all()
    serializer_class = DoctorSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_doctor):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class LabList(generics.ListAPIView):
    queryset = LabAppointmentHistory.objects.all()
    serializer_class = LabSerializer

class LabCreate(generics.CreateAPIView):
    queryset = LabAppointmentHistory.objects.all()
    serializer_class = LabSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_lab_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class LabDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LabAppointmentHistory.objects.all()
    serializer_class = LabSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_lab_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or request.user.is_clerical_staff):
            raise Http404
        return super().dispatch(request, *args, **kwargs)


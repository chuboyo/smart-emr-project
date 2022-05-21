from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

class LabInline(admin.TabularInline):
    model = LabAppointmentHistory
    extra = 0

class DoctorInline(admin.TabularInline):
    model = DoctorAppointmentHistory
    extra = 0

class PatientAdmin(admin.ModelAdmin):
    inlines = [DoctorInline, LabInline]


admin.site.register(Patient, PatientAdmin)
admin.site.register(DoctorAppointmentHistory)
admin.site.register(LabAppointmentHistory)


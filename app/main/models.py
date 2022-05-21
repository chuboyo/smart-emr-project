from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Patient(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=True, default='')
    hospital_number = models.IntegerField(unique=True, default=0)

    age = models.IntegerField(blank=False)

    # The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name.
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    sex = models.CharField(max_length=6, choices=gender_choices, default='female')
    # state of origin wasn't populated with choices because it'd be too long, the form would be customized instead
    # this thread might be useful: https://stackoverflow.com/questions/66302329/how-to-create-dropdown-box-with-forms-modelform-in-django
    nationality = models.CharField(max_length=50, blank=False)
    state_of_origin = models.CharField(max_length=50, blank=False)
    marriage_choices = [
        ('married', 'Married'),
        ('single', 'Single')
    ]
    marriage_status = models.CharField(max_length=10, choices=marriage_choices, default='single')
    address = models.CharField(max_length=300, blank=False)
    religion = models.CharField(max_length=50, blank=False)
    tribe =  models.CharField(max_length=50, blank=False)
    

    def __str__(self):
        return f' {self.hospital_number} --> {self.first_name}  {self.last_name}'

class DoctorAppointmentHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    hospital_section = models.CharField(max_length=50, blank=False)

    # appointment report section (a fieldset and legend can be used in the form)
    presenting_complain = models.TextField(default='')
    history_of_presenting_complain = models.TextField(default='')
    past_medical_and_surgical_history = models.TextField(default='')
    drugs_and_allergies = models.TextField(default='')
    family_and_social_history = models.TextField(default='')
    other_history = models.TextField(default='')
    provisional_diagnosis = models.TextField(default='')
    physical_examination = models.TextField(default='')
    # end of appointment report section

    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lab_appointment = models.TextField(default='None')
    next_appointment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.patient} --> {self.date}'

    class Meta:
        ordering = ['-date']


class LabAppointmentHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    report = models.TextField(blank=False)
    image_report = models.FileField(blank=True)
    next_appointment_date = models.DateField(blank=True, null=True)

    def __str__(self):
            return f'{self.patient} --> {self.date}'
    
    class Meta:
        ordering = ['-date']

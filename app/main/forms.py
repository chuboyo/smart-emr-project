from django import forms

from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

class PatientUpdateForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        gender_choices = [
            ('male', 'Male'),
            ('female', 'Female')
        ]

        marriage_choices = [
            ('married', 'Married'),
            ('single', 'Single')
        ]
        self.fields['marriage_status'] = forms.ChoiceField(choices=marriage_choices)

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'middle_name', 'hospital_number',
        'age', 'sex', 'nationality', 'state_of_origin', 'marriage_status', 
        'address', 'religion', 'tribe',
    ]

class CreateDoctorAppointmentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = DoctorAppointmentHistory
        fields = [
            'patient', 'hospital_section', 'presenting_complain', 'history_of_presenting_complain',
            'past_medical_and_surgical_history', 'drugs_and_allergies', 'family_and_social_history',
            'other_history', 'provisional_diagnosis', 'physical_examination', 'lab_appointment', 
            'next_appointment_date',
        ]

class CreateLabAppointmentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LabAppointmentHistory
        fields = [
            'patient', 'report', 'image_report', 'next_appointment_date',
        ]
class CreateLabAppointmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LabAppointmentHistory
        fields = [
            'report', 'image_report', 'next_appointment_date',
        ]
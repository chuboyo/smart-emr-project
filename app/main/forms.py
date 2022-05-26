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
        self.fields['gender'] = forms.ChoiceField(choices=gender_choices)
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
        fields = '__all__'

class CreateLabAppointmentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = LabAppointmentHistory
        fields = '__all__'
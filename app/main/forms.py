from django import forms

from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory

from secrets import token_hex

from datetime import date


class PatientCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PatientCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your first name'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter other names'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your last name'})
        self.fields['age'].widget.attrs.update({'class': 'form-control', 'placeholder': 'How old are you?'})
        self.fields['sex'].widget.attrs.update({'class': 'form-select' })
        self.fields['nationality'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What country are you from?'})
        self.fields['state_of_origin'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What state are you from?'})
        self.fields['tribe'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What tribe are you?'})
        self.fields['marriage_status'].widget.attrs.update({'class': 'form-select' })
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your current living address'})
        self.fields['religion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tell us your religion'})        

    def clean_hospital_id(self):
        last_name = self.cleaned_data['last_name']
        token = token_hex(2)
        today = date.today()
        hospital_id = f'{last_name}/0{today.month}{str(today.year)[2:]}/{token}'
        return hospital_id

    class Meta:
        model = Patient
        fields = '__all__'

class PatientUpdateForm(forms.ModelForm):
    def __init__(self,  *args, **kwargs):
        super(PatientUpdateForm, self).__init__(*args, **kwargs)
        marriage_choices = [
            ('married', 'Married'),
            ('single', 'Single')
        ]
        self.fields['marriage_status'] = forms.ChoiceField(choices=marriage_choices)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your first name'})
        self.fields['middle_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter other names'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your last name'})
        self.fields['age'].widget.attrs.update({'class': 'form-control', 'placeholder': 'How old are you?'})
        self.fields['sex'].widget.attrs.update({'class': 'form-select' })
        self.fields['nationality'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What country are you from?'})
        self.fields['state_of_origin'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What state are you from?'})
        self.fields['tribe'].widget.attrs.update({'class': 'form-control', 'placeholder': 'What tribe are you?'})
        self.fields['marriage_status'].widget.attrs.update({'class': 'form-select' })
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your current living address'})
        self.fields['religion'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Tell us your religion'}) 
    
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'middle_name',
            'age', 'sex', 'nationality', 'state_of_origin', 'marriage_status', 
            'address', 'religion', 'tribe',
        ]

class CreateDoctorAppointmentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'rows': 5})

    class Meta:
        model = DoctorAppointmentHistory
        fields = [
            'patient', 'hospital_section', 'presenting_complain', 'history_of_presenting_complain',
            'past_medical_and_surgical_history', 'drugs_and_allergies', 'family_and_social_history',
            'other_history', 'provisional_diagnosis', 'physical_examination', 'lab_appointment', 
            'next_appointment_date',
        ]

class CreateDoctorAppointmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control', 'rows': 5})

    class Meta:
        model = DoctorAppointmentHistory
        fields = [
            'hospital_section', 'presenting_complain', 'history_of_presenting_complain',
            'past_medical_and_surgical_history', 'drugs_and_allergies', 'family_and_social_history',
            'other_history', 'provisional_diagnosis', 'physical_examination', 'lab_appointment', 
            'next_appointment_date',
        ]


class CreateLabAppointmentHistoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = LabAppointmentHistory
        fields = [
            'patient', 'report', 'image_report', 'next_appointment_date',
        ]
class CreateLabAppointmentUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = LabAppointmentHistory
        fields = [
            'report', 'image_report', 'next_appointment_date',
        ]
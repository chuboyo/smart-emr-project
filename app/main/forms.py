from django import forms

from .models import Patient


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
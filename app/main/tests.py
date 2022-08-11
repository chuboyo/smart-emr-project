from urllib import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Patient, DoctorAppointmentHistory, LabAppointmentHistory
from django.urls import reverse, resolve
from datetime import datetime

# Create your tests here.
# Tests:
# Create Patient, Doctor Appointment and Lab Appointment
#  Check status codes, template used, form used, view function name,
# check detail view, list view, model string representations, create view, delete view

class PatientsTest(TestCase):
    def setUp(self):
        self.patient = Patient.objects.create(
            first_name='John',
            last_name = 'doe',
            hospital_number = 1,
            age=24,
            sex = 'male',
            nationality='Nigerian',
            state_of_origin='Kogi',
            marriage_status='single',
            address='Lugbe, Abuja',
            religion="Muslim",
            tribe='Ebira'
        )

        self.user = get_user_model().objects.create_user(
             email='badman@gmail.com',
             username='badman',
             password='password'
        )

        self.superuser = get_user_model().objects.create_user(
             email='genuis@gmail.com',
             username='supergenius',
             password='password',
             is_superuser = True
        )

    def test_string_representation(self):
        self.assertEqual(str(self.patient), f' {self.patient.hospital_number} --> {self.patient.first_name}  {self.patient.last_name}')

    def test_absolute_url(self):
        self.assertEqual(self.patient.get_absolute_url(), f'/patient/{self.patient.id}/')

    def test_patient_create_view(self):
        data = {
            'first_name':'John',
            'last_name' : 'doe',
            'middle_name': 'Lakh',
            'hospital_number' : 2,
            'age':24,
            'sex' :'male',
            'nationality':'Nigerian',
            'state_of_origin':'Kogi',
            'marriage_status': 'single',
            'address': 'Lugbe, Abuja',
            'religion':"Muslim",
            'tribe':'Ebira'}
        self.client.login(username=self.user.username, password='password')
        response =  self.client.post(reverse('patient_new'), data)
        self.assertEqual(response.status_code, 403) # forbidden for regular users
        self.client.logout()

        self.client.login(username=self.superuser.username, password='password')
        response =  self.client.post(reverse('patient_new'),  data)
        self.assertEqual(response.status_code, 302) 
        self.assertEqual(Patient.objects.last().last_name, 'doe')
        self.assertEqual(Patient.objects.last().age, 24)
        self.client.logout()

    def test_patient_update_view(self):
        data = {
            'first_name':'Joe',
            'last_name': 'Doe',
            'middle_name': 'Phineas',
            'hospital_number': 2,
            'age': 24,
            'sex' : 'female',
            'nationality':'Nigerian',
            'state_of_origin':'Kogi',
            'marriage_status': 'single',
            'address': 'Lugbe, Abuja',
            'religion':"Muslim",
            'tribe':'Ebira'}
        
        new_patient = Patient.objects.create(
            first_name='John',
            last_name = 'doe',
            middle_name = 'Phineas',
            hospital_number = 2,
            age=24,
            sex = 'male',
            nationality='Nigerian',
            state_of_origin='Kogi',
            marriage_status='single',
            address='Lugbe, Abuja',
            religion="Muslim",
            tribe='Ebira'
        )

        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('patient_edit', kwargs={'pk': new_patient.id}), data)
        self.assertEqual(response.status_code, 302) 
        new_patient.refresh_from_db()
        self.assertEqual(new_patient.first_name, 'Joe')
        self.assertEqual(new_patient.sex, 'female')
        self.client.logout()

    def test_patient_list_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('patient_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'patient/patient_list.html')
        self.assertContains(response, self.patient.first_name)
        self.client.logout()

    def test_patient_detail_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('patient_detail', args=[self.patient.id]))
        self.assertTemplateUsed(response, 'patient/patient_detail.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.patient.first_name)
        self.client.logout()

    def test_patient_delete_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('patient_delete', args=[self.patient.id]))
        self.assertEqual(response.status_code, 302)
        self.client.logout()


class DoctorAppointmentTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
             email='badman@gmail.com',
             username='badman',
             password='password'
        )

        self.superuser = get_user_model().objects.create_user(
             email='genuis@gmail.com',
             username='supergenius',
             password='password',
             is_superuser = True
        )

        self.patient = Patient.objects.create(
            first_name='John',
            last_name = 'doe',
            hospital_number = 1,
            age=24,
            sex = 'male',
            nationality='Nigerian',
            state_of_origin='Kogi',
            marriage_status='single',
            address='Lugbe, Abuja',
            religion="Muslim",
            tribe='Ebira'
        )

        self.history = DoctorAppointmentHistory.objects.create(
            patient = self.patient,
            hospital_section = 'General Medicine',
            created_by = self.superuser
            # other fields left to default value => ''
        )

    def test_string_representation(self):
        self.assertEqual(str(self.history), f'{self.patient} --> {self.history.date}')

    def test_absolute_url(self):
        self.assertEqual(self.history.get_absolute_url(), f'/patient/{self.patient.id}/')

    def test_appointment_history_create_view(self):
        data = {
            'patient': self.patient.id,
            'hospital_section': 'Surgery',
            'presenting_complain': 'a',
            'history_of_presenting_complain': 'b',
            'past_medical_and_surgical_history': 'c',
            'drugs_and_allergies': 'd',
            'family_and_social_history': 'e',
            'other_history': 'f',
            'provisional_diagnosis': 'g',
            'physical_examination': 'h',
            'created_by': self.superuser.id,
            'lab_appointment': 'None',
            'next_appointment_date': '2023-01-01'
            }
        self.client.login(username=self.user.username, password='password')
        response =  self.client.post(reverse('doctor_new', args=[self.patient.id]), data)
        self.assertEqual(response.status_code, 403) # forbidden for regular users
        self.client.logout()

        self.client.login(username=self.superuser.username, password='password')
        response =  self.client.post(reverse('doctor_new', args=[self.patient.id]),  data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(DoctorAppointmentHistory.objects.filter(hospital_section='Surgery').exists())
        self.client.logout()

    def test_appointment_history_update_view(self):
        data = {
            'patient': self.patient.id,
            'hospital_section': 'General Medicine',
            'presenting_complain': 'a',
            'history_of_presenting_complain': 'b',
            'past_medical_and_surgical_history': 'c',
            'drugs_and_allergies': 'd',
            'family_and_social_history': 'e',
            'other_history': 'f',
            'provisional_diagnosis': 'g',
            'physical_examination': 'h',
            'created_by': self.superuser.id,
            'lab_appointment': 'None',
            'next_appointment_date': '2023-01-01'
            }
        
        new_history = DoctorAppointmentHistory.objects.create(
            patient = self.patient,
            hospital_section = 'Surgery',
            created_by = self.superuser
            # other fields left to default value => ''
        )

        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('doctor_edit', kwargs={'pk': new_history.id}), data)
        self.assertEqual(response.status_code, 302) 
        new_history.refresh_from_db()
        self.assertEqual(new_history.hospital_section, 'General Medicine')
        self.client.logout()

    def test_appointment_list_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('doctor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'doctor/doctor_appointment_list.html')
        self.assertContains(response, self.history.hospital_section)
        self.client.logout()

    def test_appointment_detail_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('doctor_detail', args=[self.history.id]))
        self.assertTemplateUsed(response, 'doctor/doctor_appointment_detail.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.history.hospital_section)
        self.assertContains(response, self.patient.first_name)
        self.client.logout()

    def test_appointment_delete_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('doctor_delete', args=[self.history.id]))
        self.assertEqual(response.status_code, 302)
        self.client.logout()

class LabAppointmentTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
             email='badman@gmail.com',
             username='badman',
             password='password'
        )

        self.superuser = get_user_model().objects.create_user(
             email='genuis@gmail.com',
             username='supergenius',
             password='password',
             is_superuser = True
        )

        self.patient = Patient.objects.create(
            first_name='John',
            last_name = 'doe',
            hospital_number = 1,
            age=24,
            sex = 'male',
            nationality='Nigerian',
            state_of_origin='Kogi',
            marriage_status='single',
            address='Lugbe, Abuja',
            religion="Muslim",
            tribe='Ebira'
        )

        self.history = LabAppointmentHistory.objects.create(
            patient = self.patient,
            report = 'None',
            created_by = self.superuser
            # other fields left to default value => ''
        )

    def test_string_representation(self):
        self.assertEqual(str(self.history), f'{self.patient} --> {self.history.date}')

    def test_absolute_url(self):
        self.assertEqual(self.history.get_absolute_url(), f'/patient/{self.patient.id}/')

    def test_appointment_history_create_view(self):
        data = {
            'patient': self.patient.id,
            'created_by': self.superuser.id,
            'report': 'good',
            'image_report': '',
            'next_appointment_date': '2023-01-01'
            }
        self.client.login(username=self.user.username, password='password')
        response =  self.client.post(reverse('lab_new', args=[self.patient.id]), data)
        self.assertEqual(response.status_code, 403) # forbidden for regular users
        self.client.logout()

        self.client.login(username=self.superuser.username, password='password')
        response =  self.client.post(reverse('lab_new', args=[self.patient.id]),  data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(LabAppointmentHistory.objects.filter(report='good').exists())
        self.client.logout()

    def test_appointment_history_update_view(self):
        data = {
            'patient': self.patient.id,
            'created_by': self.superuser.id,
            'report': 'good',
            'image_report': '',
            'next_appointment_date': '2023-01-01'
            }
        
        new_history = LabAppointmentHistory.objects.create(
            patient = self.patient,
            report = 'None',
            created_by = self.superuser
            # other fields left to default value => ''
        )

        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('lab_edit', kwargs={'pk': new_history.id}), data)
        self.assertEqual(response.status_code, 302) # should go through for superusers, response code should be 302 but returns 200
        new_history.refresh_from_db()
        self.assertEqual(new_history.report, 'good')
        self.client.logout()

    def test_appointment_list_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('lab_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lab/lab_appointment_list.html')
        # self.assertContains(response, self.history.date)
        self.client.logout()

    def test_appointment_detail_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('lab_detail', args=[self.history.id]))
        self.assertTemplateUsed(response, 'lab/lab_appointment_detail.html')
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, self.history.date)
        self.assertContains(response, self.patient.first_name)
        self.client.logout()

    def test_appointment_delete_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.post(reverse('lab_delete', args=[self.history.id]))
        self.assertEqual(response.status_code, 302)
        self.client.logout()

class HomePageTest(TestCase):
    def setUp(self):
        self.url = reverse('home')
        self.total_patients = Patient.objects.all().count()
        self.doctor_appointments_today = DoctorAppointmentHistory.objects.filter(date = datetime.today().date()).count()

    def test_homepage_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, f'{self.total_patients} patients')
        self.assertContains(response, f'{self.doctor_appointments_today} appointments as of today')

class SearchResultTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
             email='badman@gmail.com',
             username='badman',
             password='password'
        )

        self.superuser = get_user_model().objects.create_user(
             email='genuis@gmail.com',
             username='supergenius',
             password='password',
             is_superuser = True
        )

        self.patient = Patient.objects.create(
            first_name='John',
            last_name = 'doe',
            hospital_number = 1,
            age=24,
            sex = 'male',
            nationality='Nigerian',
            state_of_origin='Kogi',
            marriage_status='single',
            address='Lugbe, Abuja',
            religion="Muslim",
            tribe='Ebira'
        )

        self.lab_history = LabAppointmentHistory.objects.create(
            patient = self.patient,
            report = 'None',
            created_by = self.superuser
            # other fields left to default value => ''
        )

        self.doctor_history = DoctorAppointmentHistory.objects.create(
            patient = self.patient,
            hospital_section = 'General Medicine',
            created_by = self.superuser
            # other fields left to default value => ''
        )


    def test_advanced_search_view(self):
        response = self.client.get(reverse('advanced_search'))
        self.assertEqual(response.status_code, 302)

        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('advanced_search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.client.logout()

    def test_patient_search_result(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('patient_search_results'), {'q': 1})
        self.assertTemplateUsed(response, 'patient/patient_search_results.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.patient.first_name)
        self.client.logout()

    def test_doctor_filter_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('doctor_search'), {'range': 30})
        self.assertTemplateUsed(response, 'doctor/appointment_search_results.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.doctor_history.hospital_section)
        self.client.logout()

    def test_lab_filter_view(self):
        self.client.login(username=self.superuser.username, password='password')
        response = self.client.get(reverse('lab_search'), {'range': 30})
        self.assertTemplateUsed(response, 'lab/appointment_search_results.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lab_history.created_by)
        self.client.logout()
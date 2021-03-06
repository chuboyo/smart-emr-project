# Generated by Django 4.0.4 on 2022-05-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='drugs_and_allergies',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='family_and_social_history',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='history_of_presenting_complain',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='other_history',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='past_medical_and_surgical_history',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='physical_examination',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='presenting_complain',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='doctorappointmenthistory',
            name='provisional_diagnosis',
            field=models.TextField(blank=True, default=''),
        ),
    ]

# Generated by Django 4.0.4 on 2022-06-06 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_patient_hospital_number_patient_hospital_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='hospital_id',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]

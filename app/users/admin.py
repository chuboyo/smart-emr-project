""" Register the new customuser and custom user forms in the django admin"""
from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import  CustomUserCreationForm, CustomUserChangeForm

class customUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email', 'username',]

admin.site.register(get_user_model(), customUserAdmin)

# Register your models here.

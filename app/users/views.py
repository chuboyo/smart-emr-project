from django.shortcuts import render

from django.contrib.auth import get_user_model

from django.views.generic import DetailView

from django.views.generic.edit import UpdateView


class UserDetailView(DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'user/user_detail.html'


class UserUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'user/edit_user.html'
    fields = '__all__'
# Create your views here.

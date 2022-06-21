from django.shortcuts import render

from django.urls import reverse_lazy

from django.contrib.auth import get_user_model

from django.views.generic import DetailView, CreateView

from django.views.generic.edit import UpdateView, DeleteView

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import CustomUser

from django.contrib.auth.mixins import ( LoginRequiredMixin)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'account/user_detail.html'
    pk_url_kwarg = 'pk'


class UserCreateView(LoginRequiredMixin, CreateView):
    model = get_user_model()
    template_name = 'account/new_user.html'
    form_class = CustomUserCreationForm
    # success_url = reverse_lazy('account_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, template_name='errors/404.html', status=404)
        return super().dispatch(request, *args, **kwargs)
    

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'account/edit_user.html'
    form_class = CustomUserChangeForm

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = get_user_model()
    template_name = 'account/delete_user.html'
    success_url = reverse_lazy('home')
    context_object_name = 'user'

# Create your views here.

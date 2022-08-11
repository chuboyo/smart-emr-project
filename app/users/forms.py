from django.contrib.auth import get_user_model #get current user model i.e
                                               # customUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #get usercreation and userchangeforms

from allauth.account.forms import LoginForm, ResetPasswordForm, ChangePasswordForm


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your first name', 'required':'required'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your last name', 'required':'required'})
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your username', 'required':'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter email address', 'required':'required'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Confirm password'})
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'is_doctor', 'is_lab_staff', 'is_clerical_staff',)

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name')

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'form-input'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-input'
        })

class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
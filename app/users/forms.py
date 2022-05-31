from django.contrib.auth import get_user_model #get current user model i.e
                                               # customUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #get usercreation and userchangeforms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'is_doctor', 'is_lab_staff', 'is_clerical_staff',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
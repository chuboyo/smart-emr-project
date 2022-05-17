from django.contrib.auth import get_user_model #get current user model i.e
                                               # customUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #get usercreation and userchangeforms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserAccountRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')

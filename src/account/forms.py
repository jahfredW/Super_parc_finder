from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUSer

class CustomSignupForm(UserCreationForm):
    class Meta:
        model = CustomUSer
        fields = ('nom', 'email',)
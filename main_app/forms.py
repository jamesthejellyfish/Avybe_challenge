from django.forms import ModelForm, Textarea, PasswordInput
from main_app.models import Image
from django.contrib.auth.models import User


class UploadImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'description', 'image_file']
        widgets = {
            'description': Textarea(attrs={'cols': 30, 'rows': 4}),
        }


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput(),
        }

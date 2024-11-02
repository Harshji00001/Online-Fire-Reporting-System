
from .models import Contact
from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    # Add any additional fields you want in your signup form
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"


class LoginForm(AuthenticationForm):
    pass


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'address']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.Textarea(attrs={'class': 'form-control'}), }
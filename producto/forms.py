from django import forms
import re
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField( label='Mensaje')

def error_mail_contacto(self):
    email = self.cleaned_data.get('customer_email')
    if email:
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, email):
            raise forms.ValidationError('Ingrese un correo electrónico válido.')
    return email

def sintexto(self):
    message = self.cleaned_data.get('message')
    if not message:
        raise forms.ValidationError('Este campo no puede estar vacío.')
    return message

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_name', 'customer_email', 'message']  
        labels = {
            'customer_name': 'Nombre',
            'customer_email': 'Correo',
            'message': 'Mensaje',
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nombre',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Confirme su contraseña'
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
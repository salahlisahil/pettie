from django import forms
from django.core.exceptions import ValidationError

from .models import Pettie


class PettieSignUpForm(forms.ModelForm):
    class Meta:
        model = Pettie
        fields = ('email', 'password', )
        widgets = {
            'password': forms.PasswordInput(),
        }

    def save(self, commit=True):
        pettie = super().save(commit=False)
        pettie.set_password(self.cleaned_data['password'])
        if commit:
            pettie.save()
        return pettie

    def clean_email(self):
        email = self.cleaned_data['email']

        exist_user = Pettie.objects.filter(email=email).first()
        if exist_user:
            raise ValidationError("User with this email is already exists")

        return email

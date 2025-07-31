from django import forms

from . import css
from .models import Email, EmailVerficationEvent


class EmailForm(forms.ModelForm):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "id":"email-login-input",
                "class":css.EMAIL_FIELD_CSS,
                "placeholder":"Your email!"
            }
        )

    )

    class Meta:
        model = EmailVerficationEvent
        fields = ['email']
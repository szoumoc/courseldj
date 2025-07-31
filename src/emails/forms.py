from django import forms

from . import css
from .models import Email, EmailVerficationEvent


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "id":"email-login-input",
                "class":css.EMAIL_FIELD_CSS,
                "placeholder":"Your email!"
            }
        )

    )

    # class Meta:
    #     model = EmailVerficationEvent
    #     fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Email.objects.filter(email=email,
                                  active = False)
        if qs.exists():
            raise forms.ValidationError("Inactive email!")
        
        return email
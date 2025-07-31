from django.contrib import admin

# Register your models here.
from .models import EmailVerficationEvent, Email

admin.site.register(Email)
admin.site.register(EmailVerficationEvent)
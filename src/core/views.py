from django.shortcuts import render
from emails.forms import EmailForm
from emails.models import Email, EmailVerficationEvent
from emails import services as email_services




def home_view(request, *args, **kwargs):
    template_name = "home.html"
    # Request POST data

    form = EmailForm(request.POST or None)
    context = {
        "form": form,
        "message": ""
    }
    if form.is_valid():
        email_val = form.cleaned_data.get('email')
        obj = email_services.start_verification_event(email_val)
        
        print(obj)
        context['form'] = EmailForm()
        context['message'] = "Success! check you email for verification."
    else:
        print(form.errors)
    return render(request, template_name, context) 
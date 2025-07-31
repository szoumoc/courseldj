from django.shortcuts import render
from emails.forms import EmailForm
from emails.models import Email

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
        obj = form.save()
        email_obj, created = Email.objects.get_or_create(email=email_val)
        print(obj)
        context['form'] = EmailForm()
        context['message'] = "Success! check you email for verification."
    else:
        print(form.errors)
    return render(request, template_name, context) 
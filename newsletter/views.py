from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'example_fluid.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = 'site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = from_email
        contact_message = '''%s: %s via %s''' % (
            form_full_name, form_message, form_email)

        send_mail(subject, contact_message, from_email, [to_email],
                  fail_silently=False)

    context = {
        'form': form,
    }

    return render(request, 'forms.html', context)

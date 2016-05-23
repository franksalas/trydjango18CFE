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

    if request.user.is_authenticated() and request.user.is_staff:
        context = {
            'queryset': [123,456]
        }

    return render(request, 'home.html', context)


def contact(request):
    title='Contact Us'
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
        'title': title,
    }

    return render(request, 'forms.html', context)

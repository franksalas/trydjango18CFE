from django.shortcuts import render
from.forms import SignUpForm, ContactForm


def home(request):
    title = 'Welcome'
    form = SignUpForm( request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'home.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')


    context = {
        'form': form,
    }

    return render(request, 'forms.html', context)










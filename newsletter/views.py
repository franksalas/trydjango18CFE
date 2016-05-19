from django.shortcuts import render
from.forms import SignUpForm


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

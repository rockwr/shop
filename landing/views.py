from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = "Bulat"
    current_day = "24.01.2019"
    form = SubscriberForm(request.POST or None)   #request.POST or None - это стандартно, то, что нужно написать в форме

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())

# Create your views here.

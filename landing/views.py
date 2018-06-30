from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):

     # creator = 'Oleksandr'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.changed_data)
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
    #locals return varrible


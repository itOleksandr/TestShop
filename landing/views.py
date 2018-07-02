from django.shortcuts import render
from .forms import SubscriberForm
from product.models import *


def landing(request):
     # creator = 'Oleksandr'
    form = SubscriberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.changed_data)
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())
    #locals return varrible


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_laptops = products_images.filter(product__category_id=1)
    products_images_phones = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals())
    # locals return varrible
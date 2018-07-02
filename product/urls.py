from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from product import views

urlpatterns = [
    url(r'product/(?P<product_id>\w+)/$', views.product, name='product')
    # url(r'^$', views.landing, name='landing')
]

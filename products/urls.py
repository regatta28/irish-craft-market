from django.conf.urls import url, include 
from .views import all_products, productdetails, new_product, edit_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<id>\d+)/$', productdetails, name='productdetails'),
    url(r'^new/$', new_product, name='new_product'),
    url(r'^(?P<id>\d+)/edit$', edit_product, name='edit_product'),
]
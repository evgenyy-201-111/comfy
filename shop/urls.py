from django.urls import re_path as url
from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
]
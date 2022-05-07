from django.shortcuts import render
from django.views import generic

from shop.models import Product, Section


def index(request):
    sections = Section.objects.all().order_by('title')
    products = Product.objects.all()[:16]
    context = {'sections': sections, 'products': products}
    return render(
        request,
        'index.html',
        context=context
    )


class ProductDetailView(generic.DetailView):
    model = Product

from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User, Group
from shop.models import Product, Section
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def index(request):
    sections = Section.objects.all().order_by('title')
    products = Product.objects.all()[:16]
    context = {'sections': sections, 'products': products}
    return render(
        request,
        'index.html',
        context=context
    )


def login(request):
    return render(
        request,
        'login.html',
        context={'login': login}
    )


def registration(request):
    return render(
        request,
        'registration.html',
        context={'registration': registration}
    )


class ProductDetailView(generic.DetailView):
    model = Product


# def add_user(name, email):
#     if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
#         return
#     password = User.objects.make_random_password()
#     user = User.objects.create_user(email, email, password)
#     user.first_name = name
#     group = Group.objects.get(name='Клиенты')
#     user.groups.add(group)
#     user.save
#
#     text = get_template('registration/registration_email.html')
#     html = get_template('registration/registration_email.html')
#
#     context = {'username': email, 'password': password}
#
#     subject = 'Регистрация'
#     from_email = 'from@supeco.ru'
#     text_content = text.render(context)
#     html_content = html.render(context)
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()

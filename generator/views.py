from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generators/home.html')

def about(request):
    return render(request, 'generators/about.html')


def password(request):
    # получение данных из формы (имя, по умолчанию)
    length = int(request.GET.get('leng', 12))
    characters = list('abcdefghijklmopqrstuvwxyz')
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        characters.extend(list('0123456789'))


    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generators/password.html', {'password': thepassword})

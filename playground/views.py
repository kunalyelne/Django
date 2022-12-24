from django.shortcuts import render
from django.http import HttpResponse


def calculate():
    x = 2
    y = 3
    return x + y

def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', {'name': 'Kunal'})
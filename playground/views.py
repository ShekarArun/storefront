from django.shortcuts import render
from django.http import HttpResponse


def dummy():
    x = 1
    y = 2
    return x + y


def say_hello(request):
    # return HttpResponse('Hello World!')
    res = dummy()
    return render(request, 'hello.html', {'name': 'Arun', 'res': res})

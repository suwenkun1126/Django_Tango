from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={'boldmessage':'Hello world'}
    return render(request,'rango/index.html',context=context)

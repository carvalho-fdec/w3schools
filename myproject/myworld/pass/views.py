from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def passcheck(request):
    template = loader.get_template('passcheck.html')
    return HttpResponse(template.render())




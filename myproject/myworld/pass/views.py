from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect

@cache_page(60 * 15)
@csrf_protect

# Create your views here.

def passcheck(request):
    template = loader.get_template('passcheck.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())

def logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == "admin" and password == "admin":
        template = loader.get_template('correct.html')
        return HttpResponse(template.render())

        #return HttpResponseRedirect(reverse('index'))
        #return HttpResponse("correct")
    else:
        #return HttpResponseRedirect(reverse('passcheck'))
        return HttpResponse("incorrect")


#def adduser(request):

from re import template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the myworld index.")
    #return render(request, 'myworld/index.html')
    #template = loader.get_template('myfirst.html')
    #return HttpResponse(template.render())
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = { 'mymembers': mymembers}
    return HttpResponse(template.render(context, request))   
    #output = ""
    #for x in mymembers:
    #    output += "First Name: " + x['first_name'] + "<br>"
    #    output += "Last Name: " + x['last_name'] + "<br>"
    #    output += "Email: " + x['email'] + "<br>"
    #    output += "Phone: " + x['phone'] + "<br>"
    #    output += "Address: " + x['address'] + "<br>"
    #    output += "City: " + x['city'] + "<br>"
    #    output += "State: " + x['state'] + "<br>"
    #    output += "Zipcode: " + x['zipcode'] + "<br>"
    #    output += "Country: " + x['country'] + "<br>"
    #    output += "<br>"
    #return HttpResponse(output)


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']
    city = request.POST['city']
    state = request.POST['state']
    zipcode = request.POST['zipcode']
    country = request.POST['country']
    member = Members(first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, zipcode=zipcode, country=country)
    member.save()
    #return HttpResponse("Record added successfully")
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = { 'mymember': mymember,}
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    member = Members.objects.get(id=id)
    member.first_name = request.POST['first_name']
    member.last_name = request.POST['last_name']
    member.email = request.POST['email']
    member.phone = request.POST['phone']
    member.address = request.POST['address']
    member.city = request.POST['city']
    member.state = request.POST['state']
    member.zipcode = request.POST['zipcode']
    member.country = request.POST['country']
    member.save()
    return HttpResponseRedirect(reverse('index'))


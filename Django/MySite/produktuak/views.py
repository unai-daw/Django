from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from platerak.models import *
from .models import Produktuak

def index(request):
  myproduktuak = Produktuak.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'myproduktuak': myproduktuak,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['izena']
  y = request.POST['prezioa']
  j = request.POST['iraungipenData']
  produktuak = Produktuak(izena=x, prezioa=y, iraungipenData = j)
  produktuak.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  produktua = Produktuak.objects.get(id=id)
  produktua.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  myproduktua = Produktuak.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myproduktua': myproduktua,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  izena = request.POST['izena']
  prezioa = request.POST['prezioa']
  iraungipenData = request.POST['iraungipenData']
  produktua = Produktuak.objects.get(id=id)
  produktua.izena = izena
  produktua.prezioa = prezioa
  produktua.iraungipenData = iraungipenData
  produktua.save()
  return HttpResponseRedirect(reverse('index'))

def creaPizza(request):
  template = loader.get_template('creaPizza.html')
  return HttpResponse(template.render({}, request))

def CalcuCreaPizza(request):
  precioFin =0
  id = request.POST['ingre1']
  id2 = request.POST['ingre2']
  id3 = request.POST['ingre3']
  id4 = request.POST['ingre4']
  id5 = request.POST['ingre5']
  produktua1 = Produktuak.objects.get(id=id)
  produktua2 = Produktuak.objects.get(id=id2)
  produktua3 = Produktuak.objects.get(id=id3)
  produktua4 = Produktuak.objects.get(id=id4)
  produktua5 = Produktuak.objects.get(id=id5)
  

  p1=float(produktua1.prezioa)
  p2=float(produktua2.prezioa)
  p3=float(produktua3.prezioa)
  p4=float(produktua4.prezioa)
  p5=float(produktua5.prezioa)
  
  precioFin=p1+p2+p3+p4+p5
  platos = list()

  myplaterak = Platerak.objects.all().values()
  #for plat in myplaterak:    
  #   if plat.prezioa < precioFin:
  #      platos.add(plat.prezioa)
    
  template = loader.get_template('creaPizza.html')
  context = {
    'myplaterak': myplaterak,
    'precioFin':precioFin,
    #'platos':platos,
  }
  return HttpResponse(template.render(context,request))
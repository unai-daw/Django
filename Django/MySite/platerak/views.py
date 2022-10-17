from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Platerak

def platerakHTML(request):
  myplaterak = Platerak.objects.all().values()
  template = loader.get_template('platerakHTML.html')
  context = {
    'myplaterak': myplaterak,
  }
  return HttpResponse(template.render(context, request))

def addPlat(request):
  template = loader.get_template('addPlat.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['izena']
  y = request.POST['deskripzioa']
  j = request.POST['prezioa']
  k = request.POST['FechaCreacion']

  platera = Platerak(izena=x, deskripzioa=y, prezioa=j, FechaCreacion=k)
  platera.save()
  myplaterak = Platerak.objects.all().values()
  template = loader.get_template('platerakHTML.html')
  context = {
    'myplaterak': myplaterak,
  }
  return HttpResponse(template.render(context, request))

def deletePlat(request, id):
  platera = Platerak.objects.get(id=id)
  platera.delete()
  myplaterak = Platerak.objects.all().values()
  template = loader.get_template('platerakHTML.html')
  context = {
    'myplaterak': myplaterak,
  }
  return HttpResponse(template.render(context, request))

def updatePlat(request, id):
  myplaterak = Platerak.objects.get(id=id)
  template = loader.get_template('updatePlat.html')
  context = {
    'myplaterak': myplaterak,
  }
  return HttpResponse(template.render(context, request))

def updaterecordPlat(request, id):
  izena = request.POST['izena']
  deskripzioa = request.POST['deskripzioa']
  prezioa = request.POST['prezioa']
  FechaCreacion = request.POST['FechaCreacion']
  platera = Platerak.objects.get(id=id)
  platera.izena = izena
  platera.deskripzioa = deskripzioa
  platera.prezioa = prezioa
  platera.FechaCreacion = FechaCreacion
  platera.save()
  #return HttpResponseRedirect(reverse('platerakHTML'))
  myplaterak = Platerak.objects.all().values()
  template = loader.get_template('platerakHTML.html')
  context = {
    'myplaterak': myplaterak,
  }
  return HttpResponse(template.render(context, request))

def sumaPlat(request):
  template = loader.get_template('sumaPlat.html')
  return HttpResponse(template.render({}, request))

def calcusumPlat(request):
  precioFin =0
  id = request.POST['id']
  id2 = request.POST['id2']
  id3 = request.POST['id3']
  platera = Platerak.objects.get(id=id)
  platera2 = Platerak.objects.get(id=id2)
  platera3 = Platerak.objects.get(id=id3)
  
  precioFin=platera.prezioa+platera2.prezioa+platera3.prezioa
 
  template = loader.get_template('sumaPlat.html')
  return HttpResponse(template.render({'precioFin':precioFin}, request))



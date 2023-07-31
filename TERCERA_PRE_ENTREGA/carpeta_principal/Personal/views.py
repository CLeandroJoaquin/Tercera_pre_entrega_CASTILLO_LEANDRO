from django.shortcuts import render
from Personal.models import Personal, Ventas, Inventario
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.


def lista_personal(request):
    contexto = {
        "personal": Personal.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='Personal/lista_personal.html',
        context=contexto,
    )
    return http_response

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response



def crear_personal(request):
    
   if request.method == "POST":
       data = request.POST
       personal = Personal(nombre=data['nombre'], numero_legajo=data['numero_legajo'])
       personal.save()
       url_exitosa = reverse('lista_personal')
       return redirect(url_exitosa)
   else:  # GET
       return render(
           request=request,
           template_name='Personal/formulario_crear_persona_a_mano.html',
       )

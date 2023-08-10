from django.shortcuts import render
from Personal.models import Personal, Ventas, Inventario
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from Personal.forms import PersonalFormulario 
from django.db.models import Q


# Create your views here.
@login_required
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



def crear_personal_version1(request):
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




def crear_personal(request):
   if request.method == "POST":
       formulario = PersonalFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           nombre = data["nombre"]
           numero_legajo = data["numero_legajo"]
           antiguedad= data["antiguedad"]  # lo crean solo en RAM
           puesto=data["puesto"]
           personal = Personal(nombre=nombre, numero_legajo=numero_legajo, antiguedad=antiguedad, puesto=puesto)
           personal.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('lista_personal')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = PersonalFormulario()
   http_response = render(
       request=request,
       template_name='Personal/formulario_persona.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_personal(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       nombre = Personal.objects.filter(nombre__contains=busqueda)
       
       
       #nombre = Personal.objects.filter(
        #   Q(nombre__contains=busqueda) | Q(puesto__contains=busqueda) | Q(numero_legajo__contains=busqueda) | Q(antiguedad__contains=busqueda)
       #)
       contexto = {
           "personal": nombre,
       }
       http_response = render(
           request=request,
           template_name='Personal/lista_personal.html',
           context=contexto,
       )
       return http_response




def eliminar_personal(request, id):
   persona = Personal.objects.get(id=id)
   if request.method == "POST":
       #borra la persona
       persona.delete()
       #redirecciona a la url exitosa
       url_exitosa = reverse('lista_personal')
       return redirect(url_exitosa)


def editar_personal(request, id):
   persona = Personal.objects.get(id=id)
   if request.method == "POST":
       formulario = PersonalFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           persona.nombre = data['nombre']
           persona.numero_legajo = data['numero_legajo']
           persona.antiguedad=data['antiguedad']
           persona.puesto=data['puesto']
           persona.save()
           url_exitosa = reverse('lista_personal')
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'nombre': persona.nombre,
           'numero_legajo': persona.numero_legajo,
           'antiguedad':persona.antiguedad,
           'puesto':persona.puesto,
           
       }
       formulario = PersonalFormulario(initial=inicial)
   return render(
       request=request,
       template_name='Personal/formulario_persona.html',
       context={'formulario': formulario},
   )

       

#DEFINICION DE CODIGO PARA INVENTARIOS....DAR DE ALTA MATERIAL, EDITAR, Y ELIMINAR


def lista_material(request):
    
    contexto = {
            "material": Personal.objects.all(),
    }
    http_response = render(
            request=request,
            template_name='Personal/lista_material.html',
            context=contexto,
        )
    return http_response



def crear_material(request):
   if request.method == "POST":
       formulario = PersonalFormulario(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data  # es un diccionario
           codigo = data["codigo"]
           unidades = data["unidades"]
           localizador= data["localizador"]  # lo crean solo en RAM
          
           inventario = Personal(codigo=codigo, unidades=unidades, localizador=localizador)
           inventario.save()  # Lo guardan en la Base de datos

           # Redirecciono al usuario a la lista de cursos
           url_exitosa = reverse('crear_material')  # estudios/cursos/
           return redirect(url_exitosa)
   else:  # GET
       formulario = PersonalFormulario()
   http_response = render(
       request=request,
       template_name='Personal/formulario_inventario.html',
       context={'formulario': formulario}
   )
   return http_response


def buscar_material(request):
   if request.method == "POST":
       data = request.POST
       busqueda = data["busqueda"]
       codigo = Personal.objects.filter(codigo__contains=busqueda)
       
       
       #nombre = Personal.objects.filter(
        #   Q(nombre__contains=busqueda) | Q(puesto__contains=busqueda) | Q(numero_legajo__contains=busqueda) | Q(antiguedad__contains=busqueda)
       #)
       contexto = {
           "material": codigo,
       }
       http_response = render(
           request=request,
           template_name='Personal/lista_material.html',
           context=contexto,
       )
       return http_response




def eliminar_material(request, id):
   material = Personal.objects.get(id=id)
   if request.method == "POST":
       #borra la persona
       material.delete()
       #redirecciona a la url exitosa
       url_exitosa = reverse('lista_material')
       return redirect(url_exitosa)

def editar_material(request, id):
    material = Personal.objects.get(id=id)
    if request.method == "POST":
        formulario = PersonalFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            material.codigo = data['codigo']
            material.unidades = data['unidades']
            material.localizador = data['localizador']

            material.save()
            url_exitosa = reverse('lista_material')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'codigo': material.codigo,
            'unidades': material.unidades,
            'localizador': material.localizador,
        }
        formulario = PersonalFormulario(initial=inicial)
    return render(
        request=request,
        template_name='Personal/formulario_inventario.html',  # Corrección en el nombre de la plantilla
        context={'formulario': formulario},
    )
       
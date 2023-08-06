from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.



class Personal(models.Model):
    nombre = models.CharField(max_length=230)
    numero_legajo = models.CharField(max_length=230)
    antiguedad = models.IntegerField(null=True)
    puesto = models.CharField(max_length=230, default='Sin puesto') 
    creador = models.ForeignKey(User, on_delete= models.CASCADE, related_name='personas_creadas', default=1)
    def __str__(self):
            return f"{self.nombre},{self.numero_legajo},{self.antiguedad},{self.puesto}"
    

class Inventario(models.Model):
    codigo = models.CharField(max_length=230)
    unidades = models.CharField(max_length=230)
    localizador =  models.IntegerField(null=True)
    def __str__(self):
         return f"{self.codigo},{self.unidades},{self.localizador}"


class Ventas(models.Model):
    codigo_de_producto=models.CharField(max_length=230)
    unidades = models.IntegerField(null=True)
    vendedor = models.CharField(max_length=230)
    descripcion= models.TextField()
    def __str__(self):
         return f"{self.codigo_de_producto}, {self.unidades},{self.vendedor},{self.descripcion}"
    




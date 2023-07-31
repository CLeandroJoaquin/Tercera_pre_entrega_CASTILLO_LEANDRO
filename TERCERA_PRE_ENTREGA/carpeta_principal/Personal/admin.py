from django.contrib import admin

# Register your models here.
from  .models import Personal, Ventas, Inventario

admin.site.register(Personal)
admin.site.register(Ventas)
admin.site.register(Inventario)
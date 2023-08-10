from django.urls import include, path
from . import views
from .views import inicio
urlpatterns = [
    path("",inicio, name="inicio"),
    path("personal/", views.lista_personal,name="Personal"),
    path("personal/crear-persona/", views.crear_personal, name="crear_personal"),
    path("personal", views.lista_personal, name="lista_personal"),
    path("buscar-persona/", views.buscar_personal, name="buscar_personal"),
    path('eliminar-persona/<int:id>/', views.eliminar_personal, name="eliminar_persona"),
    path("editar-curso/<int:id>/", views.editar_personal, name="editar_persona"),
    path("personal/crear-inventario/", views.crear_material, name="crear_material"),
    path("personal/inventario/",views.lista_material, name="lista_material"),
   
]
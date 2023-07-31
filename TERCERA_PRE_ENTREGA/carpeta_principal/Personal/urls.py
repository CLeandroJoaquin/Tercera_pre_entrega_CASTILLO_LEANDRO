from django.urls import include, path
from . import views
from .views import inicio
urlpatterns = [
    path("",inicio, name="inicio"),
    path("personal", views.lista_personal,name="Personal"),
    path("personal/crear-persona/", views.crear_personal, name="crear_personal"),
    path("personal", views.lista_personal, name="lista_personal"),
    
    
]
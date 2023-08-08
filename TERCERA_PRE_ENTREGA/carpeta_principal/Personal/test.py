from django.test import TestCase
from django.contrib.auth.models import User
from Personal.models import Personal


class PersonalTests(TestCase):
   """En esta clase van todas las pruebas del modelo Curso."""

   def test_creacion_personal(self):
       # caso uso esperado
       persona = Personal(nombre="Nombre", puesto="Puesto")
       persona.save()

       # Compruebo que el curso fue creado y la data fue guardad correctamente
       self.assertEqual(Personal.objects.count(), 1)
       self.assertEqual(persona.nombre, "Nombre")
       self.assertEqual(persona.puesto, "Puesto")

   def test_persona_str(self):
       persona = Personal(nombre="Leandro", puesto="Jefe")
       persona.save()

       # Compruebo el str funciona como se desea
       self.assertEqual(persona.__str__(), "Leandro, Jefe")


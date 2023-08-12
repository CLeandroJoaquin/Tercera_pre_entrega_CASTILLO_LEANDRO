from django.test import TestCase
from django.contrib.auth.models import User
from Personal.models import Personal


class PersonalTests(TestCase):
   """En esta clase van todas las pruebas del modelo Curso."""

   def test_creacion_personal(self):
       # caso uso esperado
       self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
       persona = Personal(nombre="Nombre", puesto="Puesto", creador=self.user)
       persona.save()

       # Compruebo que el curso fue creado y la data fue guardad correctamente
       self.assertEqual(Personal.objects.count(), 1)
       self.assertEqual(persona.nombre, "Nombre")
       self.assertEqual(persona.puesto, "Puesto")

   def test_persona_str(self):
       self.user = User.objects.create_user(username="egp1020", email='javed@javed.com', password='my_secret')
       persona = Personal(nombre="Leandro", puesto="Jefe", creador=self.user)
       persona.save()

       # Compruebo el str funciona como se dese
       self.assertEqual(persona.__str__(), "Leandro, Jefe")


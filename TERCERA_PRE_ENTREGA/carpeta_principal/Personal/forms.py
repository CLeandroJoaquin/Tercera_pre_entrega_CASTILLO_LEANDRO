from django import forms

class PersonalFormulario(forms.Form):
   nombre = forms.CharField(required=True, max_length=64)
   numero_legajo = forms.IntegerField(required=True, max_value=50000)
   antiguedad= forms.IntegerField(required=True, max_value=200)
   puesto = forms.CharField(required=True, max_length=64)


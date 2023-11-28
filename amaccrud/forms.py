from django import forms
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import ProtectedError

from . import models

class MetaForm(forms.ModelForm):
    class Meta:
        model=models.MetaModelo
        fields=['nombre','fecha',
                'objetivo','formato',
                'cant_hombres','cant_mujeres',
                'lugar','dirigido','responsable','descripcion']
    
class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields=['nombre'] 
      
class EventoForm(forms.ModelForm):
    class Meta:
        model = models.Evento
        fields=['nombre','tipo','fecha','apoyo',
                'cant_hombres','cant_mujeres','lugar',
                'dirigido','responsable','colonia','meta',
                'descripcion']

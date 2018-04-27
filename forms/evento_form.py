# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from caninana.models import Evento

class EventoForm(ModelForm):
    url = forms.CharField(max_length=200, required=False)
    class Meta:
        model = Evento
        fields = (
            'url', 'titulo', 'descricao', 'favico', 'logo', 'inicio_at', 'encerramento_at', 'template'
        )
        labels = {
            'url':'URL do Evento',
            'titulo':'Titulo do Evento',
            'descricao':'Descrição do evento',
            'favico':'Favicon',
            'logo':'Logo',
            'inicio_at':'Data de abertura',
            'encerramento_at':'Data de encerramento',
            'template':'Template do Site'
        }
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from caninana_admin.forms.evento_form import EventoForm
from caninana.models import Evento

import datetime

TEMPLATE = 'manage/%s.html'

def create(request, _template):
    template = TEMPLATE % _template
    form = EventoForm(request.POST or None, request.FILES or None, instance=None)
    if form.is_valid():
        model = form.save(commit=False)
        model.favico = request.FILES.get('favico', None)
        model.logo = request.FILES.get('logo', None)
        #if not form.cleaned_data['url'].strip():
        #    model.url = slugify(model.titulo)
        model.save()
        response = redirect('manage_event:action')
        response['Location'] += '?view=%s' % model.url
        return response
    context = {
        'form':form,
        'titulo':'Novo evento',
        'action':'create',
        'view':'novo_evento',
    }
    return render(request, template, context)

def update(request, evento, _template):
    template = TEMPLATE % _template
    form = EventoForm(request.POST or None, request.FILES or None, instance=evento)
    if form.is_valid():
        model = form.save(commit=False)
        if request.FILES:
            model.favico = request.FILES.get('favico', None)
            model.logo = request.FILES.get('logo', None)
        #if not form.cleaned_data['url'].strip():
        #    model.url = slugify(model.titulo)
        model.save()
        response = redirect('manage_event:action')
        response['Location'] += '?view=%s' % model.url
        return response
    context = {
        'form':form,
        'object':evento,
        'titulo':'Editando evento',
        'action':'update',
        'view':'eventos'
    }
    return render(request, template, context)

def workflow(request, evento):
    if evento.fluxo_trabalho == 'privado':
        evento.fluxo_trabalho = 'publicado'
    else:
        evento.fluxo_trabalho = 'privado'
    evento.publicacao_at = datetime.datetime.now()
    evento.save()
    response = redirect('manage_event:action')
    response['Location'] += '?view=%s' % evento.url
    return response

def view(request, _view, _template):
    template = TEMPLATE % _template
    _object = get_object_or_404(Evento, url=_view)
    context = {
        'object': _object,
        'titulo':'Evento',
        'descricao': _object.titulo,
        'action':'view',
        'view': 'eventos',
    }
    return render(request, template, context)
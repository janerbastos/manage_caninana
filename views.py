# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

from caninana.models import Evento
from caninana.forms.evento_forms import EventoForm

from caninana_admin.utils import get_evento_request
from caninana_admin.conteiners import evento_manager, usuario_manager

# Create your views here.

TEMPLATE = 'manage/%s.html'

def index(request):
    template = 'manage/index.html'
    eventos = Evento.objects.all()
    context = {
        'objects' : eventos,
        'titulo':'Eventos',
        'descricao': 'deste site',
    }

    return render(request, template, context)

def view(request, _view, _template):
    template = TEMPLATE % _template
    _object = None
    _objects = None
    if _view == 'usuarios':
        response = usuario_manager.view(request, _template)
    else:
       response = evento_manager.view(request,_view, _template)
    return response

def action(request):
    _view = request.GET.get('view', None)
    _action = request.GET.get('action', None)

    if _view:
        if _view == 'usuarios':
            if _action == 'new':
                return usuario_manager.create(request, 'usuarios')
            if _action == 'edit':
                _username = request.GET.get('username', None)
                return usuario_manager.update(request, _username, 'usuarios')
            if _action == 'reset-pessaword':
                _username = request.GET.get('username', None)
                return usuario_manager.reseta_senha(request, _username, 'usuarios')
            if _action == 'vincular-usuario':
                _username = request.GET.get('username', None)
                return usuario_manager.vincular(request, _username)
            if _action == 'desvincular-usuario':
                _username = request.GET.get('username', None)
                return usuario_manager.desvincular(request, _username)
            return view(request, _view, 'usuarios')
        else:
            _evento = get_object_or_404(Evento, url=_view)
            if _action == 'edit':
                return evento_manager.update(request, _evento, 'eventos')
            if _action == 'fluxo-trabalho':
                evento = get_object_or_404(Evento, url=_view)
                return evento_manager.workflow(request, evento)
            return view(request, _evento.url, 'eventos')

    elif _view == None and _action:
        if _action=='new':
            return evento_manager.create(request, 'eventos')


    return index(request)


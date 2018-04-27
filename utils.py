# -*- coding: utf-8 -*-

#from django.shortcuts import get_object_or_404

from caninana.models import Evento

LIST_KEY_SISTEM=['manage_main', ]

def get_list_request(request):
    try:
        _path = request.path.strip('/').split('/')
    except:
        _path = request.path.strip('/')
    return _path

def get_url_request(request, indice=0):
    _path = get_list_request(request)
    if isinstance(_path, list):
        return _path[indice]
    else:
        return _path

def get_evento_request(request):
    result = get_url_request(request)
    try:
        _evento = Evento.objects.get(url=result)
        return _evento
    except Evento.DoesNotExist:
        return None
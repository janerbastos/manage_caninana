# -*- coding: utf-8 -*-

from django import template
from django.db.models import Q
from django.utils.html import format_html
from caninana_admin.forms.usuario_form import UsuarioForm, VicularUsuarioForm
from caninana.models import Evento

register = template.Library()

@register.inclusion_tag('manage/tags/main_menu.html', takes_context=True)
def has_menu_main(context, **kwargs):
    object = kwargs.get('object', None)
    action = kwargs.get('action', None)
    view = kwargs.get('view', None)
    if not isinstance(object, Evento):
        object = None
    context = {
        'site':'Manage',
        'home':'index',
        'menus':None,
        'evento':object,
        'action':action,
        'view':view,
    }
    return context

@register.assignment_tag(takes_context=True)
def has_form(context, **kwargs):
    form = kwargs.get('form', None)
    if form == 'vincular':
        form = VicularUsuarioForm(context.request.POST or None)
    return form

@register.assignment_tag(takes_context=True)
def has_membros(context, **kwargs):
    evento = kwargs.get('evento', None)
    result = None
    if evento:
        result = evento.ref_eventos.all()
    return result
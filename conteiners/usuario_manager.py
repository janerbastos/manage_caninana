# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from caninana_admin.forms.usuario_form import UsuarioForm, UsuarioEditForm, UsuarioResetaPwsForm, VicularUsuarioForm
from caninana.models import Usuario
from django.template.loader import render_to_string

TEMPLATE = 'manage/%s.html'

def create(request, _template):
    template = TEMPLATE % _template
    form = UsuarioForm(request.POST or None, instance=None)
    if form.is_valid():
        model = form.save(commit=False)
        model.save()
        response = redirect('manage_event:action')
        response['Location'] += '?view=%s' % 'usuarios'
        return response
    context = {
        'form':form,
        'titulo':'Novo usuário',
        'action':'create',
        'view':'usuarios',
    }
    return render(request, template, context)

def reseta_senha(request, username, _template):
    template = TEMPLATE % _template
    user = get_object_or_404(User, username=username)
    form = UsuarioResetaPwsForm(request.POST or None)

    if request.is_ajax():
        html = render_to_string('manage/includes/ajax/conteudo_auxiliar.html', {'form': form, 'opcao': 'reset-pessaword'})
        data = {
            'result' : html
        }
        return JsonResponse(data)

    if form.is_valid():
        nova_senha = form.cleaned_data.get('confirma_password', '')
        user.set_password(nova_senha)
        user.save()
        response = redirect('manage_event:action')
        response['Location'] += '?view=%s' % 'usuarios'
        return response


    context = {
        'form':form,
        'object':user,
        'title':'Resetar senha do usuário',
        'action':'reseta-senha',
        'view':'usuarios',
    }
    return render(request, template, context)

def update(request, username, _template):
    template = TEMPLATE % _template
    user = get_object_or_404(User, username=username)
    form = UsuarioEditForm(request.POST or None, instance=user)
    if form.is_valid():
        model = form.save(commit=False)
        model.save()
        response = redirect('manage_event:action')
        response['Location'] += '?view=%s' % 'usuarios'
        return response
    context = {
        'form':form,
        'object':user,
        'title':'Editando Usuário',
        'action':'update',
        'view': 'usuarios',
    }
    return render(request, template, context)

def vincular(request, username, _template=None):
    form = VicularUsuarioForm(request.POST or None)
    if form.is_valid():
        evento = form.cleaned_data.get('evento', '')
        try:
            usuario = Usuario.objects.get(user__username=username, evento=evento)
            usuario.grupo = form.cleaned_data.get('grupo', '')
            usuario.save()
        except Usuario.DoesNotExist:
            user = get_object_or_404(User, username=username)
            model = form.save(commit=False)
            model.user = user
            model.save()

    response = redirect('manage_event:action')
    response['Location'] += '?view=%s' % 'usuarios'
    return response

def desvincular(request, username, _template=None):

    if request.method == 'POST':
        list = request.POST.getlist('user_sites')
        Usuario.objects.filter(id__in=list).delete()

        return redirect('/manage_main/?view=usuarios')

    template = 'manage/includes/ajax/conteudo_auxiliar.html'
    if _template:
        template = _template
    sites = Usuario.objects.filter(user__username=username)
    html = render_to_string(template, {'objects': sites, 'opcao': 'desvincular-usuario'})
    data = {
        'result' : html,
    }
    return JsonResponse(data)

def view(request, _template):
    template = TEMPLATE % _template
    _objects = User.objects.all()
    context = {
        'objects': _objects,
        'titulo':'Usuários',
        'action':'view',
        'view': 'usuarios',
    }
    return render(request, template, context)
# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from caninana.models import Usuario

class UsuarioForm(ModelForm):
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())
    confirma_password = forms.CharField(label='Confirmar senha', required=True, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_staff', 'is_active', 'is_superuser', 'password')
        labels = {
            'fist_name':'Primeiro nome',
            'last_name':'Último nome',
            'username':'Nome de usuário',
            'email':'Endereço de email',
            'is_staff': 'Acesso ao painel admin do Django',
            'is_active': 'Usuário ativo',
            'is_superuser' : 'Superusuário',
            'password':'Senha de acesso',
            }

    def clean_confirma_password(self):
        pws = self.cleaned_data.get('password', False)
        confirma_pws = self.cleaned_data.get('confirma_password', False)

        if pws != confirma_pws:
            raise ValidationError('Os dois campos de senha não confirma')

        return self.cleaned_data.get('password', '')


class UsuarioEditForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff', 'is_active', 'is_superuser',
        )

        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'email': 'Email',
            'username': 'Nome do usuário',
            'is_staff': 'Acesso ao painel admin do Django',
            'is_active': 'Usuário ativo',
            'is_superuser': 'Superusuário',
        }


class UsuarioResetaPwsForm(forms.Form):
    password = forms.CharField(label='Nova Senha', required=True, widget=forms.PasswordInput())
    confirma_password = forms.CharField(label='Confirmar senha', required=True, widget=forms.PasswordInput())

    def clean_confirma_password(self):
        pws = self.cleaned_data.get('password', False)
        confirma_pws = self.cleaned_data.get('confirma_password', False)

        if pws != confirma_pws:
            raise ValidationError('Os dois campos de senha não confirma')

        return self.cleaned_data.get('password', '')

class VicularUsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ('evento', 'grupo')
        labels = {
            'evento':'Selecione o Evento',
            'grupo':'Informe grupo',
        }
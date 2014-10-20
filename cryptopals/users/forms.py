# -*- coding: utf-8 -*-
from django import forms
from django.forms import Textarea

from .models import User, UserProfile


class UserForm(forms.ModelForm):
    first_name = forms.CharField(label="Name", max_length=30)
    last_name = forms.CharField(label="Surname", max_length=30)

    def __init__(self, *args, **kw):
        super(UserForm, self).__init__(*args, **kw)
        self.fields['first_name'].initial = self.instance.first_name
        self.fields['last_name'].initial = self.instance.last_name
        self.fields['public_key'].initial = self.instance.profile.public_key
        self.fields['list_user'].initial = self.instance.profile.list_user
        self.fields['write_about'].initial = self.instance.profile.write_about

        self.fields.keyOrder = [
            'first_name',
            'last_name',
            'public_key',
            'list_user',
            'write_about'
            ]

    def save(self, *args, **kw):
        super(UserForm, self).save(*args, **kw)
        self.instance.first_name = self.cleaned_data.get('first_name')
        self.instance.last_name = self.cleaned_data.get('last_name')
        profile = self.instance.profile
        profile.public_key = self.cleaned_data.get('public_key')
        profile.write_about = self.cleaned_data.get('write_about')
        profile.list_user = self.cleaned_data.get('list_user')
        profile.save()
        self.instance.save()

    class Meta:
        model = UserProfile
        labels = {
            'public_key': ('Public Key ID'),
            'write_about': ('What I write about as a penpal. More detail the better.'),
            'list_user': ('List your profile on the site? \
                You can add yourself again at any time.')
        }
        # widgets = {
        #     'write_about': Textarea(attrs={'label':'What I write about as a penpal'}),
        # }
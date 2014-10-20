# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)

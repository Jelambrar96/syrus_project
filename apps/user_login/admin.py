# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from apps.user_login.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass 

admin.site.register(User, UserAdmin)


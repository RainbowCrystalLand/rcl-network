# -*- coding: utf-8 -*-

#from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from users.models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 
		'is_superuser')
	list_filter = ('is_active', 'is_staff', 'is_superuser')

admin.site.register(User, UserAdmin)

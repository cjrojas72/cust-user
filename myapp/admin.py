from django.contrib import admin
from myapp.models import CustUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustUser, UserAdmin) 

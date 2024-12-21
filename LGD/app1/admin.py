from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Admin

# Register the Admin model
admin.site.register(Admin)

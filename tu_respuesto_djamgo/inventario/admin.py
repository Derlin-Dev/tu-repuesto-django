from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proveedor, Repuesto

admin.site.register(Proveedor)
admin.site.register(Repuesto)
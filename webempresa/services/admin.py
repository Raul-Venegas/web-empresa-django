from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceArmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceArmin)
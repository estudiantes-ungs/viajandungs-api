from django.contrib import admin
from .models import Viaje, Noticia

# Register your models here.

admin.site.register(Viaje)
admin.site.register(Noticia)

class NoticiaInline(admin.TabularInline):
    model = Noticia

class ViajeAdmin(admin.ModelAdmin):
    inlines = [
        NoticiaInline,
    ]
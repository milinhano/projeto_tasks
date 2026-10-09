from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tarefa)

#@admin.register(Categoria)
#class CategoriaAdmin(admin.ModelAdmin):
#    list_display = ("id", "nome", "criada_em")
#    search_fields = ("nome",)
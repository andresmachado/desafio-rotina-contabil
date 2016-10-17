from django.contrib import admin

# Register your models here.

from .models import Fluxograma, TarefaFluxograma, Tarefa


class TarefaAdmin(admin.ModelAdmin):
    list_display = ['titulo']
admin.site.register(Tarefa, TarefaAdmin)


class TarefasAdmin(admin.TabularInline):
    model = TarefaFluxograma
    extra = 1


class FluxogramaAdmin(admin.ModelAdmin):
    inlines = [TarefasAdmin]
    list_display = ['titulo']
admin.site.register(Fluxograma, FluxogramaAdmin)

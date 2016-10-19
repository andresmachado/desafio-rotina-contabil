from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Fluxograma, TarefaFluxograma, Tarefa


def list_flux(request, template_name="fluxogramas/list.html"):
    fluxogramas = Fluxograma.objects.all()
    return render(request, template_name, {'fluxogramas': fluxogramas})


@csrf_exempt
def create_flux(request, template_name="fluxogramas/create.html"):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        novo_fluxograma = Fluxograma.objects.create(titulo=titulo)
        tarefas = request.POST.get('tarefas')

        if tarefas:
            tarefas = request.POST.get('tarefas', None).split("&")
            for index, tarefa in enumerate(tarefas):
                tarefa_titulo = tarefa.split('=')[1]
                nova_tarefa = Tarefa.objects.create(titulo=tarefa_titulo)
                novo_fluxtaf = TarefaFluxograma(fluxograma=novo_fluxograma, tarefa=nova_tarefa, numero=index)
                novo_fluxtaf.save()
            return redirect('fluxogramas:list')
        else:
            return redirect('fluxogramas:list')
    return render(request, template_name)


def detail_flux(request, pk, template_name='fluxogramas/detail.html'):
    fluxograma = get_object_or_404(Fluxograma, pk=pk)
    tarefas = fluxograma.tarefafluxograma_set.all()
    return render(request, template_name, {"fluxograma": fluxograma, "tarefas": tarefas})


@csrf_exempt
def edit_flux(request, pk, template_name='fluxogramas/edit.html'):
    flux = get_object_or_404(Fluxograma, pk=pk)
    tarefas = flux.tarefafluxograma_set.all()

    if request.method == "POST" and not request.is_ajax():
        prioridade = request.POST.get('prioridade')
        titulo = request.POST.get('titulo')
        tarefa = Tarefa.objects.create(titulo=titulo)
        fluxtaf = TarefaFluxograma(tarefa=tarefa, numero=prioridade, fluxograma=flux)
        fluxtaf.save()
        return redirect('fluxogramas:edit', pk=pk)

    if request.is_ajax():
        for index, tarefa_id in enumerate(request.POST.getlist('tarefa[]')):
            tarefa, created = TarefaFluxograma.objects.get_or_create(pk=tarefa_id, fluxograma=flux)
            tarefa.numero = index
            tarefa.save()

    return render(request, template_name, {"fluxograma": flux, 'tarefas': tarefas})

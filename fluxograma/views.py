from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Fluxograma


def list_flux(request, template_name="fluxogramas/list.html"):
    fluxogramas = Fluxograma.objects.all()
    return render(request, template_name, {'fluxogramas': fluxogramas})


def create_flux(request, template_name="fluxogramas/create.html"):
    return render(request, template_name)


def detail_flux(request, pk, template_name='fluxogramas/detail.html'):
    fluxograma = get_object_or_404(Fluxograma, pk=pk)
    tarefas = fluxograma.tarefafluxograma_set.all()
    return render(request, template_name, {"fluxograma": fluxograma, "tarefas": tarefas})


def edit_flux(request, pk, template_name='fluxogramas/edit.html'):
    return render(request, template_name, )
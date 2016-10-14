from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=128, default='')


class Fluxograma(models.Model):
    titulo = models.CharField(max_length=128, default='')
    tarefas = models.ManyToManyField(Tarefa, through='TarefaFluxograma')


class TarefaFluxograma(models.Model):
    tarefa = models.ForeignKey(Tarefa)
    fluxograma = models.ForeignKey(Fluxograma)
    numero = models.PositiveIntegerField()

    class Meta:
        ordering = ('numero',)
        unique_together = ('tarefa', 'fluxograma', 'numero')

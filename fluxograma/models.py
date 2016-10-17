from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.titulo


class Fluxograma(models.Model):
    titulo = models.CharField(max_length=128, default='')
    tarefas = models.ManyToManyField(Tarefa, through='TarefaFluxograma')

    def __str__(self):
        return self.titulo


class TarefaFluxograma(models.Model):
    tarefa = models.ForeignKey(Tarefa)
    fluxograma = models.ForeignKey(Fluxograma)
    numero = models.PositiveIntegerField()

    def __str__(self):
        return self.tarefa.titulo

    class Meta:
        ordering = ('numero',)
        unique_together = ('tarefa', 'fluxograma', 'numero')

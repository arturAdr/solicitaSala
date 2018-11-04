# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django import forms
from django.utils import formats
from sala.models import Sala


class Agenda(models.Model):
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    qtd_pessoas = models.IntegerField()
    sala = models.ForeignKey(Sala, verbose_name='Sala',
                             on_delete=models.PROTECT)

    class Meta:
        verbose_name = u'Agenda'
        verbose_name_plural = u'Agendas'

    def __str__(self):
        return '{}-{}-{}'.format(self.data_inicio, self.data_final, self.sala.titulo)

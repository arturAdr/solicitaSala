
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from django import forms
from django.utils import formats


class Sala(models.Model):
    titulo = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    class Meta:
        verbose_name = u'Sala'
        verbose_name_plural = u'Salas'

    def __str__(self):
        return self.titulo
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

#Modelos referentes a la distribución administrativa

class Regional(models.Model):
    """Clase que hace referencia a una dirección regional ó institución primaria administrativa dependendiente directamente del Ministerio de educación"""
    nombre = models.CharField(max_length=54)
    pais = models.ForeignKey('Pais')
    director = models.ForeignKey('Funcionario')

    class Meta:
        verbose_name = ('Regional')
        verbose_name_plural = ('Regionales')
    def __str__(self):
        return u" %s " %self.nombre


class Circuito(models.Model):
    """Clase que hace referencia a una división administrativa dependendiente de la dirección regional"""
    nombre = models.CharField(max_length=2)
    regional =models.ForeignKey('Regional')
    supervisor = models.ForeignKey('Funcionario')

    class Meta:
        verbose_name = ('Circuito')
        verbose_name_plural = ('Circuitos')
    def __str__(self):
        return u" %s " %self.nombre
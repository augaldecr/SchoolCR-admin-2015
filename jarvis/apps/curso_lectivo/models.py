# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes al curso lectivo

class CursoLectivo(models.Model):
    """Curso lectivo (2013, 2014, 2015, etc.)"""
    nombre = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Curso lectivo"
        verbose_name_plural = "Cursos lectivos"

    def __str__(self):
        return u" %s " %self.nombre


class Ciclo(models.Model):
    """Clase referente a los ciclos de la educación (III Ciclo de Educación General Básica, Educación diversificada)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Ciclo"
        verbose_name_plural = "Ciclos"

    def __str__(self):
        return u" %s " %self.nombre


class TipoPeriodo(models.Model):
    """Tipo de período(trimestral, semestral, convocatoria)"""
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = "Tipo de periodo"
        verbose_name_plural = "Tipos de periodos"

    def __str__(self):
        return u" %s " %self.nombre


class Periodo(models.Model):
    """Clase referente a las diferentes etapas del curso lectivo ( Primer período, Segundo período, etc)"""
    nombre = models.CharField(max_length=54)
    fechaInicio =  models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False)
    fechaFin =  models.DateField("Fecha de fin", auto_now=False, auto_now_add=False)
    cursoLectivo = models.ForeignKey('CursoLectivo')
    tipo = models.ForeignKey('TipoPeriodo')
    estado = models.BooleanField("Activo", default=False)

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return u" %s " %self.nombre


class Dia(models.Model):
    """Clase referente a los días de la semana(Lunes, Martes, Miércoles, etc.)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Dia"
        verbose_name_plural = "Dias"

    def __str__(self):
        return u" %s " %self.nombre
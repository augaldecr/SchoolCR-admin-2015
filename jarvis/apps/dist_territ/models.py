# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

#Modelos referentes a la distribución territorial

class Pais(models.Model):
    """Clase referente a países"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = ('País')
        verbose_name_plural = ('Países')
    def __str__(self):
        return u" %s " %self.nombre


class Provincia(models.Model):
    """Clase referente a la provincia, departamento, estado ó entidad subnacional al país, ósea territorios en los que se divide el mismo"""
    nombre = models.CharField(max_length=54)
    pais = models.ForeignKey('Pais')
    
    class Meta:
        verbose_name = ('Provincia')
        verbose_name_plural = ('Provincias')
    def __str__(self):
        return u" %s " %self.nombre


class Canton(models.Model):
    """Clase que hace referencia a un cantón ó subdivisión de una provincia"""
    nombre = models.CharField(max_length=54)
    provincia = models.ForeignKey('Provincia')

    class Meta:
        verbose_name = ('Canton')
        verbose_name_plural = ('Cantones')
    def __str__(self):
        return u" %s " %self.nombre


class Distrito(models.Model):
    """Clase que hace referencia a un distrito ó subdivisión de una cantón"""
    nombre = models.CharField(max_length=54)
    canton = models.ForeignKey('Canton')

    class Meta:
        verbose_name = ('Distrito')
        verbose_name_plural = ('Distritos')
    def __str__(self):
        return u" %s " %self.nombre


class Ciudad(models.Model):
    """Clase referente a la ciudad, pueblo, aldea ó localidad dónde se encuentra la institución"""
    nombre = models.CharField(max_length=54)
    distrito = models.ForeignKey('Distrito')

    class Meta:
        verbose_name = ('Ciudad')
        verbose_name_plural = ('Ciudades')
    def __str__(self):
        return u" %s " %self.nombre
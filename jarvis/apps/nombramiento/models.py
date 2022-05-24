# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes a los nombramientos

class ClaseDePuesto(models.Model):
    """Referente a la clase de puesto de una plaza laboral"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Clase de puesto"
        verbose_name_plural = "Clases de puestos"

    def __str__(self):
        return u" %s " %self.nombre

class Especialidad(models.Model):
    """Referente a la especialidad de una plaza laboral dependendiente de una clase de puesto (076 INGLES, INFORMATICA EDUCATIVA III Y IV CICLOS, 127 INFORMATICA EN PROGRAMACION)"""
    nombre = models.CharField(max_length=54)
    claseDePuesto = models.ForeignKey('ClaseDePuesto')

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return u" %s " %self.nombre

class Plaza(models.Model):
    """Clase referente a la plaza laboral"""
    institucion = models.ForeignKey('Institucion')
    especialidad = models.ForeignKey('Especialidad')
    cantidadDeLecciones = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Plaza"
        verbose_name_plural = "Plazas"

    def __str__(self):
        return u" %s -- %s -- %s " %(self.institucion, self.especialidad, self.cantidadDeLecciones)

class Nombramiento(models.Model):
    """Clase referente a nombramientos interinos en la institución"""
    plaza = models.ForeignKey(Plaza)
    funcionario = models.ForeignKey('Funcionario')
    fechaInicio =  models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False)
    fechaFin =  models.DateField("Fecha de fin", auto_now=False, auto_now_add=False)
    grpProfAsign = models.ForeignKey('GrupoProfesional')#Categoría asignada en el momento del nombramiento
    estado = models.BooleanField("Activo", default=False)

    class Meta:
        verbose_name = "Nombramiento"
        verbose_name_plural = "Nombramientos"

    def __str__(self):
        return " %s -- %s - %s -- %s " %(self.funcionario, self.fechaInicio, self.fechaFin, self.institucion)

class Recargo(models.Model):
    """Referente a los recargos asignados al funcionario"""
    nombreRecargo = models.CharField(max_length=54)
    nombramiento = models.ForeignKey('Nombramiento')
    tipo = models.ForeignKey('TipoRecargo')
    porcentaje = models.PositiveSmallIntegerField()
    fechaInicio =  models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False)
    fechaFin =  models.DateField("Fecha de fin", auto_now=False, auto_now_add=False)
    estado = models.BooleanField("Activo", default=False)

    class Meta:
        verbose_name = "Recargo"
        verbose_name_plural = "Recargos"

    def anho(self):
        return u" %s " %self.fechaInicio.year

    def __str__(self):
        return u" %s -- %s " %(self.nombreRecargo, self.anho,)

class TipoRecargo(models.Model):
    """Tipos de recargo (administrativo ó docente)"""
    tipo = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Tipo de recargo"
        verbose_name_plural = "Tipos de recargos"

    def __str__(self):
        return u" %s " %self.tipo

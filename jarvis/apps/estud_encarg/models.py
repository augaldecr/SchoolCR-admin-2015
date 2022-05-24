# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes a la poblacion estudiantil y sus encargados

class Estudiante(models.Model):
    """Clase referente a un estudiante matriculado en la institución"""
    persona = models.ForeignKey('Persona')
    estado = models.BooleanField("Activo", default=False)
    #adecuacion = models.ForeignKey('Adecuacion')#####Tabla adecuación
    fechaIngreso = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return u" %s "
#   def estado_default():
#       return False


class Encargado(models.Model):
    persona = models.ForeignKey('Estudiante')
    lugarDeTrabajo = models.CharField(max_length=54)
    viveConEstudiante = models.BooleanField("Vive con el estudiante", default=True)
    escolaridad = models.ForeignKey('Escolaridad')
    ocupacion = models.ForeignKey('Ocupacion')
    parentesco = models.ForeignKey('Parentesco')
    ingresoMensual = models.PositiveSmallIntegerField("Ingreso mensual", blank=True, null=True)

    class Meta:
        verbose_name = "Encargado"
        verbose_name_plural = "Encargados"

    def __str__(self):
        return u" %s " %self.persona

#   def vive_default():
#       return True


class Escolaridad(models.Model):
    """Referente al nivel de escolaridad de una persona"""
    nivel = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Escolaridad"
        verbose_name_plural = "Escolaridades"

    def __str__(self):
        return u" %s " %self.nivel


class Ocupacion(models.Model):
    """Referente a la ocupacion de la persona"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Ocupacion"
        verbose_name_plural = "Ocupaciones"

    def __str__(self):
        return u" %s " %self.nombre


class Parentesco(models.Model):
    """Referente al parentesco entre varias personas"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Parentesco"
        verbose_name_plural = "Parentescos"

    def __str__(self):
        return u" %s " %self.nombre
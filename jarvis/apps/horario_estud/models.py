# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes al horario de los estudiantes

class TipoDeAusencia(models.Model):
    """Tipos de faltas a la asistencia(justificada, injustificada, tardía, etc.)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Tipo de ausencia"
        verbose_name_plural = "Tipos de ausencias"

    def __str__(self):
        return u" %s " %self.nombre
    
    
class AusenciaEstudiante(models.Model):
    """Clase referente a las faltas a la asistencia por parte del estudiante"""
    estudiante = models.ForeignKey('Estudiante')
    tipo = models.ForeignKey('TipoDeAusencia')
    fecha = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Ausencia de estudiante"
        verbose_name_plural = "Ausencias de estudiantes"

    def __str__(self):
        return u" %s - %s - %s " %(self.estudiante, self.fecha, self.tipo)
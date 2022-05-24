# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes a los grupos de estudiantes de la institución

class Nivel(models.Model):
    """Referente al nivel o grado académico(sétimo, octavo, etc.)"""
    nivel = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Nivel"
        verbose_name_plural = "Niveles"

    def __str__(self):
        return u" %s " %self.nivel


class Grupo(models.Model):
    """Grupos que dividen niveles"""
    nivel = models.ForeignKey('Nivel')
    seccion = models.PositiveSmallIntegerField(min_value=1, max_value=22)
    cursoLectivo = models.ForeignKey('CursoLectivo')
    estado = models.BooleanField(default=True)
    prof_guia = models.ForeignKey('Docente')

    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"

    def __str__(self):
        return u" %s-%s " %(self.nivel, self.seccion)


class Matricula(models.Model):
    """Clase referente a la matrícula por estudiante"""
    cursoLectivo = models.ForeignKey('CursoLectivo')
    estudiante = models.ForeignKey('Estudiante')
    nivel = models.ForeignKey('Nivel')
    activo = models.BooleanField("Activo", default=False)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    repitencia = models.PositiveSmallIntegerField("Años de repitencia")

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return u" %s - %s" %(self.estudiante, self.cursoLectivo, )
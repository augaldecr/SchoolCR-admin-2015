# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes a los funcionarios

class TipoCargo(models.Model):
    """Tipo de función que cumplen los colaboradores(director, docente, conserje, etc.)"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = ('Tipo de cargo')
        verbose_name_plural = ('Tipos de cargos')

    def __str__(self):
        return u" %s " %self.nombre


class GradoAcademico(models.Model):
    """Clase referente al grado académico del funcionario (ASP, VT1, MT2, PT3, etc.)"""
    nombre = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Grado académico"
        verbose_name_plural = "Grados académicos"

    def __str__(self):
        return u" %s " %self.nombre


class GrupoProfesional(models.Model):
    nombre = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Grupo profesional"
        verbose_name_plural = "Grupos profesionales"

    def __str__(self):
        return u" %s " %self.nombre


class TituloAcademico(models.Model):
    """Clase referente a títulos académicos (bachiller, licenciatura, maestría, etc.)"""
    nombre = models.CharField(max_length=54)
    fechaObtencion = models.DateField()
    institucion = models.ForeignKey('InstitucionSuperior')
    descripcion = models.CharField(max_length=154)
    #imagenTitulo = models.ImageField(upload_to='titulos', blank=True, null=True)

    class Meta:
        verbose_name = "Titulo académico"
        verbose_name_plural = "Titulos académicos"

    def __str__(self):
        return u" %s " %self.nombre


class Sindicato(models.Model):
    """Referente a los sindicatos (SEC, ANDE, APSE, etc.)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Sindicato"
        verbose_name_plural = "Sindicatos"

    def __str__(self):
        return u" %s " %self.nombre


class CondicionActual(models.Model):
    """Clase referente a la condición laboral del funcionario (Normal, Incapacidad, préstamos, etc...)"""
    condicion = models.CharField(max_length=15)
    class Meta:
        verbose_name = "Condicion Actual"
        verbose_name_plural = "CondicionActuals"

    def __str__(self):
        return u" %s " %self.condicion


class Funcionario(models.Model):
    """Clase referente al funcionario como tal"""
    persona = models.OneToOneField('Persona')
    cargo = models.ManyToManyField('TipoCargo')
    especialidad = models.ManyToManyField('Especialidad')
    experienciaAdquirida = models.TextField(max_length=255)
    puestoADesempenhar = models.CharField("Puesto a desempeñar", max_length=54)
    fechaIngresoMEP = models.DateField(auto_now=False, auto_now_add=False)
    direccionEnCursoLectivo = models.CharField("Dirección durante el curso lectivo",max_length=254, blank=True, null=True)
    gradoAcademico = models.ForeignKey('GradoAcademico')
    estado = models.BooleanField('Activo', default=False)
    condicion = models.ForeignKey('CondicionActual')
    sindicatos = models.ManyToManyField('Sindicato')
    aumentosAnuales = models.PositiveSmallIntegerField("Aumentos anuales", blank=True, null=True)

    class Meta:
        verbose_name = ('Funcionario')
        verbose_name_plural = ('Funcionarios')
    
    def __str__(self):
        return u" %s -- %s " %(self.persona, self.cargo) 


class Docente(models.Model):
    """Clase referente exclusivamente al funcionario que ejecuta la labor docente"""
    funcionario = models.ForeignKey('Funcionario')
    grupoProfesional = models.ForeignKey('GrupoProfesional')

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return u" %s " %self.funcionario
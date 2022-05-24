# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes a la institución

class TipoInstitucion(models.Model):
    """Tipo de institución (Preescolar, I & II ciclos, III y IV ciclos, etc.)"""
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = ('TipoInstitucion')
        verbose_name_plural = ('TipoInstituciones')

    def __str__(self):
        return u" %s " %self.nombre


class ModalidadInstitucion(models.Model):
    """Dícese de la modalidad con que trabaja el centro educativo (Académico, técnico, ambientalista, etc.)"""
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = ('ModalidadInstitucion')
        verbose_name_plural = ('ModalidadInstituciones')

    def __str__(self):
        return u" %s " %self.nombre


class TipoDireccion(models.Model):
    """Tipo de dirección del centro(Dirección 1, Dirección 2, Dirección 3)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = ('TipoDireccion')
        verbose_name_plural = ('TipoDirecciones')

    def __str__(self):
        return u" %s " %self.nombre
    


class Institucion(models.Model):
    """Clase referente una institución como tal ()"""
    codigo = models.CharField(max_length=5)
    nombre = models.CharField(max_length=54)
    regional = models.ForeignKey('Regional')
    circuito = models.ForeignKey('Circuito')
    ciudad = models.ForeignKey('Ciudad')
    direccion = models.CharField(max_length=254)
    #escudo = models.ImageField(upload_to='images')
    tipoInstitucion = models.ForeignKey('TipoInstitucion')
    modalidadInstitucion = models.ForeignKey('ModalidadInstitucion')
    tipoDireccion = models.ForeignKey('TipoDireccion')
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=16, blank=True, null=True)
    telefono2 = models.CharField(max_length=16, blank=True, null=True)
    telefax = models.CharField(max_length=16, blank=True, null=True)
    cedulaJuridicaJunta = models.CharField(max_length=15)
    cuentaBancaria = models.CharField(max_length=15)
    cuentaCajaUnica = models.CharField(max_length=15)
    codigoCentroImas = models.CharField(max_length=15)

    class Meta:
        verbose_name = ('Institución')
        verbose_name_plural = ('Instituciones')
    def __str__(self):
        return u" %s " %self.nombre


class InstitucionSuperior(models.Model):
    """Clase referente una institución como tal ()"""
    cedulaJuridica = models.CharField(max_length=15)
    nombre = models.CharField(max_length=54)
    ciudad = models.ForeignKey('Ciudad')
    direccion = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=16, blank=True, null=True)
    telefono2 = models.CharField(max_length=16, blank=True, null=True)
    telefax = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        verbose_name = ('Institución')
        verbose_name_plural = ('Instituciones')
    def __str__(self):
        return u" %s " %self.nombre
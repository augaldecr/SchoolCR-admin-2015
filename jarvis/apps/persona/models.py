# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

from dist_territ import models

#Modelos relacionados a los individuos civiles

class EstadoCivil(models.Model):
    """Clase referente a los distintos estado civiles (casado, soltero, divorciado, etc)"""
    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Estado civil"
        verbose_name_plural = "Estados civiles"

    def __str__(self):
        return u" %s " %self.nombre
        

class Persona(models.Model):
    """Clase referente al individuo como tal en general, sin importar su función dentro del sistema"""
    cedula = models.CharField(max_length=15)
    nombre = models.CharField(max_length=25)
    apellido1 = models.CharField(max_length=25)
    apellido2 = models.CharField(max_length=25, blank=True, null=True)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
    estadoCivil = models.ForeignKey('EstadoCivil')
    nacionalidad = models.ForeignKey('Pais')
    lugarDeNacimiento = models.ForeignKey('Ciudad', blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    #foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefono = models.CharField(max_length=16, blank=True, null=True)
    telefono2 = models.CharField(max_length=16, blank=True, null=True)
    telefonoTrabajo = models.CharField(max_length=16, blank=True, null=True)
    celular = models.CharField(max_length=16, blank=True, null=True)
    telefax = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return u" %s - %s %s %s" %(self.cedula, self.nombre, self.apellido1, self.apellido2)
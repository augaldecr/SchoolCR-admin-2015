# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

#Clases referentes al inventario de la institución

class Activo(models.Model):
    """Clase referente a activos de la institución"""
      class Meta:
          verbose_name = "Activo"
          verbose_name_plural = "Activos"
  
      def __str__(self):
          pass
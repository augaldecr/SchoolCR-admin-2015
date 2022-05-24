# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

#Clases refentes al sistema de juntas de educación

class Junta(models.Model):
    class Meta:
        verbose_name = "Junta"
        verbose_name_plural = "Juntas"

    def __str__(self):
        pass
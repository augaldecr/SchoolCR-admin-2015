# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.db import models

# Clases referentes al horario de los funcionarios

class HorarioFuncionario(models.Model):
    """Clase referente al horario laboral por día de la semana de los funcionarios"""
    funcionario = models.ForeignKey('Funcionario')
    dia = models.ForeignKey('Dia')
    horaEntrada = models.TimeField(auto_now=False, auto_now_add=False)
    horaSalida = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Horario del funcionario"
        verbose_name_plural = "Horarios de los funcionarios"

    def __str__(self):
        return u" %s -- %s " %(self.funcionario, self.dia,)

class AsistenciaFuncionario(models.Model):
    """Clase referente al horario laboral por día de la semana de los funcionarios"""
    funcionario = models.ForeignKey('Funcionario')
    dia = models.ForeignKey('Dia')
    horaEntrada = models.TimeField(auto_now=False, auto_now_add=False)
    horaSalida = models.TimeField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Asistencia del funcionario"
        verbose_name_plural = "Asistencia de los funcionarios"

    def __str__(self):
        return u" %s -- %s " %(self.funcionario, self.dia,)

    def tipoEntrada(self, HorarioFuncionario):
        for self.dia in HorarioFuncionario.dia:
            if self.dia == HorarioFuncionario.dia:
                if self.horaEntrada <= HorarioFuncionario.horaEntrada:
                    return u"Entrada Correcta"
                else:
                    return u"Entrada tardía"

    def tipoSalida(self, HorarioFuncionario):
        for self.dia in HorarioFuncionario.dia:
            if self.dia == HorarioFuncionario.dia:
                if self.horaSalida < HorarioFuncionario.horaSalida:
                    return u"Salida temprana"
                else:
                    return u"Salida correcta"

    #def tipoAusencia(self):
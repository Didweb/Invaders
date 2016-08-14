#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  puntuaciones.py
#
#  Copyright 2016 Eduard Pinuaga Linares <info@did-web.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
PACKS_MUNICION = 80000
N_VIDAS = 3


class Puntos:
	def __init__(self):
		self.nDisparos = 0
		self.nAciertos = 0
		self.PorAciertos = 0
		self.Por_Municion = 0
		self.PacksMunicion = PACKS_MUNICION
		self.municion = PACKS_MUNICION
		self.Nivel = 1
		self.Puntuacion = 0
		self.Vidas = N_VIDAS
		self.PackVidas = N_VIDAS

	def reset_vidas(self):
		self.Vidas = N_VIDAS
		return self.Vidas

	def get_NivelP(self):
		return self.Nivel

	def reset_Nivel(self):
		self.Nivel = 1
		return self.Nivel

	def reset_puntos(self):
		self.nDisparos = 0
		self.nAciertos = 0
		self.Puntuacion = 0
		self.municion = PACKS_MUNICION

	def NivelSuperado(self):
		self.Nivel = self.Nivel+1
		return self.Nivel

	def set_VidasMuerto(self):
		self.Vidas = self.Vidas - 1
		if self.Vidas<0:
			self.Vidas  = 0

	def get_Vidas(self):
		return self.Vidas

	def get_PorMuncion(self):
		return self.Por_Municion

	def AumentaDisparos(self):
		self.nDisparos += 1
		self.PorcentajeAciertos()
		self.ControlMunicion()


	def AumentaAciertos(self):
		self.nAciertos += 1
		self.PorcentajeAciertos()


	def calculoNivelOk(self):
		mas = int(round(self.PorAciertos)*round(self.Puntuacion))/100
		self.Puntuacion = round(self.Puntuacion)+round(mas)


	def AumentarPuntos(self,valor):
		self.Puntuacion += valor

	def get_Puntuacion(self):
		return self.Puntuacion

	def get_NDisparos(self):
		return self.nDisparos


	def get_PorAciertos(self):
		return self.PorAciertos

	def get_vidas(self):
		return self.Vidas

	def get_municion(self):
		return self.municion


		

	def set_municion(self):
		self.municion = self.PacksMunicion
		self.PorcentajeMunicion()
		return self.municion


	def PorcentajeMunicion(self):

		if self.municion == 0:
			por_municion = 0
		else:
			por_municion = (self.municion / PACKS_MUNICION )*100
		self.Por_Municion = por_municion
		return por_municion


	def PorcentajeAciertos(self):

		if self.nAciertos == 0:
			por_aciertos = 0
		else:
			por_aciertos =(self.nAciertos / self.nDisparos)*100

		self.PorAciertos = por_aciertos
		return por_aciertos


	def ControlMunicion(self):
		self.municion = self.municion - self.nDisparos
		return True




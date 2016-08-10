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
PACKS_MUNICION = 1000000

class Puntos:
	def __init__(self,nvidas):
		self.nDisparos = 0
		self.nAciertos = 0
		self.PorAciertos = 0
		self.Por_Municion = 0
		self.municion = PACKS_MUNICION
		self.Nivel = 1
		self.Puntuacion = 0
		self.Vidas = nvidas

	def set_VidasMuerto(self,n = 1):
		self.Vidas = self.Vidas - 1
		if self.Vidas<0:
			self.Vidas  = 0

	def get_Vidas(self):
		return self.Vidas

	def AumentaDisparos(self):
		self.nDisparos += 1
		self.PorcentajeAciertos()
		self.ControlMunicion()


	def AumentaAciertos(self):
		self.nAciertos += 1
		self.PorcentajeAciertos()


	def get_NDisparos(self):
		return self.nDisparos


	def get_PorAciertos(self):
		return self.PorAciertos



	def get_municion(self):
		return self.municion


	def set_municion(self,muni):
		self.municion = self.municion+muni
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


	def CargarMunicion(self,muni):
		self.municion = muni


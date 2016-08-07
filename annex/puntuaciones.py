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


class Puntos:
	def __init__(self):
		self.nDisparos = 0
		self.nAciertos = 0
		self.PorcentajeAciertos = 0

	def AumentaDisparos(self):
		self.nDisparos += 1

	def AumentaAciertos(self):
		self.nAciertos += 1

	def PorcentajeAciertos(self):
		if aciertos == 0:
			por_aciertos = 0
		else:
			por_aciertos =(self.nAciertos / self.nDisparos)*100

		self.PorcentajeAciertos = por_aciertos
		return True



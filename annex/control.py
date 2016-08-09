#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  control.py
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

import pygame, sys
from pygame.locals import *

class Niveles:
	def __init__(self):
		self.Nivel = 1

	def get_Nivel(self):
		return self.Nivel

	def set_Nivel(self, newNivel):
		self.Nivel = newNivel
		return self.Nivel


class GestorAvisos:
	def __init__(self,msn):
		self.msn = msn


	def AvisoMuerte(self,vidas):

		txt = 'Te han matado tienes '+str(vidas)+' vidas '
		self.msn.MensajeSimple(txt, (255,0,0),20,60,300)


	def FinPartida(self):

		txt = 'GAME OVER'
		self.msn.MensajeSimple(txt, (255,0,0),20,60,300)


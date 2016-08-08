#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  niveles.py
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
from annex.puntuaciones import (Puntos)

from characters.nave import (Nave,Laser)
from characters.enemy import (Alien_1,LaserEnemy)

import pygame, sys
from pygame.locals import *

ANCHO = 600
ALTO = 450
ENEMYS_N1 = 10
LINEA_INF = 420

class ServNiveles:

	def __init__(self,nivel,screen,medidaSc,msn):

		self.screen = screen
		self.AnchoScreen = medidaSc[0]
		self.AltoScreen = medidaSc[1]
		self.msn = msn

		# Datos puntos y niveles
		self.SJnivel = nivel
		self.DataPuntos = Puntos()

		# Inicializamos valor de Porcentaje municion disponible
		self.DataPuntos.PorcentajeMunicion()
		self.vidas = self.DataPuntos.Vidas


		self.Tanque = Nave(self.screen,self.DataPuntos)

		self.EscuadronAlien = {}
		for x  in range(ENEMYS_N1):
			self.EscuadronAlien[x] = Alien_1(self.screen)


	def Nivel_1(self):

		for x in range(ENEMYS_N1):
			Alien = self.EscuadronAlien[x]
			Alien.update(self.Tanque)



		self.screen.fill((0,0,0))

		self.Tanque.update()

		self.Tanque.NaveMostrar()
		for x in range(ENEMYS_N1):
			Alien = self.EscuadronAlien[x]
			Alien.MostrarAlien()
			Alien.DisparoEnemy()
			Alien.updateDisparosEnemy(self.Tanque)

			self.Tanque.colisiona_con(Alien )





		self.Tanque.Disparo()
		self.Tanque.updateDisparos()

		# cabecera
		self.msn.Cabecera( self.DataPuntos.nDisparos, \
							self.DataPuntos.PorAciertos, \
							self.DataPuntos.Por_Municion, \
							self.vidas)

		pygame.display.flip()




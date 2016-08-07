#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mensajes.py
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
from annex.puntuaciones import (Puntos)


class Mensajes(Puntos):
	def __init__(self,screen,MedidaScreen):
		self.screen = screen
		self.ANCHO = MedidaScreen[0]
		self.ALTO = MedidaScreen[1]
		self.puntos = Puntos()


	def MensajeSimple(self, txt, color):
		font = pygame.font.SysFont("arial",40)
		pantalla_texto = font.render(txt,True,color )
		self.screen.blit(pantalla_texto,(self.ANCHO/4, self.ALTO/2))

	def Cabecera(self,nd,pa,mu):
		font = pygame.font.SysFont("arial",12)
		pygame.draw.rect(self.screen, (73,9,9), [0, 0, self.ANCHO, 20 ],0)
		pa = "{:.0f}".format(pa)
		pa = str(pa)

		muN = int(mu)
		mu = str(muN)
		txt = 'Eficiencia: '+pa+'% '

		pygame.draw.rect(self.screen,(233,16,8), [15,5,100,10],0)
		pygame.draw.rect(self.screen,(6,161,4), [15,5,muN,10],0)

		pantalla_texto = font.render(txt,True,(102,238,109) )
		self.screen.blit(pantalla_texto,(200, 4))

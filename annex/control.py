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
	def __init__(self,msn,screen):
		self.msn = msn
		self.screen = screen


	def NivelSuperado(self,puntos,nivel):


		portada = pygame.image.load('./img/logo.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Superado el Nivel '+str(nivel)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,300)
		txt = 'Puntos '+str(puntos)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,330)
		pygame.display.flip()


	def AvisoMuerte(self,vidas):

		portada = pygame.image.load('./img/logo.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Te han matado tienes '+str(vidas)+' vidas '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,300)
		pygame.display.flip()

	def InicioJuego(self):

		portada = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Inicia tu aventura espacial y repele el ataque alieniguena. '
		self.msn.MensajeSimple(txt, (255,0,0),16,120,300)
		txt2 = '[C] - Continuar'
		txt3 = '[Q] - Salir'
		self.msn.MensajeSimple(txt2, (68,14,14),13,90,350)
		self.msn.MensajeSimple(txt3, (68,14,14),13,90,380)

		pygame.display.flip()


	def FinPartida(self):

		portada = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 120)


		portadaGame = pygame.image.load('./img/gameover.png').convert_alpha()
		portadaGameRect = portadaGame.get_rect()
		portadaGameRect.center = (295, 200)

		txt = '[C] - Continuar'
		txt2 = '[Q] - Salir'
		self.msn.MensajeSimple(txt, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2, (255,0,0),13,90,380)

		self.screen.blit(portada,portadaGameRect)
		self.screen.blit(portadaGame,portadaRect)
		pygame.display.flip()



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
		self.imageVidas1 = pygame.image.load('./img/vida_1.png').convert_alpha()
		self.imageVidas2 = pygame.image.load('./img/vida_2.png').convert_alpha()

	def MensajeSimple(self, txt, color,tamFont,ancho,alto):
		font = pygame.font.SysFont("arial",tamFont)
		pantalla_texto = font.render(txt,True,color )
		self.screen.blit(pantalla_texto,(ancho,alto))


	def Cabecera(self,nd,pa,mu,vidas,puntuacion,nivel,cuentaLosEnemys):
		font = pygame.font.SysFont("arial",12)
		pygame.draw.rect(self.screen, (73,9,9), [0, 0, self.ANCHO, 35 ],0)
		pa = "{:.0f}".format(pa)
		pa = str(pa)

		muN = int(mu)
		mu = str(muN)
		txt = pa+'% '

		pygame.draw.rect(self.screen,(233,16,8), [15,20,100,10],0)
		pygame.draw.rect(self.screen,(6,161,4), [15,20,muN,10],0)

		for i in range(vidas):
			posix = 580-(20*i)

			self.rect = self.imageVidas1.get_rect()
			self.rect.center = (posix,15)
			self.screen.blit(self.imageVidas1,self.rect)


		# Cuenta Enemys
		imagenEnemys = pygame.image.load('./img/enemy_1_mini.png').convert_alpha()
		self.screen.blit(imagenEnemys,(250,4))
		txtene = str(cuentaLosEnemys)
		pantalla_textoenemis = font.render(txtene,True,(219,175,10) )
		self.screen.blit(pantalla_textoenemis,(275, 5))
		
		
		txtPuntos = 'Puntos: '+str(puntuacion)
		pantalla_textoPuntos = font.render(txtPuntos,True,(219,175,10) )
		self.screen.blit(pantalla_textoPuntos,(150, 4))

		txtPuntos = 'Nivel: '+str(nivel)
		pantalla_textoPuntos = font.render(txtPuntos,True,(219,175,10) )
		self.screen.blit(pantalla_textoPuntos,(150, 20))


		txt2 = 'Munición...'
		pantalla_texto2 = font.render(txt2,True,(102,150,109) )
		self.screen.blit(pantalla_texto2,(15, 4))

		txt3 = 'Efc.'
		pantalla_texto3 = font.render(txt3,True,(102,150,109) )
		self.screen.blit(pantalla_texto3,(120, 4))

		pantalla_texto = font.render(txt,True,(102,150,109) )
		self.screen.blit(pantalla_texto,(120, 20))

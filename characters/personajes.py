#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  personajes.py
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
import random


class Nave(pygame.sprite.Sprite):

	def __init__(self,Coorx,Coory):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('./img/nave_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (Coorx/2,Coory)

	def NaveMostrar(self):
		self.screen.blit(self.image,self.rect)

	def update(self):
		key = pygame.key.get_pressed()
		valores = self.rect
		upx = valores[0]+20
		upy = valores[1]+25


		if key[K_LEFT] and key[K_UP]:
			upx = upx-self.acelerador(key)
			upy = upy-self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_RIGHT] and key[K_UP]:
			upx = upx+self.acelerador(key)
			upy = upy-self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_RIGHT] and key[K_DOWN]:
			upx = upx+self.acelerador(key)
			upy = upy+self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_LEFT] and key[K_DOWN]:
			upx = upx-self.acelerador(key)
			upy = upy+self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_LEFT]:
			upx = upx-self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_RIGHT]:
			upx = upx+self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_UP]:
			upy -= self.acelerador(key)*2
			upx = upx
			self.IMGfogonazo()

		elif key[K_DOWN]:
			upy = upy+self.acelerador(key)*2
			upx = upx

		elif key[K_x]:
			if self.DataPuntos.get_municion() > 0:
				self.Disparo()
		else:
			self.NaveCambio('./img/nave_1.png')


		if upx>=ANCHO-25:
			upx = ANCHO-25

		if upy<=LIMIT_ALTO:
			upy = LIMIT_ALTO

		if upy>LINEA_INF:
			upy = LINEA_INF

		if upx<25:
			upx = 25

		self.rect.center = (upx, upy)

class Alien_1(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.x = random.randint(1, 600)
		self.y = random.randint(0, 430)

		self.image = pygame.image.load('./img/enemy_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)





	def update(self,TuNave):
		corde = self.rect
		coorTuNave = TuNave

		lax = corde[0]
		lay = corde[1]

		if lay >= 450:
			lax = random.randint(5, 550)
			lay = 0

		ale = random.randint(0,2)

		if coorTuNave[0]>lax:
			if ale == 0:
				lax = lax+self.speed

		if coorTuNave[0]<lax:
			if ale == 0:
				lax = lax-self.speed

		self.x = lax
		self.y = lay+1

		self.rect = (self.x,self.y)
		self.rect = (self.x,self.y)
		self.screen.blit(self.image,self.rect)

class LaserAlien(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('./img/laser_alien.png').convert_alpha()
		self.rect = self.image.get_rect()



class LaserNave(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('./img/laser.png').convert_alpha()
		self.rect = self.image.get_rect()






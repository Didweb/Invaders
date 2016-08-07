#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nave.py
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

ANCHO = 600
ALTO = 450
LINEA_INF = 420
LIMIT_ALTO = 25
VELOCIDAD = 5
VELOCIDAD_LASER = 15

import pygame, sys
from pygame.locals import *

class Nave(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/nave_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (ANCHO/2,LINEA_INF)
		self.speed = VELOCIDAD

	def update(self):
		key = pygame.key.get_pressed()
		valores = self.rect
		upx = valores[0]+20
		upy = valores[1]+25


		if key[K_LEFT] and key[K_UP]:
			upx = upx-self.acelerador(key)
			upy = upy-self.acelerador(key)

		elif key[K_RIGHT] and key[K_UP]:
			upx = upx+self.acelerador(key)
			upy = upy-self.acelerador(key)

		elif key[K_RIGHT] and key[K_DOWN]:
			upx = upx+self.acelerador(key)
			upy = upy+self.acelerador(key)

		elif key[K_LEFT] and key[K_DOWN]:
			upx = upx-self.acelerador(key)
			upy = upy+self.acelerador(key)

		elif key[K_LEFT]:
			upx = upx-self.acelerador(key)

		elif key[K_RIGHT]:
			upx = upx+self.acelerador(key)

		elif key[K_UP]:
			upy -= self.acelerador(key)*2
			upx = upx

		elif key[K_DOWN]:
			upy = upy+self.acelerador(key)*2
			upx = upx

		else:
			return False


		if upx>=ANCHO-25:
			upx = ANCHO-25

		if upy<=LIMIT_ALTO:
			upy = LIMIT_ALTO

		if upy>LINEA_INF:
			upy = LINEA_INF

		if upx<25:
			upx = 25

		self.rect.center = (upx, upy)



	def acelerador(self,key):
		aceleron = self.speed
		if key[K_a]:
				aceleron = VELOCIDAD*3

		return aceleron


class Laser(pygame.sprite.Sprite):
	def __init__(self,xl,yl):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/laser.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (xl,xl)
		self.speedLaser = VELOCIDAD_LASER
		self.laser_x = xl+18
		self.laser_y = yl+25

	def update(self):
		self.laser_y= self.laser_y-self.speedLaser

		if self.laser_x == 0:
			self.rect.kill()

		self.rect.center = (self.laser_x, self.laser_y)


class Player():
	def __init__(self):




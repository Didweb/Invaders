#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  enemy.py
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

import pygame, sys, os, math
from pygame.locals import *
import random

ANCHO = 600
ALTO = 450

VEL_ALIEN_1 = 5
VEL_SHOT_ALIEN_1 = 15



class Alien_1(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.valorPuntos = 10
		self.speed = VEL_ALIEN_1
		self.vivo = True



		self.x = random.randint(1, 600)
		self.y = random.randint(-600, 0)

		self.image = pygame.image.load('./img/enemy_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)





	def update(self,TuNave):

		corde = self.rect

		coorTuNave = TuNave.rect

		lax = corde[0]
		lay = corde[1]

		if lay >= 450:
			lax = random.randint(5, 550)
			lay = 0

		ale = random.randint(0,2)



		if coorTuNave[0]>lax:
			if ale == 0:
				lax = lax+2


		if coorTuNave[0]<lax:
			if ale == 0:
				lax = lax-2




		self.x = lax
		self.y = lay+1

		self.rect = (self.x,self.y)
		self.screen.blit(self.image,self.rect)














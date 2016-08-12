#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  municion.py
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

from .sujetos import (sujeto,PlaySujeto,load_img)

class BolaMunicion(pygame.sprite.Sprite):

	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen

		self.RectBM = {'anRect':24, 'alRect':24,'desX':0,'desY':0}

		self.imagenBM = [ pygame.image.load('./img/BM/1.png').convert_alpha(), \
					pygame.image.load('./img/BM/2.png').convert_alpha(), \
					pygame.image.load('./img/BM/3.png').convert_alpha(), \
					pygame.image.load('./img/BM/4.png').convert_alpha(), \
					pygame.image.load('./img/BM/4.png').convert_alpha(), \
					pygame.image.load('./img/BM/3.png').convert_alpha(), \
					pygame.image.load('./img/BM/2.png').convert_alpha(), \
					pygame.image.load('./img/BM/1.png').convert_alpha(), \
					]

		self.xBM = random.randint(1, 600)
		self.yBM = random.randint(-10, 0)


	def get_BMRect(self):
		self.BMRect = pygame.Rect(self.xBM - self.RectBM['desX'], \
									self.yBM - self.RectBM['desY'], \
									self.RectBM['anRect'], \
									self.RectBM['alRect'])
		return self.BMRect

	def pintaBM(self):

		self.bola = PlaySujeto(self.imagenBM,self.xBM,self.yBM )


	def newPosicionBM(self):
		self.xBM = random.randint(1, 600)
		self.yBM = random.randint(-10, 0)

	def updateBM(self):

		corde = self.bola.rect

		xbm = corde[0]
		ybm = corde[1]

		ybm += 1
		print ('BM: ',xbm,' ybm : ',ybm )
		self.bola.rect = (ybm,xbm)
		self.bola.update(self.screen)


		pygame.draw.rect(self.screen, (255,0,0), self.get_BMRect(), 3)

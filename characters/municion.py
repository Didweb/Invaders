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
		
		self.BMviva = False


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

		self.get_BMRect()
		
	def get_BMRect(self):
		self.BMRect = pygame.Rect(self.xBM - self.RectBM['desX'], \
									self.yBM - self.RectBM['desY'], \
									self.RectBM['anRect'], \
									self.RectBM['alRect'])
		return self.BMRect

	def update_BMRect(self,x,y):
		self.BMRect = pygame.Rect(x - self.RectBM['desX'], y - self.RectBM['desY'], self.RectBM['anRect'], self.RectBM['alRect'])
		return self.BMRect


	def pintaBM(self):
		self.get_BMRect()
		self.bola = PlaySujeto(self.imagenBM,self.xBM,self.yBM )


	def newPosicionBM(self):
		self.xBM = random.randint(1, 600)
		self.yBM = random.randint(-10, 0)



	def get_BMViva(self):
		return self.BMviva

	def set_BMViva(self,valor):
		self.BMviva=valor
		return self.BMviva


	def updateBM(self):

		corde = self.bola.rect

		xbm = self.xBM
		ybm = self.yBM

		if ybm < 450:
			ybm += 1
			
			
			self.xBM = xbm
			self.yBM = ybm
			self.bola.rect = (ybm,xbm)
			self.bola.update(self.screen)
			self.update_BMRect(xbm,ybm)
		
		else:
			self.newPosicionBM()
			self.set_BMViva(False)

		#pygame.draw.rect(self.screen, (255,255,0), self.get_BMRect(), 3)

	def AlcanzaMunicion(self,objeto):
		if self.BMRect.colliderect(objeto):
			return True
		else:
			return False

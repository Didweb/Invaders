#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sujetos.py
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

import pygame,os


def load_img(nombre, directorio):
	ruta = os.path.join(directorio, nombre)
	try:
		image = pygame.image.load(ruta)
	except:
		print('Error! Al cargar la imagen')
	return image.convert_alpha()



class sujeto(pygame.sprite.Sprite):

	def __init__(self, screen,  imagenes, laxyy):
		self.screen = screen
		self.imagenes = imagenes
		self.frame = 0
		self.indicador = 30
		self.rect = self.imagenes[self.frame].get_rect()
		#self.rect = laxyy

	def get_rectA(self):
		return self.rect

	def set_rect(self, corde):
		self.rect = corde
		return self.rect

	def move(self, vx, vy):
		#self.rect.move_ip(vx,vy)
		self.rect = (vx,vy)
	def update(self):
		self.screen.blit(self.imagenes[self.frame],self.rect)

	def nextFrame(self):
		self.frame = self.indicador % len(self.imagenes)
		self.indicador+=1

	def setNewSprites(self, imagenes):
		self.imagenes = imagenes








class Play(sujeto):

	def __init__(self, screen, imagenes,laxyy):
		sujeto.__init__(self, screen, imagenes,laxyy)
	def getLife():
		return self.life


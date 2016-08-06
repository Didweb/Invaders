#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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

ANCHO = 600
ALTO = 450
LINEA_INF = 420
LIMIT_ALTO = 25
VELOCIDAD = 5

class Nave(pygame.sprite.Sprite):
	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('nave_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (ANCHO/2,LINEA_INF)
		self.speed = VELOCIDAD

	def update(self):
		key = pygame.key.get_pressed()
		valores = self.rect
		upx = valores[0]+25
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
			print(upy,'<',LINEA_INF-25)

		if upx<25:
			upx = 25

		self.rect.center = (upx, upy)



	def acelerador(self,key):

		aceleron = self.speed
		if key[K_a]:
				aceleron = VELOCIDAD*3

		return aceleron





def main():

	pygame.init()
	screen = pygame.display.set_mode((ANCHO,ALTO))
	pygame.display.set_caption('Invaders 1')
	reloj = pygame.time.Clock()

	tanque = Nave()
	#screen.blit(tanque.image, tanque.rect)
	colorBG = (0,0,0)

	clock = pygame.time.Clock()

	jugar = True
	while jugar:



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				juagr = False
				pygame.quit()
				sys.exit()






		screen.fill(colorBG)
		screen.blit(tanque.image, tanque.rect)
		pygame.display.flip()
		clock.tick(24)
		tanque.update()
	pygame.quit()

if __name__ == '__main__':
	main()


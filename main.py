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

from characters.nave import (Nave,Laser)


ANCHO = 600
ALTO = 450




def main():

	pygame.init()
	screen = pygame.display.set_mode((ANCHO,ALTO))
	pygame.display.set_caption('Invaders 1')
	reloj = pygame.time.Clock()

	tanque = Nave()
	#screen.blit(tanque.image, tanque.rect)
	colorBG = (0,0,0)

	clock = pygame.time.Clock()

	disparoActivo = False
	disparoActivo2 = False
	disparoActivo3 = False
	disparoActivo4 = False
	disparoActivo5 = False
	pasodisparo1 = False
	pasodisparo2 = False
	pasodisparo3 = False
	pasodisparo4 = False
	jugar = True
	disparos = {}
	nDisparos = 0
	while jugar:



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				juagr = False
				pygame.quit()
				sys.exit()

			key = pygame.key.get_pressed()

			if key[K_x]:
				if disparoActivo == False:
					disparoActivo = True
					nDisparos += 1
					las = Laser(tanque.rect.x,tanque.rect.y)
					las.update()


				if disparoActivo2 == False and pasodisparo1 == True:
					disparoActivo2 = True
					nDisparos += 1
					las2 = Laser(tanque.rect.x,tanque.rect.y)
					las2.update()

				if disparoActivo3 == False and pasodisparo2 == True:
					disparoActivo3 = True
					nDisparos += 1
					las3 = Laser(tanque.rect.x,tanque.rect.y)
					las3.update()

				if disparoActivo4 == False and pasodisparo3 == True:
					disparoActivo4 = True
					nDisparos += 1
					las4 = Laser(tanque.rect.x,tanque.rect.y)
					las4.update()

				if disparoActivo5 == False and pasodisparo4 == True:
					disparoActivo5 = True
					nDisparos += 1
					las5 = Laser(tanque.rect.x,tanque.rect.y)
					las5.update()

		screen.fill(colorBG)
		screen.blit(tanque.image, tanque.rect)


		if disparoActivo:
			las.update()
			screen.blit(las.image, las.rect)
			print ('Laser 1: ',las.laser_y)
			pasodisparo1 = True
			if las.laser_y <= 0:
				disparoActivo = False
				pasodisparo1 = False
				las.kill()

		if disparoActivo2:
			las2.update()
			screen.blit(las2.image, las2.rect)
			print ('Laser 2: ',las2.laser_y)
			pasodisparo2 = True
			if las2.laser_y <= 0:
				disparoActivo2 = False
				pasodisparo2 = False
				las2.kill()

		if disparoActivo3:
			las3.update()
			screen.blit(las3.image, las3.rect)
			print ('Laser 3: ',las3.laser_y)
			pasodisparo3 = True
			if las3.laser_y <= 0:
				disparoActivo3 = False
				pasodisparo3 = False
				las3.kill()

		if disparoActivo4:
			las4.update()
			screen.blit(las4.image, las4.rect)
			print ('Laser 4: ',las4.laser_y)
			pasodisparo4 = True
			if las4.laser_y <= 0:
				disparoActivo4 = False
				pasodisparo4 = False
				las4.kill()

		if disparoActivo5:
			las5.update()
			screen.blit(las5.image, las5.rect)
			print ('Laser 5: ',las5.laser_y)
			if las5.laser_y <= 0:
				disparoActivo5 = False
				las5.kill()

		pygame.display.flip()
		clock.tick(24)
		tanque.update()


	pygame.quit()

if __name__ == '__main__':
	main()


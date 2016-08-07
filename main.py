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

from characters.nave import (Nave,Laser,Player)
from annex.puntuaciones import (Puntos)

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

	jugar = True
	disparoActivoD = {1:False, 2:False, 3:False, 4:False, 5:False,6:False, 7:False, 8:False}
	pasoDisparoD = {1:False, 2:False, 3:False, 4:False, 5:False,6:False, 7:False, 8:False}
	lasersActivosD = {}

	DataPuntos = Puntos()
	Jugador = Player(screen)

	while jugar:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				juagr = False
				pygame.quit()
				sys.exit()

		# Prepara el disparo apretando el gatillo
		Jugador.Gatillo(DataPuntos,tanque.rect.x,tanque.rect.y)

		# el fondo y la nave
		screen.fill(colorBG)
		screen.blit(tanque.image, tanque.rect)

		# Saca disparo y controla su vida
		Jugador.Dispara()

		pygame.display.flip()
		clock.tick(30)
		tanque.update()


	pygame.quit()

if __name__ == '__main__':
	main()


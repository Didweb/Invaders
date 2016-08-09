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
from Niveles import (ServNiveles)
from annex.mensajes import (Mensajes)

from annex.mensajes import (Mensajes)
ANCHO = 600
ALTO = 450









def main():

	pygame.init()
	screen = pygame.display.set_mode((ANCHO,ALTO))
	pygame.display.set_caption('Invaders 1')
	reloj = pygame.time.Clock()

	msn = Mensajes(screen,(ANCHO,ALTO))


	colorBG = (0,0,0)
	Nivel = 1
	clock = pygame.time.Clock()

	Op_menu = True
	Op_jugar = True





	SJ = ServNiveles(Nivel,screen,(ANCHO,ALTO),msn)


	while Op_jugar:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Op_jugar = False
				pygame.quit()
				sys.exit()


		if SJ.SJnivel == 1:
			SJ.Nivel_1()




		clock.tick(50)

	pygame.quit()









if __name__ == '__main__':
	main()


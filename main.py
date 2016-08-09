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
from annex.puntuaciones import (Puntos)
from characters.nave import (Nave)
from characters.enemy import (Alien_1)
from annex.mensajes import (Mensajes)
from annex.control import (Niveles)

ANCHO = 600
ALTO = 450




jugar = True



def main():

	pygame.init()
	screen = pygame.display.set_mode((ANCHO,ALTO))
	pygame.display.set_caption('Invaders 1')
	clock = pygame.time.Clock()
	msn = Mensajes(screen,(ANCHO,ALTO))
	DataPuntos = Puntos()


	DataPuntos.PorcentajeMunicion()
	vidas = DataPuntos.Vidas

	Tanque = Nave(screen,DataPuntos)
	PosInicioNave = Tanque.PosicionInicio()

	EnemysNivel1 = 10
	EnemysPeloton = {}
	for x in range(0,EnemysNivel1):
		EnemysPeloton[x] = Alien_1(screen)


	#screen.blit(tanque.image, tanque.rect)
	colorBG = (0,0,0)

	ControlJuego = Niveles()




	while jugar:

		if ControlJuego.get_Nivel() == 1:
			EnemysNivel1 = 10
		else:
			print('Niveles no seleccionado')


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Op_jugar = False
				pygame.quit()
				sys.exit()



		screen.fill((0,0,0))

		Tanque.NaveMostrar()
		Tanque.update()

		for ep in range(EnemysNivel1):
			Enemigos = EnemysPeloton[ep]
			Enemigos.update(Tanque)
			Enemigos.DisparoEnemy()
			Enemigos.updateDisparosEnemy()

		Tanque.Disparo()
		Tanque.updateDisparos()



		# cabecera
		msn.Cabecera( DataPuntos.nDisparos, \
						DataPuntos.PorAciertos, \
						DataPuntos.Por_Municion, \
						vidas)

		pygame.display.flip()
		clock.tick(50)


	pygame.quit()






if __name__ == '__main__':
	main()


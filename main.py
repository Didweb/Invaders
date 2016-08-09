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
from annex.control import (Niveles,GestorAvisos)

ANCHO = 600 #600
ALTO = 400 #400
N_VIDAS = 2







def main():

	pygame.init()
	screen = pygame.display.set_mode((ANCHO,ALTO))
	pygame.display.set_caption('Invaders 1')
	clock = pygame.time.Clock()
	msn = Mensajes(screen,(ANCHO,ALTO),N_VIDAS)
	DataPuntos = Puntos(N_VIDAS)


	DataPuntos.PorcentajeMunicion()
	vidas = DataPuntos.get_Vidas()

	Tanque = Nave(screen,DataPuntos)
	PosInicioNave = Tanque.PosicionInicio()

	EnemysNivel1 = 10
	EnemysPeloton = {}
	for x in range(0,EnemysNivel1):
		EnemysPeloton[x] = Alien_1(screen)

	GestAvisos = GestorAvisos(msn)

	#screen.blit(tanque.image, tanque.rect)
	colorBG = (0,0,0)

	ControlJuego = Niveles()

	jugar = True
	avisos = False
	menu = True



	def avisosLoop(avisos):

		while avisos:

			screen.fill((0,0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Op_jugar = False
					pygame.quit()
					sys.exit()

				key = pygame.key.get_pressed()

				if key[K_c] :
					jugar = True
					avisos = False
					jugarLoop(jugar)

			GestAvisos.AvisoMuerte(DataPuntos.get_Vidas())

			for x in range(0,EnemysNivel1):
				EnemysPeloton[x] = Alien_1(screen)
			Tanque.resetNave()
			pygame.display.flip()



	def menuLoop(menu):
		txtGO = ''
		v = ''
		while menu:
			screen.fill((0,0,0))

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Op_jugar = False
					pygame.quit()
					sys.exit()

				key = pygame.key.get_pressed()

				if key[K_c] :
					jugar = True
					avisos = False
					jugarLoop(jugar)




			if DataPuntos.get_Vidas() == 0:
				print('GAME OVER')
				txtGO = ' --> GAME OVER <-- '
			else:
				v = 'Tienes: '+str(DataPuntos.get_Vidas())+' vidas. '

			msn.MensajeSimple(v+' '+txtGO+' [C]: Continuar',(255,0,0),20,40,60)

			for x in range(0,EnemysNivel1):
				EnemysPeloton[x] = Alien_1(screen)

			Tanque.resetNave()
			DataPuntos.Vidas = N_VIDAS
			pygame.display.flip()




	def jugarLoop(jugar):

		while jugar:

			if ControlJuego.get_Nivel() == 1:
				EnemysNivel1 = 10



			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Op_jugar = False
					pygame.quit()
					sys.exit()




			screen.fill((0,0,0))

			Tanque.NaveMostrar()
			Tanque.update()
			Tanque.Disparo()
			Tanque.updateDisparos()
			ncambio = 0
			for ep in range(EnemysNivel1):
				Enemigos = EnemysPeloton[ep]


				Enemigos.update(Tanque)
				Enemigos.DisparoEnemy()
				Enemigos.updateDisparosEnemy()

				# Mirar si me han dado
				MeHanDado = Enemigos.mirarAciertosAliens(Tanque.get_naveRect())
				if MeHanDado == True:
					DataPuntos.set_VidasMuerto()
					menu = True
					jugar = False
					avisos = False
					menuLoop(menu)

				#Tanque.ColisionEnemy(Enemigos)

				# Hemos Chocado con un Alien
				if Enemigos.get_alienRect().colliderect(Tanque.get_naveRect()):
					DataPuntos.set_VidasMuerto()

					if DataPuntos.get_Vidas()<=0:
						if DataPuntos.get_Vidas()<0:
							DataPuntos.Vidas = 0
						menu = True
						jugar = False
						avisos = False
						menuLoop(menu)
					else:
						jugar = False
						avisos = True
						menu = False
						avisosLoop(avisos)

					MirarSiAcertamos = Tanque.mirarDiana(Enemigos.get_alienRect())
					if MirarSiAcertamos == True:
						ncambio +=1





			#if ncambio > 0:
				#EnemysNivel1 = EnemysNivel1-ncambio
				#del EnemysPeloton[ep]

			print ('ncambio = ',ncambio)











			# cabecera
			msn.Cabecera( DataPuntos.nDisparos, \
							DataPuntos.PorAciertos, \
							DataPuntos.Por_Municion, \
							DataPuntos.get_Vidas())

			pygame.display.flip()
			clock.tick(50)

	menuLoop(jugar)











if __name__ == '__main__':
	main()
	#pygame.quit()


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

from annex.mensajes import (Mensajes)
from annex.control import (Niveles,GestorAvisos)

ANCHO = 600 #600
ALTO = 450 #450








class main():
	def __init__(self):
		self.jugar = False
		self.gameover = False
		self.dado = False
		self.menu = True
		self.primerapartida = True
		self.superado = False





		pygame.init()
		self.screen = pygame.display.set_mode((ANCHO,ALTO))
		pygame.display.set_caption('Invaders 1')
		self.clock = pygame.time.Clock()
		self.msn = Mensajes(self.screen,(ANCHO,ALTO))



		self.DataPuntos = Puntos()
		self.DataPuntos.PorcentajeMunicion()
		self.ControlJuego = Niveles(self.screen,self.DataPuntos)


		self.GestAvisos = GestorAvisos(self.msn,self.screen)

		self.aniquilados = 0



		self.menuLoop(self.menu)





	def menuLoop(self,menu):



		while menu:
			self.screen.fill((0,0,0))




			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.menu = False
					pygame.quit()
					sys.exit()

				key = pygame.key.get_pressed()

				if key[K_q] :
					self.menu = False
					pygame.quit()
					sys.exit()

				if key[K_c] :
					self.jugar = True
					self.menu = False
					self.jugarLoop(self.jugar)



			if self.gameover == True:
				self.DataPuntos.reset_puntos()
				self.DataPuntos.CargarMunicion(self.DataPuntos.PacksMunicion)
				self.GestAvisos.FinPartida()
				self.DataPuntos.Vidas = self.DataPuntos.reset_vidas()

			elif self.primerapartida == True:
				self.DataPuntos.reset_puntos()
				self.GestAvisos.InicioJuego()
				self.DataPuntos.Vidas = self.DataPuntos.reset_vidas()

			elif self.dado == True:
				self.DataPuntos.CargarMunicion(self.DataPuntos.PacksMunicion)
				self.GestAvisos.AvisoMuerte(self.DataPuntos.get_Vidas())

			elif self.superado == True:
				self.DataPuntos.CargarMunicion(self.DataPuntos.PacksMunicion)
				self.GestAvisos.NivelSuperado(self.DataPuntos.get_Puntuacion(),self.ControlJuego.get_Nivel())
				self.DataPuntos.Vidas = self.DataPuntos.get_vidas()
				print('Superado')

				self.ControlJuego.set_Nivel(self.nextNivel)

				self.EnemysNivel1 = self.ControlJuego.get_EnemysN1()









	def jugarLoop(self,jugar):

		self.gameover = False
		self.dado = False
		self.menu = False
		self.primerapartida = False
		self.superado = False


		self.ControlJuego.SetsNivel(self.ControlJuego.get_Nivel())

		while jugar:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.jugar = False
					pygame.quit()
					sys.exit()

			self.screen.fill((0,0,0))


			self.ControlJuego.MountNivel()





			"""
			ncambio = 0
			for ep in range(self.EnemysNivel1):
				self.Enemigos = self.EnemysPeloton[ep]

				if self.Enemigos != False:
					self.Enemigos.update(self.Tanque)
					self.Enemigos.DisparoEnemy()
					self.Enemigos.updateDisparosEnemy()

					# Mirar si me han dado
					MeHanDado = self.Enemigos.mirarAciertosAliens(self.Tanque.get_naveRect())
					if MeHanDado == True:

						self.DataPuntos.set_VidasMuerto()

						if self.DataPuntos.get_Vidas()<=0:
							self.gameover = True
							self.dado = False
							self.menu = True
							self.primerapartida = False
							self.jugar = False
							self.menuLoop(self.menu)

						else:
							self.gameover = False
							self.dado = True
							self.menu = True
							self.primerapartida = False
							self.jugar = False
							self.menuLoop(self.menu)







					#Tanque.ColisionEnemy(Enemigos)

					# Hemos Chocado con un Alien
					if self.Enemigos.get_alienRect().colliderect(self.Tanque.get_naveRect()):
						self.DataPuntos.set_VidasMuerto()

						if self.DataPuntos.get_Vidas()<=0:
							self.gameover = True
							self.dado = False
							self.menu = True
							self.primerapartida = False
							self.jugar = False
							self.menuLoop(self.menu)

						else:

							self.gameover = False
							self.dado = True
							self.menu = True
							self.primerapartida = False
							self.jugar = False
							self.menuLoop(self.menu)





					MirarSiAcertamos = self.Tanque.mirarDiana(self.Enemigos.get_alienRect())
					if MirarSiAcertamos == True:
						#print ('DADO',ep)
						self.EnemysPeloton[ep] = False
						self.DataPuntos.AumentarPuntos(self.Enemigos.valorPuntos)
						self.nextNivel = self.ControlJuego.get_Nivel()+1
						self.aniquilados += 1
						self.DataPuntos.AumentaAciertos()
						ncambio +=1


			self.Tanque.NaveMostrar()
			self.Tanque.update()
			self.Tanque.Disparo()
			self.Tanque.updateDisparos()

			print (self.aniquilados,'==',self.EnemysNivel1)
			if self.aniquilados == self.EnemysNivel1:
				self.aniquilados = 0
				self.superado = True
				self.menu = True
				self.menuLoop(self.menu)



			#if ncambio > 0:
				#EnemysNivel1 = EnemysNivel1-ncambio
				#del EnemysPeloton[ep]


			"""






			print (self.DataPuntos.Por_Municion)



			# cabecera
			self.msn.Cabecera( self.DataPuntos.nDisparos, \
							self.DataPuntos.PorAciertos, \
							self.DataPuntos.Por_Municion, \
							self.DataPuntos.get_Vidas(), \
							self.DataPuntos.get_Puntuacion(),
							self.ControlJuego.get_Nivel())

			pygame.display.flip()
			self.clock.tick(25)















if __name__ == '__main__':
	main()
	#pygame.quit()

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
		pygame.display.set_caption(' .- RasInvaders -. ')
		self.clock = pygame.time.Clock()
		self.msn = Mensajes(self.screen,(ANCHO,ALTO))



		self.DataPuntos = Puntos()
		self.DataPuntos.PorcentajeMunicion()
		self.ControlJuego = Niveles(self.screen,self.DataPuntos)
		self.ControlJuego.get_Nivel()

		self.GestAvisos = GestorAvisos(self.msn,self.screen,self.DataPuntos)





		self.menuLoop(self.menu)





	def menuLoop(self,menu):



		if self.superado == True:
			self.DataPuntos.NivelSuperado()
			self.puntos_ante = self.DataPuntos.get_Puntuacion()
			self.DataPuntos.calculoNivelOk()

		if self.primerapartida == True:
			self.ControlJuego.get_Nivel()
			
		if self.gameover == True:
			self.Nivelpasado = self.DataPuntos.get_NivelP()
			self.Puntospasados = self.DataPuntos.get_Puntuacion()

		

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
				self.gameover = False
				self.primerapartida = False
				self.dado = False
				self.superado = False
				self.jugarLoop(True)

			if key[K_n] :
				self.jugar = True
				self.menu = False
				self.gameover = False
				self.primerapartida = False
				self.dado = False
				self.superado = False
				self.DataPuntos.reset_Nivel()
				self.ControlJuego.get_Nivel()
				self.DataPuntos.reset_puntos()
				self.DataPuntos.set_municion()
				
				self.jugarLoop(True)

			if self.gameover == True:
				self.GestAvisos.FinPartida(self.Puntospasados,self.Nivelpasado)

				self.DataPuntos.Vidas = self.DataPuntos.reset_vidas()

			elif self.primerapartida == True:
				self.DataPuntos.reset_puntos()
				self.GestAvisos.InicioJuego()
				self.DataPuntos.Vidas = self.DataPuntos.reset_vidas()
				self.ControlJuego.get_Nivel()

			elif self.dado == True:
				
				self.GestAvisos.AvisoMuerte(self.DataPuntos.get_Vidas())
				self.jugar = True

			elif self.superado == True:
				
				datosPunts = [self.puntos_ante, \
								self.DataPuntos.get_PorAciertos(),\
								self.DataPuntos.get_Puntuacion()]
								
				self.GestAvisos.NivelSuperado(datosPunts,self.DataPuntos.get_NivelP())
				self.DataPuntos.Vidas = self.DataPuntos.get_vidas()







			pygame.display.flip()
			









	def jugarLoop(self,jugar):

		self.gameover = False
		self.dado = False
		self.menu = False
		self.primerapartida = False
		self.superado = False
		self.jugar = True
		
		self.ControlJuego.SetsNivel()

		
		
		while jugar:
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.jugar = False
					pygame.quit()
					sys.exit()

			self.screen.fill((0,0,0))

			
			self.ControlJuego.MountNivel()
			estat = self.ControlJuego.EstadoActual()


			self.dado = estat['dado']
			self.gameover = estat['gameover']
			self.menu = estat['menu']
			self.primerapartida = estat['primerapartida']
			self.superado = estat['superado']
			self.jugar = estat['jugar']


			

			if self.jugar == False:
				self.menuLoop(True)





			# cabecera
			self.msn.Cabecera( self.DataPuntos.nDisparos, \
							self.DataPuntos.PorAciertos, \
							self.DataPuntos.Por_Municion, \
							self.DataPuntos.get_Vidas(), \
							self.DataPuntos.get_Puntuacion(),
							self.DataPuntos.get_NivelP())

			pygame.display.flip()
			self.clock.tick(40)















if __name__ == '__main__':
	main()
	pygame.quit()


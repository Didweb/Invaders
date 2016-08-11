#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  control.py
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


from characters.nave import (Nave)
from characters.enemy import (AlienMosca)

import pygame, sys
from pygame.locals import *

class Niveles:
	def __init__(self,screen, DataPuntos):
		self.Nivel = 1
		self.n_Enemys = 0
		self.screen = screen
		self.DataPuntos = DataPuntos
		self.jugar = True



	def get_Nivel(self):
		return self.Nivel

	def set_Nivel(self, newNivel):
		self.Nivel = newNivel
		return self.Nivel

	def get_EnemysN1(self):
		return self.EnemysN1


	def SetsNivel(self,nivel):
		self.n_Enemys =  {1: (100,0,0)}
		self.Nivel = nivel
		self.Tanque = Nave(self.screen,self.DataPuntos)

		self.Pelotones = {}
		# 3 tipos de enemigos posibles por nivel
		for xx in range(0,2):

			# Montamos los diccionarios con cada peloton de enemigos
			for x in range(0,self.n_Enemys[self.Nivel][xx]):
				if self.n_Enemys[self.Nivel][xx] > 0:

					if self.Nivel == 1:
						alienMosca = AlienMosca(self.screen)
						self.Pelotones[x] = {'bicho':alienMosca,'estado':True}






	def MountNivel(self):


		nPelo = len(self.Pelotones)
		for ep in range(nPelo):
				self.Enemigos = self.Pelotones[ep]['bicho']
				if self.Pelotones[ep]['estado'] == True:
					self.Enemigos.pintar()
					self.Enemigos.pasitos(self.Tanque)#self.Enemigos.update(self.Tanque)
					self.Enemigos.DisparoEnemy()
					print('ep en true: ',ep)
				else:
					print('ep en explo: ',ep)

					self.Enemigos.exploUpdate()

				self.Enemigos.updateDisparosEnemy()

				# Mirar si acertamos a un enemigo
				MirarSiAcertamos = self.Tanque.mirarDiana(self.Enemigos.get_alienRect())
				if MirarSiAcertamos == True:

					self.Enemigos.muerto()
					self.Pelotones[ep]['estado'] = False
					self.DataPuntos.AumentarPuntos(self.Enemigos.valorPuntos)

					self.DataPuntos.AumentaAciertos()


				# Hemos Chocado con un Alien
				if self.Enemigos.get_alienRect().colliderect(self.Tanque.get_naveRect()):
					self.DataPuntos.set_VidasMuerto()
					print('++++++++++++++++++++++++++++++++++++++++++++++++++++')
					self.Enemigos.muerto()
					self.Enemigos.exploUpdate()
					if self.DataPuntos.get_Vidas()<=0:
						self.gameover = True
						self.dado = False
						self.menu = True
						self.primerapartida = False
						self.jugar = False


					else:

						self.gameover = False
						self.dado = True
						self.menu = True
						self.primerapartida = False
						self.jugar = False

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


					else:
						self.gameover = False
						self.dado = True
						self.menu = True
						self.primerapartida = False
						self.jugar = False



		self.Tanque.NaveMostrar()
		self.Tanque.update()
		self.Tanque.Disparo()
		self.Tanque.updateDisparos()


	def EstadoActual(self):
		return self.jugar

class GestorAvisos:
	def __init__(self,msn,screen):
		self.msn = msn
		self.screen = screen


	def NivelSuperado(self,puntos,nivel):


		portada = pygame.image.load('./img/logo.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Superado el Nivel '+str(nivel)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,300)
		txt = 'Puntos '+str(puntos)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,330)
		pygame.display.flip()


	def AvisoMuerte(self,vidas):

		portada = pygame.image.load('./img/logo.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Te han matado tienes '+str(vidas)+' vidas '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,300)
		pygame.display.flip()

	def InicioJuego(self):

		portada = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Inicia tu aventura espacial y repele el ataque alieniguena. '
		self.msn.MensajeSimple(txt, (255,0,0),16,120,300)
		txt2 = '[C] - Continuar'
		txt3 = '[Q] - Salir'
		self.msn.MensajeSimple(txt2, (68,14,14),13,90,350)
		self.msn.MensajeSimple(txt3, (68,14,14),13,90,380)

		pygame.display.flip()


	def FinPartida(self):

		portada = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 120)


		portadaGame = pygame.image.load('./img/gameover.png').convert_alpha()
		portadaGameRect = portadaGame.get_rect()
		portadaGameRect.center = (295, 200)

		txt = '[C] - Continuar'
		txt2 = '[Q] - Salir'
		self.msn.MensajeSimple(txt, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2, (255,0,0),13,90,380)

		self.screen.blit(portada,portadaGameRect)
		self.screen.blit(portadaGame,portadaRect)
		pygame.display.flip()



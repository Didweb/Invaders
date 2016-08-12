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
from characters.municion import (BolaMunicion)

import pygame, sys
from pygame.locals import *

class Niveles:
	def __init__(self,screen, DataPuntos):
		self.Nivel = 1
		self.n_Enemys = 0
		self.screen = screen
		self.DataPuntos = DataPuntos
		self.jugar = True

		self.n_Enemy_auto = 1



	def get_Nivel(self):
		return self.Nivel

	def set_Nivel(self, newNivel):
		self.Nivel = newNivel
		return self.Nivel

	def get_EnemysN1(self):
		return self.EnemysN1


	def SetsNivel(self,nivel):
		self.jugar = True
		self.n_Enemys =  {1: (2,0,0), 2:(2,0,0), 3:(3,0,0)}
		self.Nivel = nivel
		self.Tanque = Nave(self.screen,self.DataPuntos)

		self.Pelotones = {}


		# Si no tenemos preparados los proximos niveles se montan
		# segun ultima configuracion
		print (len(self.n_Enemys),'>=',self.Nivel)
		if len(self.n_Enemys)>self.Nivel:
			elnivel = self.Nivel


		else:
			elnivel = len(self.n_Enemys)
			if self.superado == True:
				self.n_Enemy_auto += 1


		# 3 tipos de enemigos posibles por nivel
		for xx in range(0,2):

			# Montamos los diccionarios con cada peloton de enemigos


			for x in range(0,self.n_Enemys[elnivel][xx]*self.n_Enemy_auto):
				if self.n_Enemys[elnivel][xx] > 0:

					if self.Nivel == 1:
						alienMosca = AlienMosca(self.screen)
						self.Pelotones[x] = {'bicho':alienMosca,'estado':True}
					elif self.Nivel > 1:
						alienMosca = AlienMosca(self.screen)
						self.Pelotones[x] = {'bicho':alienMosca,'estado':True}


		self.gameover = False
		self.dado = False
		self.menu = False
		self.primerapartida = False
		self.superado = False
		self.jugar = True
		self.alcanzado = False
		self.loopExploNave = 0

		self.bolaM = BolaMunicion(self.screen)
		self.bolaM.pintaBM()




	def MountNivel(self):


		nPelo = len(self.Pelotones)
		cuentaMuertos = 0


		self.bolaM.updateBM()
		self.bolaM.bola.nextFrame()
		#For donde monta Pelotones de enemigos y control de sucesos



		for ep in range(nPelo):
			print ('Ep = ',ep)
			self.Enemigos = self.Pelotones[ep]['bicho']
			if self.Pelotones[ep]['estado'] == True:
				self.Enemigos.pintar()
				self.Enemigos.pasitos(self.Tanque)
				self.Enemigos.DisparoEnemy()

			else:
				cuentaMuertos += 1

				self.Enemigos.exploUpdate()

			self.Enemigos.updateDisparosEnemy()

			# Mirar si acertamos a un enemigo
			MirarSiAcertamos = self.Tanque.mirarDiana(self.Enemigos.get_alienRect())
			if MirarSiAcertamos == True:

				self.Enemigos.muerto()
				self.Pelotones[ep]['estado'] = False

				# Gestion de puntos
				self.DataPuntos.AumentarPuntos(self.Enemigos.valorPuntos)
				self.DataPuntos.AumentaAciertos()



			# Hemos Chocado con un Alien
			if self.Enemigos.get_alienRect().colliderect(self.Tanque.get_naveRect()):
				self.DataPuntos.set_VidasMuerto()
				self.Enemigos.muerto()
				self.alcanzado = True
				self.Tanque.explosion()


			# Mirar si me han dado
			MeHanDado = self.Enemigos.mirarAciertosAliens(self.Tanque.get_naveRect())
			if MeHanDado == True:
				self.DataPuntos.set_VidasMuerto()
				self.alcanzado = True
				self.Tanque.explosion()






		print (cuentaMuertos,'==',nPelo)
		if cuentaMuertos == nPelo:
			self.superado = True
			self.jugar = False
			self.menu = True

		if self.alcanzado==True:

			#while self.Tanque.explo.indicador<40:
			if self.loopExploNave<40:
				self.Tanque.exploUpdate()
				self.loopExploNave +=1
			else:
				if self.DataPuntos.get_Vidas()<=0:
					self.gameover = True
					self.menu = True
					self.jugar = False
					self.n_Enemy_auto = 0


				else:
					self.dado = True
					self.menu = True
					self.jugar = False
		else:
			self.Tanque.NaveMostrar()
			self.Tanque.update()
			self.Tanque.Disparo()
			self.Tanque.updateDisparos()


	def EstadoActual(self):
		estados = {'jugar':self.jugar, \
					'gameover':self.gameover, \
					'dado':self.dado, \
					'menu':self.menu, \
					'primerapartida':self.primerapartida, \
					'superado': self.superado }
		return estados

class GestorAvisos:
	def __init__(self,msn,screen):
		self.msn = msn
		self.screen = screen


	def NivelSuperado(self,puntos,nivel):


		portada = pygame.image.load('./img/logo_superado.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 200)
		self.screen.blit(portada,portadaRect)

		txt = 'Superado el Nivel '+str(nivel)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,300)
		txt = 'Puntos '+str(puntos)+'  '
		self.msn.MensajeSimple(txt, (255,0,0),13,60,330)
		pygame.display.flip()


	def AvisoMuerte(self,vidas):

		portada = pygame.image.load('./img/logo_alcanzado.png').convert_alpha()
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
		self.msn.MensajeSimple(txt2, (193,21,21),13,90,350)
		self.msn.MensajeSimple(txt3, (193,21,21),13,90,380)

		pygame.display.flip()


	def FinPartida(self):

		portada = pygame.image.load('./img/gameover.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 120)


		portadaGame = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaGameRect = portadaGame.get_rect()
		portadaGameRect.center = (315, 270)

		txt = '[C] - Continuar'
		txt2 = '[Q] - Salir'
		self.msn.MensajeSimple(txt, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2, (255,0,0),13,90,380)

		self.screen.blit(portada,portadaGameRect)
		self.screen.blit(portadaGame,portadaRect)
		pygame.display.flip()



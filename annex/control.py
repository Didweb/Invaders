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
import random
import pygame, sys
from pygame.locals import *

class Niveles:
	def __init__(self,screen, DataPuntos):
		
		self.n_Enemys = 0
		self.screen = screen
		self.DataPuntos = DataPuntos
		self.Nivel = self.DataPuntos.get_NivelP()
		self.jugar = True

		self.n_Enemy_auto = 1



	def get_Nivel(self):
		self.Nivel = self.DataPuntos.get_NivelP()
		return self.Nivel



	def get_EnemysN1(self):
		return self.EnemysN1


	def SetsNivel(self):
		self.jugar = True
		self.n_Enemys =  {1: (5,0,0), 2:(8,0,0), 3:(10,0,0)}
		self.Nivel = self.DataPuntos.get_NivelP()
		self.Tanque = Nave(self.screen,self.DataPuntos)

		self.Pelotones = {}


		# Si no tenemos preparados los proximos niveles se montan
		# segun ultima configuracion
		if len(self.n_Enemys)>self.Nivel:
			elnivel = self.Nivel


		else:
			elnivel = len(self.n_Enemys)
			if self.superado == True:
				self.n_Enemy_auto += 1


		# 3 tipos de enemigos posibles por nivel
		for xx in range(0,3):
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
		
		self.nPelo = len(self.Pelotones)


	def MountNivel(self):

		self.cuentaMuertos = 0
		#For donde monta Pelotones de enemigos y control de sucesos

		
		for ep in range(self.nPelo):
			self.Enemigos = self.Pelotones[ep]['bicho']
			if self.Pelotones[ep]['estado'] == True:
				self.Enemigos.pintar()
				self.Enemigos.pasitos(self.Tanque)
				self.Enemigos.DisparoEnemy()

			else:
				self.cuentaMuertos += 1
				

				self.Enemigos.exploUpdate()

			self.Enemigos.updateDisparosEnemy()

			# Mirar si acertamos a un enemigo
			MirarSiAcertamos = self.Tanque.mirarDiana(self.Enemigos.get_alienRect())
			if MirarSiAcertamos == True:
				
				# Gestion de puntos
				if self.Pelotones[ep]['estado'] == True:
					self.DataPuntos.AumentarPuntos(self.Enemigos.valorPuntos)
					self.DataPuntos.AumentaAciertos()

				self.Enemigos.muerto()
				self.Pelotones[ep]['estado'] = False

				



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

			
			
		
		if self.cuentaMuertos >= self.nPelo:
			self.superado = True
			self.jugar = False
			self.menu = True
		else:
			self.superado = False




		


		if self.alcanzado==True:

			if self.loopExploNave<40:
				self.Tanque.exploUpdate()
				self.loopExploNave +=1
			else:
				if self.DataPuntos.get_Vidas()<=0:
					self.gameover = True
					self.menu = True
					self.jugar = False
					self.superado = False
					self.n_Enemy_auto = 1


				else:
					self.dado = True
					self.menu = True
					self.jugar = False
					self.superado = False
		else:
			
			# Servimos municion extra
			
			if self.DataPuntos.get_PorMuncion()<45:
				if self.bolaM.get_BMViva() == True:
					self.bolaM.updateBM()
					self.bolaM.bola.nextFrame()
					# Recoger municion
					AlcanzarMunicion = self.bolaM.AlcanzaMunicion(self.Tanque.get_naveRect())
					
					if AlcanzarMunicion == True:
						self.DataPuntos.set_municion()
						self.bolaM.newPosicionBM()
						self.bolaM.set_BMViva(False)
						
				elif self.bolaM.get_BMViva() == False:
					ran = random.randint(0, 50)
					if ran == 1:
						self.bolaM.set_BMViva(True)
						
			
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
	def __init__(self,msn,screen,DataPunts):
		self.msn = msn
		self.screen = screen
		self.DataPuntos = DataPunts

	def NivelSuperado(self,puntos,nivel):


		portada = pygame.image.load('./img/logo_superado.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 100)
		self.screen.blit(portada,portadaRect)

		txta = '[C] - Continuar'
		txt2b = '[Q] - Salir'
		self.msn.MensajeSimple(txta, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2b, (255,0,0),13,90,380)
		nivel = nivel-1
		txt = 'Nivel '+str(nivel)+'  SUPERADO!! '
		self.msn.MensajeSimple(txt, (255,0,0),20,200,200)
		txt = str(puntos[0])+' puntos  + '+str(round(puntos[1]))+'% Efect. =  '+str(puntos[2])+' puntos'
		self.msn.MensajeSimple(txt, (85,162,237),20,120,260)
		pygame.display.flip()


	def AvisoMuerte(self,vidas):

		portada = pygame.image.load('./img/logo_alcanzado.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 100)
		self.screen.blit(portada,portadaRect)

		txta = '[C] - Continuar'
		txt2b = '[Q] - Salir'
		self.msn.MensajeSimple(txta, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2b, (255,0,0),13,90,380)

		txt = 'Te han matado tienes '+str(vidas)+' vidas '
		self.msn.MensajeSimple(txt, (255,0,0),20,150,200)
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


	def FinPartida(self,puntos,nivel):

		portada = pygame.image.load('./img/gameover.png').convert_alpha()
		portadaRect = portada.get_rect()
		portadaRect.center = (285, 120)


		portadaGame = pygame.image.load('./img/caratula.png').convert_alpha()
		portadaGameRect = portadaGame.get_rect()
		portadaGameRect.center = (315, 270)

		txta = str(puntos)+' puntos  | Nivel '+str(nivel)
		self.msn.MensajeSimple(txta, (223,11,11),20,150,300)


		txt = '[C] - Nueva Partida'
		txt2 = '[Q] - Salir'
		self.msn.MensajeSimple(txt, (255,0,0),13,90,350)
		self.msn.MensajeSimple(txt2, (255,0,0),13,90,380)

		self.screen.blit(portada,portadaGameRect)
		self.screen.blit(portadaGame,portadaRect)
		

		pygame.display.flip()



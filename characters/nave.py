#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nave.py
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

ANCHO = 600
ALTO = 450
LINEA_INF = 420
LIMIT_ALTO = 60
VELOCIDAD = 5
VELOCIDAD_LASER = 15

RECTS_NAVE = {'anRect':26, 'alRect':40,'desX':14,'desY':20}


import pygame, sys
from pygame.locals import *



class Nave(pygame.sprite.Sprite):
	def __init__(self,screen,DataPuntos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('./img/nave_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (ANCHO/2,LINEA_INF)





		self.speed = VELOCIDAD
		self.screen = screen

		self.disparoActivoD = {1:False, 2:False, 3:False, 4:False, 5:False,6:False, 7:False, 8:False}
		self.pasoDisparoD = {1:False, 2:False, 3:False, 4:False, 5:False,6:False, 7:False, 8:False}
		self.lasersActivosD = {}
		self.DataPuntos = DataPuntos

		self.naveRect = pygame.Rect(self.rect.center[0]-RECTS_NAVE['desX'], self.rect.center[1]-RECTS_NAVE['desY'], RECTS_NAVE['anRect'], RECTS_NAVE['alRect'])


	def PosicionInicio(self):
		self.rect.center = (ANCHO/2,LINEA_INF)

	def NaveMostrar(self):
		self.screen.blit(self.image,self.rect)
		pygame.draw.rect(self.screen, (255,255,255), self.get_naveRect(), 2)

	def get_naveRect(self):
		self.naveRect = pygame.Rect(self.rect.center[0]-RECTS_NAVE['desX'], self.rect.center[1]-RECTS_NAVE['desY'], RECTS_NAVE['anRect'], RECTS_NAVE['alRect'])
		return self.naveRect

	def ColisionEnemy(self,enemy):
		if self.colliderect(enemy):
			print ("Hubo una colision")

	def resetNave(self):
		self.rect.center = (ANCHO/2,LINEA_INF)
		self.naveRect = pygame.Rect(self.rect.center[0]-RECTS_NAVE['desX'], self.rect.center[1]-RECTS_NAVE['desY'], RECTS_NAVE['anRect'], RECTS_NAVE['alRect'])



	def update(self):
		key = pygame.key.get_pressed()
		valores = self.rect
		upx = valores[0]+20
		upy = valores[1]+25


		if key[K_LEFT] and key[K_UP]:
			upx = upx-self.acelerador(key)
			upy = upy-self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_RIGHT] and key[K_UP]:
			upx = upx+self.acelerador(key)
			upy = upy-self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_RIGHT] and key[K_DOWN]:
			upx = upx+self.acelerador(key)
			upy = upy+self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_LEFT] and key[K_DOWN]:
			upx = upx-self.acelerador(key)
			upy = upy+self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_LEFT]:
			upx = upx-self.acelerador(key)
			self.NaveCambio('./img/nave_1_iz.png')

		elif key[K_RIGHT]:
			upx = upx+self.acelerador(key)
			self.NaveCambio('./img/nave_1_de.png')

		elif key[K_UP]:
			upy -= self.acelerador(key)*2
			upx = upx
			self.IMGfogonazo()

		elif key[K_DOWN]:
			upy = upy+self.acelerador(key)*2
			upx = upx

		elif key[K_x]:
			if self.DataPuntos.get_municion() > 0:
				self.Disparo()
		else:
			self.NaveCambio('./img/nave_1.png')


		if upx>=ANCHO-25:
			upx = ANCHO-25

		if upy<=LIMIT_ALTO:
			upy = LIMIT_ALTO

		if upy>LINEA_INF:
			upy = LINEA_INF

		if upx<25:
			upx = 25

		self.rect.center = (upx, upy)


	def acelerador(self,key):
		aceleron = self.speed
		if key[K_a]:
			aceleron = VELOCIDAD+4
			self.IMGfogonazo()

		return aceleron

	def IMGfogonazo(self):
		upx = self.rect[0]
		upy = self.rect[1]
		self.imageAC = pygame.image.load('./img/nave_1_aceleron.png').convert_alpha()
		self.rectAC = self.imageAC.get_rect()
		self.rectAC.center = (upx+20,upy+50)
		self.screen.blit(self.imageAC, self.rectAC)


	def NaveCambio(self,img):
		self.image = pygame.image.load(img).convert_alpha()
		self.screen.blit(self.image,self.rect)


	def Disparo(self):
		valueXY = self.rect
		key = pygame.key.get_pressed()
		if self.DataPuntos.get_municion() > 0:
			if key[K_x]:
				for dA in self.disparoActivoD:

					if self.disparoActivoD[dA]==True:
						unTiro = self.lasersActivosD[dA]
						unTiro.update()


					elif dA == 1:
						unTiro = Laser(valueXY[0],valueXY[1])
						unTiro.update()
						self.lasersActivosD[dA] = unTiro
						self.disparoActivoD[dA] = True
						self.DataPuntos.AumentaDisparos()




					elif dA > 1:
						if self.disparoActivoD[dA-1]==True and self.pasoDisparoD[dA-1] == True:
							unTiro = Laser(valueXY[0],valueXY[1])
							unTiro.update()
							self.lasersActivosD[dA] = unTiro
							self.disparoActivoD[dA] = True
							self.DataPuntos.AumentaDisparos()



	def updateDisparos(self):
		for dA in self.disparoActivoD:

			if self.disparoActivoD[dA] == True:

				unTiro = self.lasersActivosD[dA]
				unTiro.update()
				self.pasoDisparoD[dA] = True


				self.screen.blit(unTiro.image, unTiro.rect)

				if unTiro.laser_y <= 0:
					self.pasoDisparoD[dA] = False
					self.disparoActivoD[dA] = False
					unTiro.kill()
				else:
					self.lasersActivosD[dA] = unTiro





class Laser(pygame.sprite.Sprite):
	def __init__(self,xl,yl):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/laser.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (xl,xl)
		self.speedLaser = VELOCIDAD_LASER
		self.laser_x = xl+18
		self.laser_y = yl+25

	def update(self):
		self.laser_y= self.laser_y-self.speedLaser

		if self.laser_x == 0:
			self.rect.kill()

		self.rect.center = (self.laser_x, self.laser_y)


















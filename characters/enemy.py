#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  enemy.py
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

import pygame, sys, os, math
from pygame.locals import *
import random

ANCHO = 600
ALTO = 450

VEL_ALIEN_1 = 5
VEL_SHOT_ALIEN_1 = 10
FRECUENCIA_DISPARO = 60 # contra más alto menos disparan ya que disparan si sale 0, ente 0 y n

RECTS_LASER_E = {'anRect':3, 'alRect':13,'desX':2,'desY':8}
RECTS_ENEMY = {'anRect':32, 'alRect':24,'desX':-4,'desY':-4}


class Alien_1(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.valorPuntos = 10
		self.speed = random.randint(1, 4)
		self.vivo = True

		self.MunicionAlien = 3
		self.tiempoDisparo = 0
		self.lasersActivosAliens = {}



		self.x = random.randint(1, 600)
		self.y = random.randint(-600, 0)

		self.image = pygame.image.load('./img/enemy_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)

		self.disparoActivoD = {1:False, 2:False, 3:False}
		self.pasoDisparoD = {1:False, 2:False, 3:False}
		self.lasersActivosD = {}

		self.alienRect = pygame.Rect(self.x-RECTS_ENEMY['desX'], self.y-RECTS_ENEMY['desY'], RECTS_ENEMY['anRect'], RECTS_ENEMY['alRect'])


	def get_alienRect(self):
		self.alienRect = pygame.Rect(self.x-RECTS_ENEMY['desX'], self.y-RECTS_ENEMY['desY'], RECTS_ENEMY['anRect'], RECTS_ENEMY['alRect'])
		return self.alienRect






	def update(self,TuNave):

		corde = self.rect

		coorTuNave = TuNave.rect

		lax = corde[0]
		lay = corde[1]

		if lay >= 450:
			lax = random.randint(5, 550)
			lay = 0

		ale = random.randint(0,2)



		if coorTuNave[0]>lax:
			if ale == 0:
				lax = lax+self.speed


		if coorTuNave[0]<lax:
			if ale == 0:
				lax = lax-self.speed




		self.x = lax
		self.y = lay+1

		self.rect = (self.x,self.y)

		self.screen.blit(self.image,self.rect)
		#pygame.draw.rect(self.screen, (255,0,0), self.get_alienRect(), 3)







	def DisparoEnemy(self):

		valueXY = self.rect
		AleDispa = random.randint(0, 60)
		if valueXY[1]>25 and AleDispa==0:


			for dA in self.disparoActivoD:

				if self.disparoActivoD[dA]==True:
					unTiro = self.lasersActivosD[dA]
					unTiro.update()


				elif dA == 1:
					unTiro = LaserEnemy(valueXY[0],valueXY[1])
					unTiro.update()
					self.lasersActivosD[dA] = unTiro
					self.disparoActivoD[dA] = True




				elif dA > 1:
					if self.disparoActivoD[dA-1]==True and self.pasoDisparoD[dA-1] == True:
						unTiro = LaserEnemy(valueXY[0],valueXY[1])
						unTiro.update()
						self.lasersActivosD[dA] = unTiro
						self.disparoActivoD[dA] = True





	def updateDisparosEnemy(self):
		for dA in self.disparoActivoD:

			if self.disparoActivoD[dA] == True:

				unTiro = self.lasersActivosD[dA]
				unTiro.update()
				self.pasoDisparoD[dA] = True




				self.screen.blit(unTiro.image, unTiro.rect)
				#pygame.draw.rect(self.screen, (255,255,255), unTiro.get_lasereRect(), 1)



				if unTiro.laser_y >= 450:
					self.pasoDisparoD[dA] = False
					self.disparoActivoD[dA] = False
					pass
				else:
					self.lasersActivosD[dA] = unTiro



	def mirarAciertosAliens(self,objeto):
		for dA in self.disparoActivoD:

			if self.disparoActivoD[dA] == True:
				unTiro = self.lasersActivosD[dA]
				if objeto.colliderect(unTiro.get_lasereRect()):

					return True
				else:
					return False


class LaserEnemy(pygame.sprite.Sprite):
	def __init__(self,xl,yl):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/laser_alien.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (xl,xl)
		self.speedLaser = VEL_SHOT_ALIEN_1
		self.laser_x = xl+18
		self.laser_y = yl+25

		self.laserERect = pygame.Rect(self.laser_x-RECTS_LASER_E['desX'], self.laser_y-RECTS_LASER_E['desY'], RECTS_LASER_E['anRect'], RECTS_LASER_E['alRect'])

	def update(self):
		self.laser_y= self.laser_y+VEL_SHOT_ALIEN_1
		self.rect.center = (self.laser_x, self.laser_y)

	def get_lasereRect(self):
		self.laserERect = pygame.Rect(self.laser_x-RECTS_LASER_E['desX'], self.laser_y-RECTS_LASER_E['desY'], RECTS_LASER_E['anRect'], RECTS_LASER_E['alRect'])
		return self.laserERect








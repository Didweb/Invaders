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


def load_img(nombre, directorio):
	ruta = os.path.join(directorio, nombre)
	try:
		image = pygame.image.load(ruta)
	except:
		print('Error! Al cargar la imagen')
	return image.convert_alpha()




class Enemys(pygame.sprite.Sprite):
	def __init(self):
		pygame.sprite.Sprite.__init__(self)



	def pintar(self):
		self.screen.blit(self.image,self.rect)

	def muerto(self):
		corde = self.rect
		self.explosion(self.rect)
		#self.x = -30
		#self.y =-30

	def update(self):
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)


	def explosion(self,cordeXY):
		corde = cordeXY
		self.explo = PlaySujeto(self.imagenExp,corde[0],corde[1])




	def exploUpdate(self):
		if self.explo.indicador <= 40:
			self.explo.update(self.screen)
			self.explo.nextFrame()
		elif self.explo.indicador > 40:
			self.x = -30
			self.y = -30


	def get_alienRect(self):
		self.alienRect = pygame.Rect(self.x - self.RectEnemy['desX'], \
									self.y - self.RectEnemy['desY'], \
									self.RectEnemy['anRect'], \
									self.RectEnemy['alRect'])
		return self.alienRect


	def DisparoEnemy(self):

		valueXY = self.rect
		AleDispa = random.randint(0, 60)
		if valueXY[1]>25 and AleDispa==0:


			for dA in self.disparoActivoD:

				if self.disparoActivoD[dA]==True:
					unTiro = self.lasersActivosD[dA]
					unTiro.update()


				elif dA == 1:
					unTiro = LaserEnemy(self.x,self.y,self.L_RectLaserE,self.L_Settings)
					unTiro.update()
					self.lasersActivosD[dA] = unTiro
					self.disparoActivoD[dA] = True

				elif dA > 1:
					if self.disparoActivoD[dA-1]==True and self.pasoDisparoD[dA-1] == True:
						unTiro = LaserEnemy(self.x,self.y,self.L_RectLaserE,self.L_Settings)
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



class AlienMosca(Enemys):
	def __init__(self,screen):
		Enemys.__init__(self)

		self.imagenExp = [ pygame.image.load('./img/enemy_1_exp/1.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/2.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/2.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/3.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/3.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/4.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/4.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/5.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/5.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/6.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/6.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/7.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/7.png').convert_alpha(), \
							pygame.image.load('./img/enemy_1_exp/8.png').convert_alpha() \
							]

		self.lasersActivosD = {}
		self.screen = screen
		self.RectLaserE = {'anRect':3, 'alRect':13,'desX':2,'desY':8}
		self.RectEnemy = {'anRect':32, 'alRect':24,'desX':-4,'desY':-4}


		self.x = random.randint(1, 600)
		self.y = random.randint(-600, 0)


		self.image = pygame.image.load('./img/enemy_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (self.x, self.y)


		# Settings para n disparos
		self.disparoActivoD = {1:False, 2:False, 3:False}
		self.pasoDisparoD = {1:False, 2:False, 3:False}


		self.valorPuntos = 10
		self.speed = random.randint(1, 4)
		self.vivo = True

		self.vidaexplo=0
		# Parametros del Laser
		self.L_RectLaserE = {'anRect':3, 'alRect':13,'desX':2,'desY':8}
		self.L_Settings = {'L_posX': 18, \
							'L_posY': 25, \
							'L_img': './img/laser_alien.png', \
							'L_velShot': 10, \
							'L_freqShot': 60}





	def pasitos(self,TuNave):


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


		self.rect = self.rect = (self.x,self.y)




		#pygame.draw.rect(self.screen, (255,0,0), self.get_alienRect(), 3)




class sujeto(pygame.sprite.Sprite):

	def __init__(self, imagenes,x,y):
		self.imagenes = imagenes
		self.frame = 0
		self.indicador = 30
		self.rect = self.imagenes[self.frame].get_rect()
		self.rect.top = x
		self.rect.left = y
	def move(self, vx, vy):
		self.rect.move_ip(vx,vy)
	def update(self, superficie):
		corde = self.rect
		superficie.blit(self.imagenes[self.frame],(corde[1],corde[0]))
	def nextFrame(self):
		self.frame = self.indicador % len(self.imagenes)
		self.indicador+=1
	def setNewSprites(self, imagenes):
		self.imagenes = imagenes



class PlaySujeto(sujeto):

	def __init__(self, imagenes,x,y):
		sujeto.__init__(self, imagenes,x,y)
	def getLife():
		return self.life




class LaserEnemy(pygame.sprite.Sprite):
	def __init__(self,xl,yl,Rects,Sets):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(Sets['L_img']).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (xl,xl)
		self.speedLaser = Sets['L_velShot']
		self.laser_x = xl+Sets['L_posX']
		self.laser_y = yl+Sets['L_posY']

		self.Sets = Sets
		self.Rects = Rects

		self.laserERect = pygame.Rect( \
							self.laser_x-Rects['desX'], \
							self.laser_y-Rects['desY'], \
							Rects['anRect'], \
							Rects['alRect'])

	def update(self):
		self.laser_y= self.laser_y+self.Sets['L_velShot']
		self.rect.center = (self.laser_x, self.laser_y)

	def get_lasereRect(self):
		self.laserERect = pygame.Rect( \
							self.laser_x-self.Rects['desX'], \
							self.laser_y-self.Rects['desY'], \
							self.Rects['anRect'], \
							self.Rects['alRect'])
		return self.laserERect








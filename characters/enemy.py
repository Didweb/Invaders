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

import pygame, sys, os
from pygame.locals import *
import random
from .sujetos import (sujeto,Play,load_img)

ANCHO = 600
ALTO = 450

VEL_ALIEN_1 = 5
VEL_SHOT_ALIEN_1 = 15

sujeto

class Alien_1(pygame.sprite.Sprite):
	def __init__(self,screen):
		self.screen = screen
		self.valorPuntos = 10
		self.speed = VEL_ALIEN_1
		self.vivo = True


		path_ebeny_1 = './img/enemy_1'
		path_ebeny_1_exp = './img/enemy_1_exp'

		self.enemy_1 = [load_img('enemy_1_1.png',path_ebeny_1 ), \
					load_img('enemy_1_2.png',path_ebeny_1 ), \
					load_img('enemy_1_3.png',path_ebeny_1 ), \
					load_img('enemy_1_4.png',path_ebeny_1 ), \
					load_img('enemy_1_5.png',path_ebeny_1 ),
					load_img('enemy_1_5.png',path_ebeny_1 ),\
					load_img('enemy_1_6.png',path_ebeny_1 ), \
					load_img('enemy_1_7.png',path_ebeny_1 ),
					load_img('enemy_1_7.png',path_ebeny_1 ), \
					load_img('enemy_1_8.png',path_ebeny_1 ),
					load_img('enemy_1_8.png',path_ebeny_1 )]

		self.enemy_1_exp = [load_img('enemy_1_exp_1.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_2.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_3.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_4.png',path_ebeny_1_exp),
			load_img('enemy_1_exp_5.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_6.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_7.png',path_ebeny_1_exp), \
			load_img('enemy_1_exp_8.png',path_ebeny_1_exp)]

		self.imagenes = self.enemy_1
		self.frame = 0
		self.indicador = 30


		self.rect = self.imagenes[self.frame].get_rect()
		self.rect.center = (ANCHO/2,ALTO/2)
		self.screen.blit(self.imagenes[self.frame],self.rect)





	def update(self):

		self.rect = self.imagenes[self.frame].get_rect()
		self.rect.center = self.movimientos()
		self.screen.blit(self.imagenes[self.frame],self.rect)

	def nextFrame(self):
		self.frame = self.indicador % len(self.imagenes)
		self.indicador+=1

	def setNewSprites(self, imagenes):
		self.imagenes = imagenes

	def HitShot(self,screen):
		n = len(self.enemy_1_exp)
		for i in range(n):
			screen.blit(self.enemy_1_exp[i],self.rect)

		self.vivo = False


	def movimientos(self):
		mx = self.rect[0]
		my = self.rect[1]
		ale = random.randint(1, 4)
		if mx<=0:
			mx = mx+1
		elif mx>=ANCHO:
			mx = mx-1

		if my<=15:
			my = my+ale
		elif my>=ALTO:
			my = my+ale

		return (mx,my)


	def paint(self):
		self.update()
		self.nextFrame()







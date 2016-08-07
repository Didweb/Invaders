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

import pygame, sys
from pygame.locals import *


ANCHO = 600
ALTO = 450

VEL_ALIEN_1 = 5
VEL_SHOT_ALIEN_1 = 15


class Alien_1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./img/enemy_1.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = (ANCHO/2,ALTO/2)
		self.speed = VEL_ALIEN_1

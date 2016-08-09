#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
from scene.scene import Scene
import pygame
import scene.director
from pygame.locals import *
import scene_home


# Constantes
BLANCO = (255,255,255)
NEGRO = (0, 0, 0)
MAGENTA = (255,0,255)
FPS = 60

# Clases
# ---------------------------------------------------------------------



class Cuadrado:
    def __init__(self, x, y, lado, color, fondo):
        self.x = x
        self.y = y
        self.color = color
        self.fondo = fondo
        self.lado = lado
        self.rect = pygame.Rect(self.x,
                                self.y,
                                self.lado,
                                self.lado)

    def __pinta(self, pantalla, color):
        'Realiza el dibujo efectivo'
        pygame.draw.rect(pantalla, color, self.rect, 0)

    def pinta(self, pantalla):
        'Pinta el cuadrado con el color propio'
        self.__pinta(pantalla, self.color)

    def borra(self, pantalla):
        'Borra el cuadrado'
        # Realmente lo pinta con el color de fondo
        self.__pinta(pantalla, self.fondo)

    def colisiona_con(self, cuadrado2):
        'Comprueba la colisión con otro cuadrado'
        return self.rect.colliderect(cuadrado2.rect)

    def mover(self, avance_x, avance_y):
        'avance del cuadrado en un cuadro (frame)'
        self.rect.move_ip(avance_x, avance_y)



class Pantalla1(Scene):
	"""Escena inicial del juego, esta es la primera que se carga cuando inicia"""

	def __init__(self, director):
		Scene.__init__(self, director)

	def on_update(self, screen):
		self.cuadrado = Cuadrado(50,50, 35, BLANCO, NEGRO)
		self.cuadrado2 = Cuadrado(540,50,35, MAGENTA, NEGRO)
		self.cuadrado.pinta(screen)
		self.cuadrado2.pinta(screen)
		pygame.display.update()

	def on_event(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()


	def on_draw(self, screen):
		print ('Pantalla 1')
		key = pygame.key.get_pressed()

		if key[K_q] :
			self.quit()

		if key[K_c] :
			sceneSH = scene_home.SceneHome(dir)
			self.director.change_scene(sceneSH)



		# borrar el cuadrado de la pantalla
		self.cuadrado.borra(screen)
		self.cuadrado.mover(1, 0)
		self.cuadrado.pinta(screen)
		pygame.display.update()



# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos

# Constantes

from scene.scene import Scene
from scene.director import Director
import pygame
import Pantalla_1
from pygame.locals import *



# Clases
# ---------------------------------------------------------------------

class SceneHome(Scene):
	"""Escena inicial del juego, esta es la primera que se carga cuando inicia"""

	def __init__(self, director):
		Scene.__init__(self, director)

	def on_update(self):
		pass

	def on_event(self):

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quit()


	def on_draw(self, screen):
		print('Escena Home')
		key = pygame.key.get_pressed()

		if key[K_q] :
			self.quit()

		if key[K_c] :
			sceneP1 = Pantalla_1.Pantalla1(dir)
			self.director.change_scene(scene)


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------

def main():
	print('Escena Home')
	 # Eventos de Salida
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			self.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				dir = director.Director()
				scene = Pantalla_1.Pantalla1(dir)
				dir.change_scene(scene)

if __name__ == '__main__':
	main()

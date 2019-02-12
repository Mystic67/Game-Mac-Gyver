#! /usr/bin/python3
# -*-coding: utf-8-*-
import os
import pygame
from pygame.locals import *
from settings import *
from map import Map

#Init Pygame
pygame.init()

#Window
window = pygame.display.set_mode((window_side_size, window_side_size))

#Icon
icon = pygame.image.load(icon_picture)
pygame.display.set_icon(icon)

#Title
pygame.display.set_caption(window_title)

#Main loop
continue_main = 1
while continue_main:

	#These variables are reset to 1 at each loop
	continue_game = 1
	continue_home = 1

	map = Map("map.txt")
	map.draw_map(window)
	pygame.display.flip()

	#Home loop
	while continue_home:

		#Limit the loop speed
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#If user quit, put this varables to 0
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				continue_main = 0

	#Game loop
	while continuer_game:

		#Limit the loop speed
		pygame.time.Clock().tick(30)

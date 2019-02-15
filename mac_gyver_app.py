#! /usr/bin/python3
# -*-coding: utf-8-*-

import os
import pygame
from pygame.locals import *
import config.settings as constants
from views.graphic_map import Graphic_Map
from views.sprite import Sprite

#Init Pygame
pygame.init()


#Initialize the window size and load the stat_picture
window = pygame.display.set_mode((constants.WINDOW_SIDE_SIZE, constants.WINDOW_SIDE_SIZE))


#Display the start picture
picture_home = pygame.image.load(constants.HOME_PICTURE).convert()
window.blit(picture_home,(0,0))
pygame.display.flip()


#Set the icon from application
icon = pygame.image.load(constants.ICON_PICTURE)
pygame.display.set_icon(icon)


#Set the title from window
pygame.display.set_caption(constants.WINDOW_TITLE)


'''Loop from the main programme'''
continue_main = 1
while continue_main:
	#This variables are set to 1 at each loop
	continue_home = 1
	continue_game = 1


	'''Home loop'''
	while continue_home:


		#Limit the loop speed
		pygame.time.Clock().tick(30)


		for event in pygame.event.get():
			#If user quit, put all loops variables and game_level to 0
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				continue_main = 0
				game_level = 0
			#If user presse space bar, quit home screen and choise game level
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					continue_home = 0
					game_level = 1


	if game_level != 0:
		#Load the map from file and draw the tiles from the map
#		pygame.image.load(constants.home_picture).convert()
		map = Graphic_Map(constants.MAP)
		map.draw_map(window)
		#refresh the display
		pygame.display.flip()
		#Create the sprite Mac Gyver and display it on start position
		# Mac Gyver is movable (Last param True)
		mac_gyver = Sprite(map, constants.MAC_GYVER, constants.START, True)
		mac_gyver.display(window)
		#Create the sprite Mac Gyver and display it on start position
		murdoc = Sprite(map, constants.MURDOC, constants.GOAL)
		murdoc.display(window)
		#refresh the display
		pygame.display.flip()


	'''Game loop'''
	while continue_game:


		#Limit the loop speed
		pygame.time.Clock().tick(30)
		for event in pygame.event.get():
			#If user quit, put all loops variables and game_level to 0
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				continue_main = 0
				game_level = 0
			#If user presse space bar, quit home screen and choise game level
			elif event.type == KEYDOWN:
				if event.key == K_RIGHT:
					mac_gyver.move_right()

				elif event.key == K_LEFT:
					mac_gyver.move_left()

				elif event.key == K_UP:
					mac_gyver.move_up()

				elif event.key == K_DOWN:
					mac_gyver.move_down()


		#Draw map and display the sprites and objects
		map.draw_map(window)
		mac_gyver.display(window)
		murdoc.display(window)
		##refresh the display
		pygame.display.flip()

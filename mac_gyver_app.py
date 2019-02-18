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
					game_end = 0


	if game_level != 0:
		#Load the map from file and draw the tiles from the map
#		pygame.image.load(constants.home_picture).convert()
		map = Graphic_Map(constants.MAP)
		map.draw_map(window)
		#refresh the display
		pygame.display.flip()
		#Create the sprite Mac Gyver and display it on start position
		# Mac Gyver is movable (Last param True)
		#Create the sprite Mac Gyver and display it on start position
		mac_gyver = Sprite(map, constants.MAC_GYVER, constants.START, True)
		mac_gyver.display(window)

		#Create the sprite Murdoc and display it on start position
		murdoc = Sprite(map, constants.MURDOC, constants.GOAL)
		murdoc.display(window)

		list_gadget=[]
		for index, gadget in enumerate(constants.GADGETS_NAME):
			#for image in constants.GADGETS:
			#print(gadget)
			gadget = Sprite(map, constants.GADGETS_PICTURES[index])
			list_gadget.append(gadget)
			gadget.display(window)


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
		murdoc.display(window)
		mac_gyver.display(window)

        #Diplay the gadget from list
		for index, gadget in enumerate(list_gadget):
			if gadget.get_position() == mac_gyver.get_position():
				del list_gadget[index]
			gadget.display(window)

		if murdoc.get_position() == mac_gyver.get_position():
			continue_game = 0
			game_end = 1


		#refresh the display
		pygame.display.flip()

	'''End of game '''
	if game_end != 0:

		if len(list_gadget) == 0:
			del murdoc
			mac_gyver.display(window)
			message = pygame.image.load(constants.YOU_WIN).convert_alpha()

		else:
			del mac_gyver
			murdoc.display(window)
			message = pygame.image.load(constants.YOU_LOSE).convert_alpha()

		window.blit(message, (120,200))
		#refresh the display
		pygame.display.flip()

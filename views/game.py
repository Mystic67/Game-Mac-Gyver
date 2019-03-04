#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants
from controller.events import Events as events
from views.graphic_map import Graphic_Map
from views.sprite import Sprite
from views.counter import Counter


class Game:
    '''This class is for the program flow '''
    @classmethod
    def __init__(cls):
        '''This class initialize the window'''
        # Init Pygame
        pygame.init()
        # Initialize the window size.
        cls.window = pygame.display.set_mode(
            (constants.WINDOW_WIDTH_SIDE_SIZE,
             constants.WINDOW_HEIGHT_SIDE_SIZE))
        # Load the stat_picture
        picture_home = pygame.image.load(constants.HOME_PICTURE).convert()
        # Display the start picture
        cls.window.blit(picture_home, (0, 0))
        # Set the icon from application
        icon = pygame.image.load(constants.ICON_PICTURE)
        pygame.display.set_icon(icon)
        # Set the title from window
        pygame.display.set_caption(constants.WINDOW_TITLE)
        # Display counter background
        cls.window.blit(
            Counter.background(),
            (constants.COUNTER_POS_X,
             constants.COUNTER_POS_Y))
        # refresh the display
        pygame.display.flip()

    @classmethod
    def home_loop(cls):
        # init the game variables
        events.init_game()
        '''Home loop'''
        while events.home:
            # Limit the loop speed
            pygame.time.Clock().tick(30)
            # Listen the user entry.
            events.listen_game_events()
            # Reset the gadgets counter
            Counter.reset()

        if events.game_level != 0:
            # Load the map from file and draw the tiles from the map
            cls.graphmap = Graphic_Map(constants.MAP)
            cls.graphmap.draw_map(cls.window)
            # Create the personnages
            cls.create_personnages()
            # Create the gadgets and display them
            cls.create_gadgets()

    @classmethod
    def game_loop(cls):
        '''Game loop'''
        while events.game:
            # Limit the loop speed
            pygame.time.Clock().tick(30)
            # Call game events with events for moving the sprite
            events.listen_game_events(cls.mac_gyver)
            # Draw map and display the sprites and objects
            cls.graphmap.draw_map(cls.window)
            cls.murdoc.display(cls.window)
            cls.mac_gyver.display(cls.window)
            # Display the gadget and delete gadgets when picked up
            cls.display_and_del_gadgets()
            # Display the counter
            Counter.display(cls.window)
            # Compare the position from murdoc and mac_gyver to know if game is
            # end
            if cls.murdoc.position.get_position() == \
                    cls.mac_gyver.position.get_position():
                # set the game variables to end the game
                events.end_game()
            # Refresh display
            pygame.display.flip()
            # End the game
            cls.end_game()

    @classmethod
    def end_game(cls):
        '''Method to end the game '''
        if events.game_end != 0:
            # If Mac Gyver win, Murdoc disappears
            if len(cls.object_list_gadget) == 0:
                for sprite in cls.object_list_sprites:
                    if sprite == "murdoc":
                        del sprite
                cls.graphmap.draw_map(cls.window)
                cls.mac_gyver.display(cls.window)
                message = pygame.image.load(constants.YOU_WIN).convert_alpha()
            # if Mac Gyver lose, he disappears
            else:
                for sprite in cls.object_list_sprites:
                    if sprite == "mac_gyver":
                        del sprite
                cls.graphmap.draw_map(cls.window)
                cls.murdoc.display(cls.window)
                for gadget in cls.object_list_gadget:
                    gadget.display(cls.window)
                message = pygame.image.load(constants.YOU_LOSE).convert_alpha()

            # Display the end message
            cls.window.blit(message, (120, 200))
            # refresh the display
            pygame.display.flip()

    @classmethod
    def create_personnages(cls):
        '''This method create the personnages and put them in a List'''
        cls.object_list_sprites = []
        cls.mac_gyver = Sprite(
            cls.graphmap,
            constants.MAC_GYVER,
            constants.START,
            True)
        cls.object_list_sprites.append(cls.mac_gyver)
        # Create the sprite Murdoc and display it on goal position
        cls.murdoc = Sprite(cls.graphmap, constants.MURDOC, constants.GOAL)
        cls.object_list_sprites.append(cls.murdoc)

    @classmethod
    def create_gadgets(cls):
        '''This method create gadgets, put the objects in a
        list and refresh the display'''
        cls.object_list_gadget = []
        for index, cls.gadget in enumerate(constants.GADGETS_NAME):
            cls.gadget = Sprite(
                cls.graphmap,
                constants.GADGETS_PICTURES[index])
            cls.object_list_gadget.append(cls.gadget)
            cls.gadget.display(cls.window)

    @classmethod
    def display_and_del_gadgets(cls):
        ''' This method delete the gadgets when MAC_GYVER
        picked it up and display the gadgets'''
        for index, cls.gadget in enumerate(cls.object_list_gadget):
            if cls.gadget.position.get_position() == \
                    cls.mac_gyver.position.get_position():
                Counter.add_gadgets(cls.object_list_gadget[index])
                del cls.object_list_gadget[index]
            cls.gadget.display(cls.window)

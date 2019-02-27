#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants
from models.map import Map


class Graphic_Map(Map):
    ''' This class inherited from class Map for graphical map drawing'''

    def __init__(self, filename):
        Map.__init__(self, filename)

    def draw_map(self, window):
        ''' This method draw the map tile per tile '''

        tile_error = pygame.image.load(constants.TILE_ERROR).convert()
        tiles = pygame.image.load(constants.TILES_PICTURES)
        tile_start = tiles.subsurface(
            40, 80, 40, 40).convert_alpha()  # Colonne,Ligne,H,W
        tile_wall = tiles.subsurface(480, 440, 40, 40).convert_alpha()
        tile_goal = tiles.subsurface(320, 40, 40, 40).convert_alpha()
        tile_path = tiles.subsurface(360, 40, 40, 40).convert_alpha()

        '''Search the positions and values from loaded file with the item
           generator method defined in parent class Map and display each tile
            at his positions.'''
        for position, value in self.items():
            if value == constants.START:
                x = position.get_x() * constants.SPRITE_SIZE
                y = position.get_y() * constants.SPRITE_SIZE
                window.blit(tile_start, (x, y))
            elif value == constants.WALL:
                x = position.get_x() * constants.SPRITE_SIZE
                y = position.get_y() * constants.SPRITE_SIZE
                window.blit(tile_wall, (x, y))
            elif value == constants.PATH:
                x = position.get_x() * constants.SPRITE_SIZE
                y = position.get_y() * constants.SPRITE_SIZE
                window.blit(tile_path, (x, y))
            elif value == constants.GOAL:
                x = position.get_x() * constants.SPRITE_SIZE
                y = position.get_y() * constants.SPRITE_SIZE
                window.blit(tile_goal, (x, y))
            else:
                x = position.get_x() * constants.SPRITE_SIZE
                y = position.get_y() * constants.SPRITE_SIZE
                window.blit(tile_error, (x, y))
                print("Error string in map at position ({},{})".
                      format(position.get_x() + 1, position.get_y() + 1))

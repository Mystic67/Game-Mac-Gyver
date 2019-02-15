#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
from pygame.locals import *
import config.settings as constants
from views.graphic_map import Graphic_Map
from models.position import Position as pos


class Sprite:
    def __init__(self, instance_map, image, init_pos, move=False ):
        self.__map =instance_map
        self.__image = image
        self.__init_pos = init_pos
        self.__move = move
        self.__move_conditions = [constants.PATH, constants.START, constants.GOAL]
        for position, value in self.__map.items():
            if value == self.__init_pos:
                self.__x= position.get_x()
                self.__y= position.get_y()


    ''' This method is needed to display the sprite on new position after move.'''
    def display(self, window):
        sprite = pygame.image.load(self.__image).convert_alpha()
        window.blit(sprite, (self.__y * constants.SPRITE_SIZE,\
        self.__x * constants.SPRITE_SIZE))


    ''' This methods move the sprite if sprite movable
        The spite can move if target position is Path'''

    '''Method to move_down the sprite '''
    def move_down(self):
        if self.__move:
            if self.__map[self.__x+1, self.__y] in self.__move_conditions:
                self.__x += 1


    '''Method to move_up the sprite '''
    def move_up(self):
        if self.__move:
            if self.__map[self.__x-1, self.__y] in self.__move_conditions:
                self.__x -= 1

    '''Method to move_right the sprite '''
    def move_right(self):
        if self.__move:
            if self.__map[self.__x, self.__y+1] in self.__move_conditions:
                self.__y += 1

    '''Method to move_left the sprite '''
    def move_left(self):
        if self.__move:
            if self.__map[self.__x, self.__y-1] in self.__move_conditions:
                self.__y -= 1

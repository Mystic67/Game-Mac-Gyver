#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants
import random


class Sprite:
    object_create = 0

    def __init__(self, instance_map, image, init_pos="random", move=False):
        ''' Initialize the attributs'''
        self.__map = instance_map
        self.__image = image
        self.__init_pos = init_pos
        self.__move = move
        self.__move_conditions = [
            constants.PATH,
            constants.START,
            constants.GOAL]
        self.__init_position()

    def display(self, window):
        ''' This method is needed to display the sprite on position
         or refresh the position after move.'''
        sprite = pygame.image.load(self.__image).convert_alpha()
        window.blit(sprite, (self.__y * constants.SPRITE_SIZE,
                             self.__x * constants.SPRITE_SIZE))

    def __init_position(self):
        '''This method initialise the position with random
        or given position. '''
        if self.__init_pos == "random":
            type(self).object_create += 1
            rand_pos = random.choice(
                [pos for (pos, val) in self.__map.items()
                    if val == constants.PATH])
            self.__x = rand_pos.get_x()
            self.__y = rand_pos.get_y()

        else:
            ''' if the position is given in param. The position (x,y)
             is stored in list whith list comprehention,
             also need to accès with index 0 '''
            position = [
                pos for (
                    pos,
                    val) in self.__map.items() if val == self.__init_pos]
            self.__x = position[0].get_x()
            self.__y = position[0].get_y()

    def __del__(self):
        # if self.__init_pos == "random":
        type(self).object_create -= 1

    def get_position(self):
        '''Method to get the position from sprite '''
        return (self.__y, self.__x)

    def move_down(self):
        '''Method to move_down the sprite if give attribut True to param __move.
        The spite can move if target position is Path'''
        if self.__move:
            if self.__map[self.__x + 1, self.__y] in self.__move_conditions:
                self.__x += 1

    def move_up(self):
        '''Method to move_up the sprite if give attribut True to param __move.
        The spite can move if target position is Path'''
        if self.__move:
            if self.__map[self.__x - 1, self.__y] in self.__move_conditions:
                self.__x -= 1

    def move_right(self):
        '''Method to move_right the sprite if give attribut True to param __move.
        The spite can move if target position is Path'''
        if self.__move:
            if self.__map[self.__x, self.__y + 1] in self.__move_conditions:
                self.__y += 1

    def move_left(self):
        '''Method to move_left the sprite if give attribut True to param __move.
        The spite can move if target position is Path'''
        if self.__move:
            if self.__map[self.__x, self.__y - 1] in self.__move_conditions:
                self.__y -= 1

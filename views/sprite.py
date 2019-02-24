#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants
import random
from views.counter import Counter


class Sprite:
    '''This class create personnages and gadgets.'''
    def __init__(self, instance_map, image, init_pos="random", movable=False):
        ''' Initialize the attributs'''
        self.__map = instance_map
        self.__image = image
        self.__init_pos = init_pos
        self.__movable = movable
        self.__x = 0
        self.__y = 0
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
            rand_pos = random.choice(
                [pos for (pos, val) in self.__map.items()
                    if val == constants.PATH])
            self.__x = rand_pos.get_x()
            self.__y = rand_pos.get_y()
            # increment counter of total gadgets
            Counter.increment("total_gadgets")
        else:
            ''' if the position is given in param. The position (x,y)
             is stored in list whith list comprehention,
             also need to accès with index 0 '''
            position = [pos for (pos, val) in self.__map.items()
                        if val == self.__init_pos]
            self.__x = position[0].get_x()
            self.__y = position[0].get_y()

    def get_position(self):
        '''Method to get the position from sprite.
        Needed to compare position from MacGyver with MURDOC  '''
        return (self.__y, self.__x)

    def set_position(self, x, y):
        '''Method to set the position from sprites.
        Needed to set the positions from the gadgets in gadgets
        in the counter.'''
        self.__x = x
        self.__y = y

    def move(self, direction):
        '''Method to move the sprite if give attribut True to class parameter.
        The spite can move if target position is Path'''
        self.direction = direction
        if self.__movable:
            if self.direction == "down":
                if self.__map[self.__x + 1,
                              self.__y] in self.__move_conditions:
                    self.__x += 1

            elif self.direction == "up":
                if self.__map[self.__x - 1,
                              self.__y] in self.__move_conditions:
                    self.__x -= 1

            elif self.direction == "right":
                if self.__map[self.__x, self.__y +
                              1] in self.__move_conditions:
                    self.__y += 1

            elif self.direction == "left":
                if self.__map[self.__x, self.__y -
                              1] in self.__move_conditions:
                    self.__y -= 1

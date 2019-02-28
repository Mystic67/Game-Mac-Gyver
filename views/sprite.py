#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants
import random
from views.counter import Counter
from models.position import Position
from collections import deque


class Sprite:
    '''This class create personnages and gadgets.'''
    fifo = deque([], maxlen = len(constants.GADGETS_NAME))

    def __init__(self, instance_map, image="images/ether.png", init_pos="random", movable=False):
        ''' Initialize the attributs'''
        self.__map = instance_map #instance of Graphic_Map
        self.__image = image
        self.__init_pos = init_pos
        self.__movable = movable
        self.__move_conditions = [
            constants.PATH,
            constants.START,
            constants.GOAL]
        self.position = Position(0,0)
        self.__init_position()

    def display(self, window):
        ''' This method is needed to display the sprite on position
         or refresh the position after move.'''
        sprite = pygame.image.load(self.__image).convert_alpha()
        window.blit(sprite, (self.position.get_x() * constants.SPRITE_SIZE,
                             self.position.get_y() * constants.SPRITE_SIZE))

    def __init_position(self):
        '''This method initialise the position with random
        or given position. '''
        if self.__init_pos == "random":
            while 1:
                '''loop to find a free random position '''
                rand_pos = random.choice(
                    [pos for (pos, val) in self.__map.items()
                        if val == constants.PATH])
                if rand_pos not in Sprite.fifo:
                    break
            Sprite.fifo.append(rand_pos)
            self.position.set_position(rand_pos.get_position())
            Counter.increment("total_gadgets")
        else:
            ''' If the position is given in param. The position (x,y)
             is stored in list by a list comprehention.
             Also need to accès to the value with index 0 '''
            position = [pos for (pos, val) in self.__map.items()
                        if val == self.__init_pos]
            self.position.set_position(position[0].get_position())


    def move(self, direction):
        '''Method to move the sprite if give attribut True to class parameter.
        The spite can move if target position is Path'''
        self.direction = direction
        if self.__movable:
            if self.direction == "right":
                if self.__map[self.position.get_x() + 1,
                              self.position.get_y()] in self.__move_conditions:
                    self.position.set_x(self.position.get_x()+1)

            elif self.direction == "left":
                if self.__map[self.position.get_x() - 1,
                              self.position.get_y()] in self.__move_conditions:
                    self.position.set_x(self.position.get_x()-1)

            elif self.direction == "down":
                if self.__map[self.position.get_x(), self.position.get_y() +
                              1] in self.__move_conditions:
                    self.position.set_y(self.position.get_y()+1)

            elif self.direction == "up":
                if self.__map[self.position.get_x(), self.position.get_y() -
                              1] in self.__move_conditions:
                    self.position.set_y(self.position.get_y()-1)

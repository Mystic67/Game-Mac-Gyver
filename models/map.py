#! /usr/bin/python3
# -*-coding: utf-8-*-
#import pandas as pd
# import numpy as np

from position import Position as pos
import settings as constants
import pygame
from pygame.locals import *

class Map:
    def __init__(self, filename):
        ''' intialize the variable '''
        self.filename = filename
        self.list_positions = []
        self.list_chars=[]
        self.load_From_File()

    def load_From_File(self):
        """load the maze from file and  """
        with open(self.filename,"r") as file:
            for x,line in enumerate(file):
                for y, char in enumerate(line):
                    self.list_positions.append(pos(x,y))
                    self.list_chars.append(char)

    def __iter__(self):
        """makes position iterable """
        return iter(self.list_positions)

    def __str__(self):
        """method to represente the map if print(instance) in interpreter """
        string=""
        for value in self.list_chars:
            string+=value
        return string

    def __repr__(self):
        """method to represente the instance from object if enter
         instance name in interpreter """
        string="{"
        first_loop = True
        for key, value in self.items():
            if not first_loop:
                string += ","
            else:
                first_loop = False
            string+= repr(key)+":" + repr(value)
        string+="}"
        return string

    def __getitem__(self, pos):
        """Return the value from position """
        #value=0
        for index, val in enumerate(self.list_positions):
            if hash(val) == hash(pos):
                return self.list_chars[index]

    def items(self):
        """ method to create a generator (list_positions, list_chars) """
        for index, position in enumerate(self.list_positions):
            value= self.list_chars[index]
            if value != "\n":
                yield(position, value)

    def draw_map(self, window):

        start = pygame.image.load(constants.home_picture).convert()
        wall = pygame.image.load(constants.wall_picture).convert()
        goal = pygame.image.load(constants.goal_picture).convert_alpha()
        path = pygame.image.load(constants.background_picture).convert()

        for position, value in self.items():
            #Draw start
            if value == constants.START:
                x=position.get_x() * constants.size_sprite
                y=position.get_y() * constants.size_sprite
                window.blit(start, (x,y))
            elif value == constants.WALL:
                x=position.get_x() * constants.size_sprite
                y=position.get_y() * constants.size_sprite
                window.blit(wall, (x,y))
            elif value == constants.GOAL:
                x=position.get_x() * constants.size_sprite
                y=position.get_y() * constants.size_sprite
                window.blit(goal, (x,y))
            else:
                x=position.get_x() * constants.size_sprite
                y=position.get_y() * constants.size_sprite
                window.blit(path, (x,y))


def main():
    """ main test """
    map = Map("map.txt")
    print(map)
    print(map[(0,0)])
    print(map[2,5])
    print(map[2,6])
    for position, value in map.items():
        print(position, value)

if __name__=="__main__":
    main()

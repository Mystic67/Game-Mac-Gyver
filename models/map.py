#! /usr/bin/python3
# -*-coding: utf-8-*-
#import pandas as pd
# import numpy as np

from position import Position as pos
import settings as constants

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

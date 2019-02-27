#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame
import config.settings as constants


class Counter:
    '''This class is a counter for the gadgets total and gadgets picked up'''
    _total_gadgets = 0
    _picked_up_gadgets = 0
    _picked_up_liste = []

    @classmethod
    def display(cls, window):
        '''This method display the background end text from counter '''
        window.blit(
            cls.background(),
            (constants.COUNTER_POS_X,
             constants.COUNTER_POS_Y))

        window.blit(
            cls.text(),
            ((constants.WINDOW_WIDTH_SIDE_SIZE / 3),
             constants.COUNTER_POS_Y))

        for index, sprite in enumerate(cls._picked_up_liste):
            sprite.position.set_position(
                ((constants.SPRITE_BY_SIDE + 0.75),
                (5 + index * 1.5)))
            sprite.display(window)

    @classmethod
    def text(cls):
        '''This method create the counter texte'''
        font = pygame.font.Font(None, 30)
        text = font.render("Gadgets Picked Up: {}/{}".format(
            cls._picked_up_gadgets, cls. _total_gadgets), True, (0, 0, 0))
        return text

    @classmethod
    def background(cls):
        '''This method create the counter background'''
        background = pygame.Surface(
            (constants.WINDOW_WIDTH_SIDE_SIZE,
             constants.SPRITE_SIZE * 2))
        background.fill((156, 157, 156))
        background.convert()
        return background

    @classmethod
    def increment(cls, variable="gadgets"):
        '''This method increment the attributs'''
        if variable == "gadgets":
            cls._picked_up_gadgets += 1
        else:
            cls._total_gadgets += 1

    @classmethod
    def reset(cls):
        '''This method  reset the attibut to 0'''
        cls._total_gadgets = 0
        cls._picked_up_gadgets = 0
        cls._picked_up_liste = []

    @classmethod
    def add_gadgets(cls, sprite):
        cls._picked_up_liste.append(sprite)
        cls.increment("gadgets")

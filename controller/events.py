#! /usr/bin/python3
# -*-coding: utf-8-*-

import pygame


class Events:
    '''This class listen the user inputs and set the game variables '''
    main = 1
    home = 1
    game = 1
    game_level = 0
    game_end = 0
    # self.listen_events()

    @classmethod
    def listen_game_events(cls, instance_sprite=None):
        cls.instance_sprite = instance_sprite
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_ESCAPE:
                cls.quit_game()  # Quit the game
                '''If user presse space bar, quit home screen and start game'''
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cls.go_game()  # Start de game
                    ''' Listen the directory entry key if instance
                     of sprite is given as parameter'''
                elif instance_sprite is not None:
                    if event.key == pygame.K_RIGHT:
                        cls.instance_sprite.move("right")

                    elif event.key == pygame.K_LEFT:
                        cls.instance_sprite.move("left")

                    elif event.key == pygame.K_UP:
                        cls.instance_sprite.move("up")

                    elif event.key == pygame.K_DOWN:
                        cls.instance_sprite.move("down")

    @classmethod
    def quit_game(cls):
        cls.home = 0
        cls.game = 0
        cls.main = 0
        cls.game_level = 0

    @classmethod
    def init_game(cls):
        cls.home = 1
        cls.game = 1

    @classmethod
    def go_game(cls):
        cls.home = 0
        cls.game_level = 1
        cls.game_end = 0

    @classmethod
    def end_game(cls):
        cls.game = 0
        cls.game_end = 1
        cls.home = 1

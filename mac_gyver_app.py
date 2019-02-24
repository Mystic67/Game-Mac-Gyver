#! /usr/bin/python3
# -*-coding: utf-8-*-


from controller.events import Events as events
from views.game import Game as game


def main():
    # init the game window
    game()
    '''Loop from the main programme'''
    while events.main:

        game.home_loop()

        game.game_loop()


if __name__ == "__main__":
    main()

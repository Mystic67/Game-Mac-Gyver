#!/usr/bin/python3
# -*- coding: Utf-8 -*

# Map constants
START="S"
GOAL="G"
PATH="."
WALL="M"

MAP="models/map.txt"


#Pygame views constants
#window settings
WINDOW_TITLE = "Mac Gyver"
ICON_PICTURE = "images/MacGyver.png"


#mase pictures
HOME_PICTURE = "images/Game_MacGyver.png"
MAC_GYVER = "images/MacGyver.png"
MURDOC = "images/Murdoc.png"
GADGETS_NAME = ["chalumeau", "ether", "couteau", "tube", "seringue"]
GADGETS_PICTURES = ["images/chalumeau.png", "images/ether.png", "images/couteau_suisse.png",\
 "images/tube_plastique.png","images/seringue.png"]
TILES_PICTURES ="images/floor-tiles-40x40.png"
TILE_ERROR = "images/Error_tile.png"
YOU_WIN = "images/You_win.png"
YOU_LOSE = "images/You_lose.png"


#maze settings
SPRITE_BY_SIDE = 15
SPRITE_SIZE = 40
WINDOW_SIDE_SIZE = SPRITE_BY_SIDE * SPRITE_SIZE

import pygame
from pygame.locals import *


FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 20 # size of box height & width in pixels
BOARDWIDTH = 10 # number of columns
BOARDHEIGHT = 20 # number of rows
BORDERWIDTH = 5 #thickness of window borders
PANELWIDTH = 6 # number of columns with spacing
PANELHEIGHT = 4 # number of columns with spacing
BLANK = '.'
assert WINDOWWIDTH > (BOARDWIDTH + PANELWIDTH + 1) * BOXSIZE, 'Board + Panel needs to be smaller than window'
assert (WINDOWHEIGHT / BOXSIZE) > BOARDHEIGHT, 'Board needs to be smaller than window'
#XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * BOXSIZE )) / 2)
XMARGIN = 20
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE)) / 2)


#define colors
#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
DARKGRAY    = ( 90,  90,  90)
BLACK       = (  0,   0,   0)

RED         = (155,   0,   0)   #I
YELLOW      = (155, 155,   0)   #J
PURPLE      = (255,   0, 255)   #L
BLUE        = (  0,   0, 155)   #O
LIGHTBLUE   = ( 20,  20, 175)   #S
GREEN       = (  0, 155,   0)   #T 
ORANGE      = (255, 128,   0)   #Z

I = 'I'
J= 'J'
L = 'L'
O = 'O'
S = 'S'
T = 'T'
Z = 'Z'

#color associations
WINDOWCOLOR = GRAY
BOARDGAMECOLOR = BLACK
BORDERCOLOR = DARKGRAY
TEXTCOLOR = BLACK

#movement constants
ROTATE = 'rotate'   #rotates clockwise
DOWN = 'down'
DROP = 'drop'
LEFT = 'left'
RIGHT = 'right'

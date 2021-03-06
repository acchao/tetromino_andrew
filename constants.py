import pygame
from pygame.locals import *


FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 580 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 20 # size of box height & width in pixels
BOARDWIDTH = 10 # number of columns
BOARDHEIGHT = 20 # number of rows
BORDERWIDTH = 5 #thickness of window borders
PANELWIDTH = 6 # number of columns with spacing
PANELHEIGHT = 5 # number of columns with spacing

assert WINDOWWIDTH > (BOARDWIDTH + PANELWIDTH + 1) * BOXSIZE, 'Board + Panel needs to be smaller than window'
assert (WINDOWHEIGHT / BOXSIZE) > BOARDHEIGHT, 'Board needs to be smaller than window'
XMARGIN = int((WINDOWWIDTH - ((BOARDWIDTH + PANELWIDTH + 1) * BOXSIZE )) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE)) / 2)
BBWIDTH = 1

PANELPIXELX = XMARGIN + BOXSIZE * (BOARDWIDTH+1)
PANELPIXELY = YMARGIN

#define colors
#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
DARKGRAY    = ( 90,  90,  90)
BLACK       = (  0,   0,   0)

RED         = (155,   0,   0)   #I
YELLOW      = (255, 255,   0)   #J
PURPLE      = (255,   0, 255)   #L
BLUE        = (  0,   0, 155)   #O
LIGHTBLUE   = ( 20,  191, 255)   #S
GREEN       = (  0, 155,   0)   #T 
ORANGE      = (255, 128,   0)   #Z

I = 'I'
J = 'J'
L = 'L'
O = 'O'
S = 'S'
T = 'T'
Z = 'Z'
BLANK = 0
SHAPES = (I,J,L,O,S,T,Z)

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

#gameplay speeds
SOFTDROPSPEED = 0.08
LATERALSPEED = 0.15
DEFAULTFALLSPEED = 1

#game states
ACTIVE = 'active'
PAUSE = 'pause'
OVER = 'over'
WIN = 'win'

#scoring and levels
LEVELONE = 1
ONELINEPTS = 40
TWOLINEPTS = 100
THREELINEPTS = 300
FOURLINEPTS = 1200
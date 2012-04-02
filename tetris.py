import random, time, pygame, sys
from pygame.locals import *
#from constants import *


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

#color associations
WINDOWCOLOR = GRAY
BOARDGAMECOLOR = BLACK
BORDERCOLOR = DARKGRAY
TEXTCOLOR = BLACK


def main():
    global FPSCLOCK, DISPLAYSURF, FONTOBJ
    pygame.init()	#initialize the game
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FONTOBJ = pygame.font.Font('freesansbold.ttf', 18)
    
    pygame.display.set_caption('Tetris')

    #set up initial pieces
    board = getBlankBoard()
    DISPLAYSURF.fill(WINDOWCOLOR)
    
    while True: #main game loop
        drawBoard(board)
        drawNextShapePanel()
        drawScorePanel()
        drawInstructions()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #update screen
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
    return board


def drawBoard(board):
    # draw the border around the board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                     (XMARGIN - BORDERWIDTH, YMARGIN - BORDERWIDTH,
                     (BOARDWIDTH * BOXSIZE) + BORDERWIDTH*2, (BOARDHEIGHT * BOXSIZE) + BORDERWIDTH*2), 0)

    # fill the background of the board
    pygame.draw.rect(DISPLAYSURF, BOARDGAMECOLOR, (XMARGIN, YMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # draw the individual boxes on the board
    #for x in range(BOARDWIDTH):
    #    for y in range(BOARDHEIGHT):
    #        drawBox(x, y, board[x][y])

def drawNextShapePanel():
    # draw the border around the next shape panel
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR,
                     (XMARGIN*2 + (BOARDWIDTH * BOXSIZE) - BORDERWIDTH, YMARGIN - BORDERWIDTH,
                     (PANELWIDTH * BOXSIZE) + BORDERWIDTH*2, (PANELHEIGHT * BOXSIZE) + BORDERWIDTH*2), 0)
    # fill the background of the next shape panel
    pygame.draw.rect(DISPLAYSURF, BOARDGAMECOLOR, (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), 
                     YMARGIN, BOXSIZE * PANELWIDTH, BOXSIZE * PANELHEIGHT))

def drawScorePanel():
    # Level
    levelSurf = FONTOBJ.render('Level: ', True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * PANELHEIGHT)
    DISPLAYSURF.blit(levelSurf, levelRect)

    # Score
    scoreSurf = FONTOBJ.render('Score: ', True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+1))
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
    # Lines
    lineSurf = FONTOBJ.render('Lines: ', True, TEXTCOLOR)
    lineRect = lineSurf.get_rect()
    lineRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+2))
    DISPLAYSURF.blit(lineSurf, lineRect)

def drawInstructions():
    # P to start
    # TODO rotate between play and pause
    playSurf = FONTOBJ.render('P - Play/Start ', True, TEXTCOLOR)
    playRect = playSurf.get_rect()
    playRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+4))
    DISPLAYSURF.blit(playSurf, playRect)

    # Q/Esc to Quit
    quitSurf = FONTOBJ.render('Q/ESC - Quit ', True, TEXTCOLOR)
    quitRect = playSurf.get_rect()
    quitRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+5))
    DISPLAYSURF.blit(quitSurf, quitRect)

if __name__ == '__main__':
    main()

import pygame, random
from constants import *
from Piece import *

'''
Class board
The board game, pieces, and mechanics on the board.

'''

class Board:
    def __init__(self,displaysurf):
        self.board = self.getBlankBoard()
        self.displaysurf = displaysurf
        self.piece = Piece(L)
        self.nextPiece = Piece(BLANK)
        #draw the board
        self.draw()

        #Queue the next piece

        #Generate the current piece

        #set the game states
        #new, play, pause, reset

    def draw(self):
        # draw the border around the board
        pygame.draw.rect(self.displaysurf, BORDERCOLOR,
                         (XMARGIN - BORDERWIDTH, YMARGIN - BORDERWIDTH,
                         (BOARDWIDTH * BOXSIZE) + BORDERWIDTH*2, (BOARDHEIGHT * BOXSIZE) + BORDERWIDTH*2), 0)

        # fill the background of the board
        pygame.draw.rect(self.displaysurf, BOARDGAMECOLOR, (XMARGIN, YMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))

        #place the piece on the board.
        for x in range(4):
            for y in range(4):
                self.board[self.piece.x+x][self.piece.y+y] = self.piece.getGrid()[x][y]

        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.drawBox(x, y, self.board[x][y])

        

    #draw each box in the board based on the given x,y, coordinate and box type
    def drawBox(self,x,y,boxType):
        if boxType == I:
            boxColor = RED
        elif boxType == J:
            boxColor = YELLOW
        elif boxType == L:
            boxColor = PURPLE
        elif boxType == O:
            boxColor = BLUE
        elif boxType == S:
            boxColor = LIGHTBLUE
        elif boxType == T:
            boxColor = GREEN
        elif boxType == Z:
            boxColor = ORANGE
        else:
            boxColor = BLACK

        #draw box border
        pygame.draw.rect(self.displaysurf, BLACK, (x*BOXSIZE + XMARGIN, y*BOXSIZE + YMARGIN, BOXSIZE, BOXSIZE))
        
        #draw box fill
        pygame.draw.rect(self.displaysurf, boxColor, 
                        (x*BOXSIZE + XMARGIN + BBWIDTH, y*BOXSIZE + YMARGIN + BBWIDTH, 
                        BOXSIZE - BBWIDTH, BOXSIZE - BBWIDTH))

    def getBlankBoard(self):
        board = []
        # create and return a new blank board data structure
        for i in range(BOARDWIDTH):
            board.append([BLANK] * BOARDHEIGHT)
        return board

    #def getNextPiece(self):
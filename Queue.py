import pygame, random
from constants import *
from Piece import *

'''
Class Queue
This is the panel that shows the next piece and generates it.

'''

class Queue:
    def __init__(self,displaysurf):
        self.panel = self.getBlankPanel()
        self.displaysurf = displaysurf
        self.piece = Piece(random.choice(list(SHAPES)))
        self.piece.x = 1
        self.piece.y = 1

    def draw(self):
        queueX = XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE)
        queueY = YMARGIN
        queueWidth = PANELWIDTH * BOXSIZE
        queueHeight = PANELHEIGHT * BOXSIZE

        #draw the panel border
        pygame.draw.rect(self.displaysurf, BORDERCOLOR, (queueX - BORDERWIDTH, queueY - BORDERWIDTH, 
                        queueWidth + BORDERWIDTH*2,queueHeight + BORDERWIDTH*2))

        #draw the panel
        pygame.draw.rect(self.displaysurf, BOARDGAMECOLOR, (queueX, queueY, queueWidth, queueHeight))

        #draw the piece
        self.drawPiece()

        #draw the panel to the screen
        for x in range(PANELWIDTH):
            for y in range(PANELHEIGHT):
                self.drawBox(x, y, self.panel[x][y])

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
        pygame.draw.rect(self.displaysurf, BLACK, (x*BOXSIZE + PANELPIXELX, y*BOXSIZE + PANELPIXELY, BOXSIZE, BOXSIZE))
        
        #draw box fill
        pygame.draw.rect(self.displaysurf, boxColor, 
                        (x*BOXSIZE + PANELPIXELX + BBWIDTH, y*BOXSIZE + PANELPIXELY + BBWIDTH, 
                        BOXSIZE - BBWIDTH, BOXSIZE - BBWIDTH))

    def drawPiece(self):
        #clear the old piece
        self.clearOldPiece()

        #place the piece on the board.
        for x in range(4):
            for y in range(4):
                self.panel[self.piece.x+x][self.piece.y+y] = self.piece.piece[x][y]

    def clearOldPiece(self):
        for x in range(4):
            for y in range(4):
                self.panel[x][y] = BLANK

    def getNextPiece(self):
        nextPieceType = self.piece.pieceType
        
        #get a new random shape
        self.piece.pieceType = random.choice(list(SHAPES))
        
        #replace the queued piece
        self.piece.piece[:] = self.piece.setPiece(self.piece.pieceType)

        #return the next piece
        return nextPieceType

    def getBlankPanel(self):
        panel = []
        # create and return a new blank board data structure
        for i in range(PANELWIDTH):
            panel.append([BLANK] * PANELHEIGHT)
        return panel
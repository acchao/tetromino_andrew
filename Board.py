import pygame, random
from constants import *
from Piece import *

'''
Class board
The board game, pieces, and mechanics on the board.

SCORING SYSTEM
Basic, where n = level
1 line = 40 * (n+1)
2 line = 100 * (n+1)
3 line = 300 * (n+1)
4 line = 1200 * (n+1)

Soft Drop = rows * 4
Hard Drop = rows * 10
'''

 Board:
    def __init__(self,displaysurf):
        self.board = self.getBlankBoard()
        self.boardWithPieces = self.getBlankBoard()
        self.displaysurf = displaysurf
        self.piece = Piece(random.choice(list(SHAPES)))
        self.completedLines = 0
        self.totalCompletedLines = 0
        self.score = 0
        #draw the board
        self.draw()

        #Queue the next piece
        #self.queueNext();
        
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

        self.drawPiece()

        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.drawBox(x, y, self.board[x][y])

    def clearOldPiece(self):
        for x in range(4):
            for y in range(4):
                if self.piece.piece[x][y] != BLANK and self.board[self.piece.x+x][self.piece.y+y] != BLANK:
                    self.board[self.piece.x+x][self.piece.y+y] = BLANK

    def drawPiece(self,dX=0,dY=0):
        #clear the old piece
        self.clearOldPiece()

        #place the piece on the board.
        self.piece.x += dX
        self.piece.y += dY
        for x in range(4):
            for y in range(4):
                if self.isOnBoard(bX=self.piece.x+x,bY=self.piece.y+y):
                    if self.piece.piece[x][y] != BLANK:     #only draw the nonblank tiles
                        self.board[self.piece.x+x][self.piece.y+y] = self.piece.piece[x][y]

    def setPiece(self):
        #place the piece on the boardWithPieces.
        for x in range(4):
            for y in range(4):
                if self.isOnBoard(bX=self.piece.x+x,bY=self.piece.y+y):
                    if self.piece.piece[x][y] != BLANK:     #only draw the nonblank tiles
                        self.boardWithPieces[self.piece.x+x][self.piece.y+y] = self.piece.piece[x][y]
                        self.board[self.piece.x+x][self.piece.y+y] = self.piece.piece[x][y]

    def newPiece(self,shapeType):
        self.piece = Piece(shapeType)

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

    def movePiece(self, action):
        isSet = False
        
        if action == DROP:
            while self.isValidMove(action):
                self.clearOldPiece()
                self.piece.y += 1
            self.setPiece()
            isSet = True

        elif action == DOWN:
            if self.isValidMove(action):
                self.drawPiece(dY=1)
            else:
                self.setPiece()
                isSet = True
        elif action == LEFT:
            if self.isValidMove(action):
                self.drawPiece(dX=-1)
        elif action == RIGHT:
            if self.isValidMove(action):
                self.drawPiece(dX=1)
        elif action == ROTATE:
            if self.isValidMove(action):
                self.rotate()

        return isSet
    
    def rotate(self):
        #clear the old piece
        for x in range(4):
            for y in range(4):
                    if self.piece.piece[x][y] != BLANK:
                        self.board[self.piece.x+x][self.piece.y+y] = BLANK
        self.piece.rotate()

    #checks if provided coordinates are still on the board.
    def isOnBoard(self,bX=0,bY=0):
        if (0 <= bX < BOARDWIDTH) and (0 <= bY < BOARDHEIGHT):
            return True
        else:
            return False

    '''
    isValidMove()
    input
        action - directional or rotational action
    output
        boolean - True if valid action, otherwise False
    '''
    def isValidMove(self,action):
        valid = True

        #generate a list of valid moves base of piece's current position
        #TODO The following block of code can still be condensed

        if action == DOWN or action == DROP:
            for y in reversed(range(self.piece.gridSize)):
                for x in range(self.piece.gridSize):
                    if self.piece.piece[x][y] != BLANK: #if current box is not blank, check below it on the boardWithPieces
                        if self.isOnBoard(bX=(self.piece.x + x), bY=(self.piece.y + y + 1)):    #check if the next spot is on the board
                            if self.boardWithPieces[self.piece.x + x][self.piece.y + y + 1] != BLANK:     #check if the next spot is blank
                                valid = False
                        else:
                            valid = False
        elif action == LEFT:
            for x in range(self.piece.gridSize):
                for y in range(self.piece.gridSize):
                    if self.piece.piece[x][y] != BLANK: #if current box is not blank, check to the left of it
                        if self.isOnBoard(bX=(self.piece.x + x - 1), bY =(self.piece.y + y)):   #check if the next spot is on the board
                            if self.boardWithPieces[self.piece.x + x - 1][self.piece.y + y] != BLANK:     #check if the next spot is blank
                                valid = False
                        else:
                            valid = False
        elif action == RIGHT:
            for x in reversed(range(self.piece.gridSize)):
                for y in range(self.piece.gridSize):
                    if self.piece.piece[x][y] != BLANK: #if current box is not blank, check to the left of it
                        if self.isOnBoard(bX=(self.piece.x + x + 1), bY =(self.piece.y + y)):   #check if the next spot is on the board
                            if self.boardWithPieces[self.piece.x + x + 1][self.piece.y + y] != BLANK: #check if the next spot is blank
                                valid = False
                        else:
                            valid = False
        elif action == ROTATE:
             #Initialize temporary variables
            tempRotatedPiece = self.piece.setPiece(BLANK)

            #Rotate the piece
            for col in range(self.piece.gridSize):
                for index, cell in zip(reversed(range(self.piece.gridSize)),self.piece.piece[col]):
                    tempRotatedPiece[index][col] = cell

            for x in range(self.piece.gridSize):
                for y in range(self.piece.gridSize):
                    if tempRotatedPiece[x][y] != BLANK:
                        if self.isOnBoard(bX=(self.piece.x + x), bY= (self.piece.y + y)):
                            if self.boardWithPieces[self.piece.x + x][self.piece.y + y] != BLANK:
                                valid = False
                        else:
                            valid = False
        else:
            pass

        return valid

    #scan for completed rows, update completedLines, clear them.
    def clearCompletedRows(self):
        self.completedLines = 0
        y = BOARDHEIGHT - 1;
        while y >= 0:
            if self.isCompletedRow(y):
                self.completedLines += 1
                #clear row by shifting board down
                for y1 in reversed(range(y)):
                    for x in range(BOARDWIDTH):
                        self.boardWithPieces[x][y1+1] = self.boardWithPieces[x][y1]
                        self.board[x][y1+1] = self.board[x][y1]
            else:
                y -= 1

        self.totalCompletedLines += self.completedLines

    
    #returns a boolean if a row is completed
    def isCompletedRow(self, y):
        completed = True
        for x in range(BOARDWIDTH):
            if self.boardWithPieces[x][y] == BLANK:
                completed = False
        return completed
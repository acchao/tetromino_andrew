import pygame
from constants import *
'''
Class Piece
This class defines the game pieces and their shapes.
4x4 array

piece[col][row]
'''

class Piece:
    def __init__(self, pieceType):
        self.pieceType = pieceType
        self.rotation = 0
        self.rotationLimit = 0
        self.piece = self.setPiece(pieceType)
        if self.pieceType == I:
            self.gridSize = 4
        else:
            self.gridSize = 3
        #position on the board
        self.x = int(BOARDWIDTH/2) - 2
        #make sure the I piece starts from the top of the board
        if pieceType == I:      
            self.y = -1
        else:
            self.y = 0

    def rotate(self):
        #Initialize temporary variables
        tempPiece = self.setPiece(self.pieceType)
        self.rotation += 1
        if self.rotation < self.rotationLimit: #not all pieces can rotate the same amount, limit it.
            #for every column
            for col in range(self.gridSize):
                #take the column and assign it to the tempPiece Row
                for index, cell in zip(reversed(range(self.gridSize)),self.piece[col]):
                    tempPiece[index][col] = cell
        else:
            self.rotation = 0
        self.piece[:] = tempPiece

    def setPiece(self, pieceType):
        piece = []

        if pieceType == I:
            piece = [[0,I,0,0],
                     [0,I,0,0],
                     [0,I,0,0],
                     [0,I,0,0]]
            self.rotationLimit = 2
        elif pieceType == J:
            piece = [[0,J,0,0],
                     [0,J,0,0],
                     [J,J,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 4
        elif pieceType == L:
            piece = [[L,L,0,0],
                     [0,L,0,0],
                     [0,L,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 4
        elif pieceType == O:
            piece = [[0,0,0,0],
                     [O,O,0,0],
                     [O,O,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 1
        elif pieceType == S:
            piece = [[0,S,0,0],
                     [S,S,0,0],
                     [S,0,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 2
        elif pieceType == T:
            piece = [[0,T,0,0],
                     [T,T,0,0],
                     [0,T,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 4
        elif pieceType == Z:
            piece = [[Z,0,0,0],
                     [Z,Z,0,0],
                     [0,Z,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 2
        else:
            piece = [[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]]
            self.rotationLimit = 1
        return piece


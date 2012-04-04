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
        self.piece = self.setPiece(pieceType)
        self.rotation = 0
        self.rotationLimit = 0
        if self.pieceType == I:
            self.gridSize = 4
        else:
            self.gridSize = 3
        #position on the board
        self.x = 2
        self.y = 0

    def rotate(self):
        #Initialize temporary variables
        tempPiece = self.setPiece(BLANK)
        tempCol = [0,0,0,0]

        #for every column
        for col in range(self.gridSize):
            #take the column and assign it to the tempPiece Row
            for index, cell in zip(reversed(range(self.gridSize)),self.piece[col]):
                tempPiece[index][col] = cell
            
        self.piece[:] = tempPiece

    def setPiece(self, pieceType):
        piece = []

        if pieceType == I:
            piece = [[0,0,0,0],
                     [I,I,I,I],
                     [0,0,0,0],
                     [0,0,0,0]]

        elif pieceType == J:
            piece = [[0,0,0,0],
                     [J,J,J,0],
                     [0,0,J,0],
                     [0,0,0,0]]
        elif pieceType == L:
            piece = [[0,0,L,0],
                     [L,L,L,0],
                     [0,0,0,0],
                     [0,0,0,0]]
        elif pieceType == O:
            piece = [[0,0,0,0],
                     [O,O,0,0],
                     [O,O,0,0],
                     [0,0,0,0]]
        elif pieceType == S:
            piece = [[0,S,0,0],
                     [S,S,0,0],
                     [S,0,0,0],
                     [0,0,0,0]]
        elif pieceType == T:
            piece = [[0,0,0,0],
                     [T,T,T,0],
                     [0,T,0,0],
                     [0,0,0,0]]
        elif pieceType == Z:
            piece = [[Z,0,0,0],
                     [Z,Z,0,0],
                     [0,Z,0,0],
                     [0,0,0,0]]
        else:
            piece = [[0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]]

        return piece


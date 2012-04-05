import pygame
from constants import *

'''
Class Splashscreen
Introduce the Game

'''

class Splashscreen:
    def __init__(self,displaysurf, fontobj):
        self.displaysurf = displaysurf
        self.fontobj = fontobj
        self.offset = 200
        #self.draw()

    def draw(self):
        # Title
        titleSurf = self.fontobj.render('Tetris Clone', True, TEXTCOLOR)
        titleRect = titleSurf.get_rect()
        titleRect.topleft = (self.offset, YMARGIN)
        pygame.draw.rect(self.displaysurf, GRAY, titleRect)
        self.displaysurf.blit(titleSurf, titleRect)

        # Author
        authorSurf = self.fontobj.render('By Andrew Chao', True, TEXTCOLOR)
        authorRect = authorSurf.get_rect()
        authorRect.topleft = (self.offset, YMARGIN + BOXSIZE * 1)
        pygame.draw.rect(self.displaysurf, GRAY, authorRect)
        self.displaysurf.blit(authorSurf, authorRect)

        # Any key to start
        playSurf = self.fontobj.render('Press Any Key to Start...', True, TEXTCOLOR)
        playRect = playSurf.get_rect()
        playRect.topleft = (self.offset, YMARGIN*2 + BOXSIZE * 3)
        pygame.draw.rect(self.displaysurf, GRAY, playRect)
        self.displaysurf.blit(playSurf, playRect)

        # Q/Esc to Quit
        quitSurf = self.fontobj.render('Q - Quit ', True, TEXTCOLOR)
        quitRect = quitSurf.get_rect()
        quitRect.topleft = (self.offset, YMARGIN*2 + BOXSIZE * 5)
        pygame.draw.rect(self.displaysurf, GRAY, quitRect)
        self.displaysurf.blit(quitSurf, quitRect)

        # Up Arrows
        upSurf = self.fontobj.render('Up Arrow - Rotate ', True, TEXTCOLOR)
        upRect = upSurf.get_rect()
        upRect.topleft = (self.offset, YMARGIN*2 + BOXSIZE * 6)
        pygame.draw.rect(self.displaysurf, GRAY, upRect)
        self.displaysurf.blit(upSurf, upRect)

        # Other Arrows
        moveSurf = self.fontobj.render('Left, Down, Right Arrows - Move ', True, TEXTCOLOR)
        moveRect = moveSurf.get_rect()
        moveRect.topleft = (self.offset, YMARGIN*2 + BOXSIZE * 7)
        pygame.draw.rect(self.displaysurf, GRAY, moveRect)
        self.displaysurf.blit(moveSurf, moveRect)

        # Drop
        dropSurf = self.fontobj.render('Spacebar - Drop ', True, TEXTCOLOR)
        dropRect = dropSurf.get_rect()
        dropRect.topleft = (self.offset, YMARGIN*2 + BOXSIZE * 8)
        pygame.draw.rect(self.displaysurf, GRAY, dropRect)
        self.displaysurf.blit(dropSurf, dropRect)

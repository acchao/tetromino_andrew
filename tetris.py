import random, time, pygame, sys
from pygame.locals import *
from constants import *
from Board import *
from Splashscreen import *
from Queue import *


'''

Tetris
    Board
        pieces
        draw()
        isLineComplete()
        clearCompleteLines()
        movePiece()
    Piece
        shape
        color
        orientation
        draw()
        rotate()
    Score
        value
    Level
        value
    Lines
        value
    State
        Pause
        Play
        Quit

'''


def main():
    global FPSCLOCK, DISPLAYSURF, FONTOBJ
    pygame.init()	#initialize the game
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FONTOBJ = pygame.font.Font('freesansbold.ttf', 18)
    
    pygame.display.set_caption('Tetris')

    #set up initial pieces
    board = Board(DISPLAYSURF)
    queue = Queue(DISPLAYSURF, board)
    splashscreen = Splashscreen(DISPLAYSURF, FONTOBJ)
    DISPLAYSURF.fill(WINDOWCOLOR)
    splash = True
    
    while True: #main game loop
        if splash:
            splashscreen.draw()
        else:
            board.draw()
            queue.draw()
            drawScorePanel()
            drawInstructions()

        listenForQuit()
        splash = listenForKeyEvents(board,splash)
        

        #update screen
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def drawScorePanel():
    # Level
    levelSurf = FONTOBJ.render('Level: ', True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * PANELHEIGHT)
    DISPLAYSURF.blit(levelSurf, levelRect)

    # Score
    scoreSurf = FONTOBJ.render('Score: ', True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+1))
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
    # Lines
    lineSurf = FONTOBJ.render('Lines: ', True, TEXTCOLOR)
    lineRect = lineSurf.get_rect()
    lineRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+2))
    DISPLAYSURF.blit(lineSurf, lineRect)

def drawInstructions():
    # P to start
    # TODO rotate between play and pause
    playSurf = FONTOBJ.render('P - Pause/Play ', True, TEXTCOLOR)
    playRect = playSurf.get_rect()
    playRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+4))
    DISPLAYSURF.blit(playSurf, playRect)

    # Q/Esc to Quit
    quitSurf = FONTOBJ.render('Q - Quit ', True, TEXTCOLOR)
    quitRect = quitSurf.get_rect()
    quitRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+5))
    DISPLAYSURF.blit(quitSurf, quitRect)

    # Up Arrows
    upSurf = FONTOBJ.render('Up Arrow - Rotate ', True, TEXTCOLOR)
    upRect = upSurf.get_rect()
    upRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+6))
    DISPLAYSURF.blit(upSurf, upRect)

    # Other Arrows
    moveSurf = FONTOBJ.render('Other Arrows - Move ', True, TEXTCOLOR)
    moveRect = moveSurf.get_rect()
    moveRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+7))
    DISPLAYSURF.blit(moveSurf, moveRect)

def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * BOXSIZE + XMARGIN
    top = boxy * BOXSIZE + YMARGIN
    return (left, top)

def listenForQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
        pygame.event.post(event) #return the event if not quitting

def listenForKeyEvents(board, splash):
    action = None
    for event in pygame.event.get():

        if splash:
            if event.type == pygame.KEYUP:
                splash = False
                DISPLAYSURF.fill(WINDOWCOLOR)
                break
        #TODO handle keydown first, before adding KEYUP interactions        
        elif event.type == pygame.KEYDOWN:
            #p for pause/play
            if event.key == pygame.K_p:
                pauseGame()
            #space to drop the piece
            elif event.key == pygame.K_SPACE:
                action = DROP
            #down arrow to speed down
            elif event.key == pygame.K_DOWN:
                action = DOWN
            #left arrow - shift piece left
            elif event.key == pygame.K_LEFT:
                action = LEFT
            #right arrow - shift piece right
            elif event.key == pygame.K_RIGHT:
                action = RIGHT
            #up arrow - rotate piece
            elif event.key == pygame.K_UP:
                action = ROTATE
                
    if action:
        move(board, action)

    return splash

def pauseGame():
    #TODO
    pausedSurf = FONTOBJ.render('PAUSED', True, WHITE)
    pausedRect = pausedSurf.get_rect()
    pausedRect.topleft = (XMARGIN + (BOARDWIDTH * BOXSIZE)/2, YMARGIN + (BOXSIZE * BOARDHEIGHT / 2))
    DISPLAYSURF.blit(pausedSurf, pausedRect)
    while resumeGame() == None:
        pygame.display.update()
        FPSCLOCK.tick()
                
def resumeGame():
    #TODO
    for event in pygame.event.get([KEYDOWN,KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

#include any other movement function calls here.
def move(board, action):
    board.movePiece(action)



    

if __name__ == '__main__':
    main()

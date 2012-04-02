import random, time, pygame, sys
from pygame.locals import *
from constants import *


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
    board = getBlankBoard()
    DISPLAYSURF.fill(WINDOWCOLOR)
    
    while True: #main game loop
        drawBoard(board)
        drawNextShapePanel()
        drawScorePanel()
        drawInstructions()

        listenForQuit()
        listenForKeyEvents()
        

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
    quitRect = quitSurf.get_rect()
    quitRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+5))
    DISPLAYSURF.blit(quitSurf, quitRect)

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

def listenForKeyEvents():
    action = None
    for event in pygame.event.get():
        #TODO handle keydown first, before adding KEYUP interactions        
        if event.type == pygame.KEYDOWN:
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
        pygame.event.post(event)
    if action:
        move(action)

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
    for event in pygame.event.get([KEYDOWN,KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

def move(action):
    #TODO
    moveSurf = FONTOBJ.render('Move - %s' % action, True, TEXTCOLOR)
    moveRect = moveSurf.get_rect()
    moveRect.topleft = (XMARGIN*2 + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+7))
    DISPLAYSURF.blit(moveSurf, moveRect)
    

if __name__ == '__main__':
    main()

'''
Name: tetris.py
Author: Andrew Chao
Date: 4/4/2012
'''
import random, time, pygame, sys
from pygame.locals import *
from constants import *
from Board import *
from Splashscreen import *
from Queue import *

#Main Game Loop
def main():
    global FPSCLOCK, DISPLAYSURF, FONTOBJ
    pygame.init()	#initialize the game
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    FONTOBJ = pygame.font.Font('freesansbold.ttf', 18)
    
    pygame.display.set_caption('Tetrisss?')

    #set up initial pieces
    board = Board(DISPLAYSURF, FONTOBJ)
    queue = Queue(DISPLAYSURF)
    splashscreen = Splashscreen(DISPLAYSURF, FONTOBJ)
    DISPLAYSURF.fill(WINDOWCOLOR)
    start = False
    lastEventTime = time.time()
    lastDropTime = time.time()
    soundOn = True
    pygame.mixer.music.load('tetrisb.mid')
    pygame.mixer.music.play(-1, 0.0)
        
    while True: #main game loop
        #speed up the game as you level up
        fallspeed = generateSpeed(board.level)
        listenForQuit()
        soundOn = toggleSound(soundOn) 
        start = listenForStart(start)
        if not start:
            splashscreen.draw()
        else:
            board.checkGameState()
            board.draw()
            drawScorePanel(board)
            drawInstructions()
            if board.gameState == ACTIVE:
                queue.draw()
                #if its been longer than the fallspeed and the down key is not pressed, move the piece down
                keystate = pygame.key.get_pressed()
                if time.time() - lastDropTime > fallspeed and not keystate[K_DOWN]: 
                    move(board, queue, DOWN)
                    lastDropTime = time.time()
            
            lastEventTime = listenForKeyEvents(board,queue,lastEventTime)
            
        
        #update screen
        pygame.display.update()
        FPSCLOCK.tick(FPS)


'''
SCORING SYSTEM
Refer to Board.Py
'''
def drawScorePanel(board):
    # Clear the Panel
    pygame.draw.rect(DISPLAYSURF, GRAY, ((XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE),YMARGIN*2 + BOXSIZE * PANELHEIGHT,
        WINDOWHEIGHT - YMARGIN*2 + BOXSIZE * PANELHEIGHT,
        WINDOWWIDTH - XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE))))

    # Level
    levelSurf = FONTOBJ.render('Level: %s' % str(board.level), True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * PANELHEIGHT)
    DISPLAYSURF.blit(levelSurf, levelRect)

    # Score
    scoreSurf = FONTOBJ.render('Score: %s' % str(board.score), True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+1))
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
    # Lines - total lines Completed
    lineSurf = FONTOBJ.render('Lines: %s' % str(board.totalCompletedLines), True, TEXTCOLOR)
    lineRect = lineSurf.get_rect()
    lineRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+2))
    DISPLAYSURF.blit(lineSurf, lineRect)

def drawInstructions():
    # Clear the Panel
    pygame.draw.rect(DISPLAYSURF, GRAY, ((XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE),YMARGIN*2 + BOXSIZE * (PANELHEIGHT+4),
        WINDOWHEIGHT - YMARGIN*2 + BOXSIZE * (PANELHEIGHT+4),
        WINDOWWIDTH - XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE))))

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
    
    # Sound
    soundSurf = FONTOBJ.render('S - Sound ', True, TEXTCOLOR)
    soundRect = soundSurf.get_rect()
    soundRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+6))
    DISPLAYSURF.blit(soundSurf, soundRect)

    # Up Arrows
    upSurf = FONTOBJ.render('Up Arrow - Rotate ', True, TEXTCOLOR)
    upRect = upSurf.get_rect()
    upRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+7))
    DISPLAYSURF.blit(upSurf, upRect)

    # Other Arrows
    moveSurf = FONTOBJ.render('Other Arrows - Move ', True, TEXTCOLOR)
    moveRect = moveSurf.get_rect()
    moveRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+8))
    DISPLAYSURF.blit(moveSurf, moveRect)

    # Drop
    dropSurf = FONTOBJ.render('Spacebar - Drop ', True, TEXTCOLOR)
    dropRect = dropSurf.get_rect()
    dropRect.topleft = (XMARGIN + BOXSIZE + (BOARDWIDTH * BOXSIZE), YMARGIN*2 + BOXSIZE * (PANELHEIGHT+9))
    DISPLAYSURF.blit(dropSurf, dropRect)

def listenForQuit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_q):
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
        pygame.event.post(event) #return the event if not quitting

def toggleSound(soundOn):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if soundOn:
                    pygame.mixer.music.stop()
                    soundOn = False
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    soundOn = True
            else:
                pygame.event.post(event)
        else:
            pygame.event.post(event)
        break
    return soundOn

def listenForStart(start):
    if not start:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                start = True
                DISPLAYSURF.fill(WINDOWCOLOR)
                break
    return start

def listenForKeyEvents(board, queue,lastEventTime):
    action = None
    #look for one off events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #p for pause/play
            if event.key == pygame.K_p:
                if board.gameState == PAUSE:
                    board.gameState = ACTIVE
                elif board.gameState == ACTIVE:
                    board.gameState = PAUSE
                if board.gameState == OVER or board.gameState == WIN:
                    board.reset()
                    queue.reset()
            #space to drop the piece
            elif event.key == pygame.K_SPACE:
                action = DROP
            #space to drop the piece
            elif event.key == pygame.K_LEFT:
                action = LEFT
            #space to drop the piece
            elif event.key == pygame.K_RIGHT:
                action = RIGHT
            #up arrow - rotate piece
            elif event.key == pygame.K_UP:
                action = ROTATE
            break

    #look for continuous key presses
    keystate = pygame.key.get_pressed()
    if keystate[K_DOWN]:
        #down arrow to speed down
        if time.time() - lastEventTime >= SOFTDROPSPEED:
            action = DOWN
            board.softDropDistance += 1
        #left arrow - shift piece left
    elif keystate[K_LEFT] and action == None:   #checking for none allows for faster key pressing
        if time.time() - lastEventTime >= LATERALSPEED:
            action = LEFT
        #right arrow - shift piece right
    elif keystate[K_RIGHT] and action == None:
        if time.time() - lastEventTime >= LATERALSPEED:
            action = RIGHT

    if action and board.gameState == ACTIVE:
        move(board, queue, action)
        lastEventTime = time.time()

    return lastEventTime
    

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
def move(board, queue, action):
    isSet = board.movePiece(action)
    if isSet:
        #clear completed rows
        board.clearCompletedRows()
        #grab a new piece
        board.newPiece(queue.getNextPiece())

#hardcoding, needs to be changed to be more flexible
def generateSpeed(level):
    if level < 10:
        speed = DEFAULTFALLSPEED - .1*(level-1)
    elif level < 11:
        speed = .1 - .01*(level%10)
    else:
        speed = 9001
    return speed

if __name__ == '__main__':
    main()

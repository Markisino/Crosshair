"""
Project #1
Made by:
- Earl Aromin Steven
- Marco Tropiano
- Thomas Backs
"""
import pygame # this should work in Anaconda as well
import sys
import random
import copy
from pygame.locals import *

import config
        
def main():
    global FPSCLOCK, DISPLAYSURF, REDPILERECT, BLACKPILERECT, REDTOKENIMG
    global BLACKTOKENIMG, BOARDIMG, ARROWIMG, ARROWRECT, HUMANWINNERIMG
    global COMPUTERWINNERIMG, WINNERRECT, TIEWINNERIMG

    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((config.WINDOWWIDTH, config.WINDOWHEIGHT))
    pygame.display.set_caption('X-Rudder')

    REDPILERECT = pygame.Rect(int(config.SPACESIZE / 2), config.WINDOWHEIGHT - int(3 * config.SPACESIZE / 2), config.SPACESIZE, config.SPACESIZE)
    BLACKPILERECT = pygame.Rect(config.WINDOWWIDTH - int(3 * config.SPACESIZE / 2), config.WINDOWHEIGHT - int(3 * config.SPACESIZE / 2), config.SPACESIZE, config.SPACESIZE)
    REDTOKENIMG = pygame.image.load('img/red_token.png')
    REDTOKENIMG = pygame.transform.smoothscale(REDTOKENIMG, (config.SPACESIZE, config.SPACESIZE))
    BLACKTOKENIMG = pygame.image.load('img/black-token.png')
    BLACKTOKENIMG = pygame.transform.smoothscale(BLACKTOKENIMG, (config.SPACESIZE, config.SPACESIZE))
    BOARDIMG = pygame.image.load('img/board.png')
    BOARDIMG = pygame.transform.smoothscale(BOARDIMG, (config.SPACESIZE, config.SPACESIZE))

    HUMANWINNERIMG = pygame.image.load('img/human-winner.png')
    COMPUTERWINNERIMG = pygame.image.load('img/computer-winner.png')
    TIEWINNERIMG = pygame.image.load('img/tie.png')
    WINNERRECT = HUMANWINNERIMG.get_rect()
    WINNERRECT.center = (int(config.WINDOWWIDTH / 2), int(config.WINDOWHEIGHT / 2))

    is_first_game = True

    while True:
        runGame(is_first_game)
        is_first_game = False

def runGame(is_first_game):
    if is_first_game:
        # Let the computer starts so the player will see
        turn = config.COMPUTER
        show_help = True
    else:
        if random.randint(0, 1) == 0:
            turn = config.COMPUTER
        else:
            turn = config.HUMAN
        show_help = False

    # set up a blank board.
    main_board = getNewBoard()
    
    while True:
        drawBoard(main_board)
        # DISPLAYSURF.blit(winner_img, WINNERRECT)
        pygame.display.update()
        FPSCLOCK.tick()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                return

        

def drawBoard(board, extraToken=None):
    DISPLAYSURF.fill(config.BGCOLOR)

    # draw tokens
    spaceRect = pygame.Rect(0, 0, config.SPACESIZE, config.SPACESIZE)
    for x in range(config.BOARDWIDTH):
        for y in range(config.BOARDHEIGHT):
            spaceRect.topleft = (config.XMARGIN + (x * config.SPACESIZE), config.YMARGIN + (y * config.SPACESIZE))
            if board[x][y] == config.RED:
                DISPLAYSURF.blit(REDTOKENIMG, spaceRect)
            elif board[x][y] == config.BLACK:
                DISPLAYSURF.blit(BLACKTOKENIMG, spaceRect)
    
    # draw the extra token
    if extraToken != None:
        if extraToken['color'] == config.RED:
            DISPLAYSURF.blit(REDTOKENIMG, (extraToken['x'], extraToken['y'], config.SPACESIZE, config.SPACESIZE))
        elif extraToken['color'] == config.BLACK:
            DISPLAYSURF.blit(BLACKTOKENIMG, (extraToken['x'], extraToken['y'], config.SPACESIZE, config.SPACESIZE))

    # draw board over the tokens
    for x in range(config.BOARDWIDTH):
        for y in range(config.BOARDHEIGHT):
            spaceRect.topleft = (config.XMARGIN + (x * config.SPACESIZE), config.YMARGIN + (y * config.SPACESIZE))
            DISPLAYSURF.blit(BOARDIMG, spaceRect)

    # draw the red and black tokens off to the side
    DISPLAYSURF.blit(REDTOKENIMG, REDPILERECT)
    DISPLAYSURF.blit(BLACKTOKENIMG, BLACKPILERECT)

def getNewBoard():
    board = []
    for x in range(config.BOARDWIDTH):
        board.append([config.EMPTY] * config.BOARDHEIGHT)   
    print(board)
    return board
        

if __name__ == '__main__':
    main()
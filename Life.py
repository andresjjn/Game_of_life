#!/usr/bin/env python3
"""John Conway's Game of Life.

The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970.[1]
It is a zero-player game, meaning that its evolution is determined by
its initial state, requiring no further inumpyut. One interacts with the
Game of Life by creating an initial configuration and observing how it evolves.
It is Turing complete and can simulate a universal constructor or any other
Turing machine.

Thanks to @dotcsv (Carlos Santana Vega) for a good video tutorial about this
project."""

import pygame
import numpy
import time


pygame.init()
wh, ht = (500, 500)
screen = pygame.display.set_mode((ht, wh))
back_color = (25, 25, 25)
screen.fill(back_color)
nxC, nyC = (50, 50)
status = numpy.zeros((nxC, nyC))
dimCW = int(wh / nxC)
dimCH = int(ht / nyC)

status[44, 33] = 1
status[45, 34] = 1
status[45, 35] = 1
status[44, 35] = 1
status[43, 35] = 1

pause = False

while True:
    newstatus = numpy.copy(status)
    screen.fill(back_color)
    time.sleep(0.08)

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pause = not pause
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    click = pygame.mouse.get_pressed()

    if sum(click) > 0:
        pX, pY = pygame.mouse.get_pos()
        celX, celY = int(numpy.floor(pX / dimCW)), int(numpy.floor(pY / dimCH))
        newstatus[celX, celY] = 1

    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pause:
                n_neigh = status[(x - 1) % nxC, (y - 1) % nyC] + \
                        status[(x) % nxC, (y - 1) % nyC] + \
                        status[(x + 1) % nxC, (y - 1) % nyC] + \
                        status[(x - 1) % nxC, (y) % nyC] + \
                        status[(x + 1) % nxC, (y) % nyC] + \
                        status[(x - 1) % nxC, (y + 1) % nyC] + \
                        status[(x) % nxC, (y + 1) % nyC] + \
                        status[(x + 1) % nxC, (y + 1) % nyC]

                if status[x, y] == 0 and n_neigh == 3:
                    newstatus[x, y] = 1
                elif status[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newstatus[x, y] = 0

            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]
            if newstatus[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    status = numpy.copy(newstatus)
    pygame.display.flip()

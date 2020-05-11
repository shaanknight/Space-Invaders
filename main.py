import pygame
import sys
import time
import math
from pygame.locals import *
from spaceship import *
from alien import *
from missile import *


pygame.init()
pygame.font.init()

FPS = 30
clock = pygame.time.Clock()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Space Invader')

black = (0, 0, 0)
score = 0

fir = []
kir = []
c = 0
ali = Alien(time.time(), 1)

while True:

    display.fill(black)
    draw(ship, display)
    font = pygame.font.Font(None, 36)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                mis = missile1(time.time(), ship.move_x, 500, 1)
                draw_bul(mis, display)
                fir.append(mis)
            if event.key == pygame.K_s:
                mis = missile2(time.time(), ship.move_x, 500, 1)
                draw_bul(mis, display)
                kir.append(mis)
        ship.event_handler(event)

    if time.time() - ali.time >= 10:
        c = 1
        ali = Alien(time.time(), 1)

    if time.time() - ali.time < 8 and ali.ext == 1:
        draw_alien(ali, display)

    try:
        if time.time() - btime < 5 and bext == 1:
            display.blit(bimage, (balix, baliy))
    except BaseException:
        pass

    for i in fir:
        if i.posx == ali.move_x and i.posy <= ali.move_y and ali.ext == 1 and i.ext == 1:
            ali.ext = 0
            i.ext = 0
            score = score + 1

        if i.posy > -100 and i.ext == 1:
            draw_bul(i, display)
            i.posy = 500 - (time.time() - i.time) * 100
        else:
            i.ext = 0

    for i in kir:
        if i.posx == ali.move_x and i.posy <= ali.move_y and ali.ext == 1 and i.ext == 1:
            balix = ali.move_x
            baliy = ali.move_y
            btime = time.time()
            bext = 1
            bimage = pygame.image.load('dead.png')
            ali.ext = 0
            i.ext = 0
            score = score + 1

        if i.posy > -100 and i.ext == 1:
            draw_bul(i, display)
            i.posy = 500 - (time.time() - i.time) * 200
        else:
            i.ext = 0

    text = font.render("Score: " + str(score), True, (255, 255, 255))
    display.blit(text, [350, 350])
    pygame.display.update()
    clock.tick(FPS)

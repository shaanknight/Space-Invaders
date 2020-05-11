import pygame
import random

pygame.init()


class Alien():

    def __init__(self, t, ext):
        self.image = pygame.image.load('840px_COLOURBOX11524534100x100.png')
        self.move_x = random.randint(0, 7) * 100
        self.move_y = random.randint(0, 1) * 100
        self.time = t
        self.ext = ext


def draw_alien(ali, display):
    display.blit(ali.image, (ali.move_x, ali.move_y))

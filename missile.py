import pygame

pygame.init()


class bullet():

    def __init__(self, t, x, y, ext):
        self.time = t
        self.posx = x
        self.posy = y
        self.ext = ext


class missile1(bullet):

    def __init__(self, t, x, y, ext):
        super().__init__(t, x, y, ext)
        self.image = pygame.image.load('images.png')


class missile2(bullet):

    def __init__(self, t, x, y, ext):
        super().__init__(t, x, y, ext)
        self.image = pygame.image.load('bomb100x100.png')


def draw_bul(mis, display):
    display.blit(mis.image, (mis.posx, mis.posy))

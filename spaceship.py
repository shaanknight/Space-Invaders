import pygame

pygame.init()


class Ship():

    def __init__(self):
        self.image = pygame.image.load('800px_COLOURBOX11524534100x100.png')
        self.move_x = 0

    def event_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if self.move_x > 0:
                    self.move_x -= 100
            elif event.key == pygame.K_d:
                if self.move_x < 700:
                    self.move_x += 100


ship = Ship()


def draw(ship, display):
    # print(ship.move_x)
    display.blit(ship.image, (ship.move_x, 600))

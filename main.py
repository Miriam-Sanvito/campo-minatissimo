import pygame, sys
from pygame.locals import *
from tavolo import Piattaforma


window_width = 700
window_height = 500
window_size = (window_width, window_height)
screen = pygame.display.set_mode(window_size)
display = pygame.Surface((600, 400))
pygame.display.set_caption("campo minato")

clock = pygame.time.Clock()
fps = 60
piattaforma = Piattaforma(display)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    piattaforma.draw()
    pygame.display.flip()
    clock.tick(fps)


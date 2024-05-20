import pygame
from math import ceil
class Piattaforma():
    def __init__(self, display, nomefile = 'map.txt') -> None:
        self.display = display
        self.colore0 = ((207,250, 137))
        self.colore1 = ((145, 199, 58))
        with open(nomefile) as f:
            self.game_map = [list(map(int, riga.strip().split())) for riga in f]
        self.num_righe = len(self.game_map)
        self.num_colonne = len(self.game_map[0])
        self.quad_width = ceil(display.get_width()/ self.num_colonne) 
        self.quad_height = ceil(display.get_height()/ self.num_righe)

        self.quad_rects = []
        for y, riga in enumerate(self.game_map):
            for x, quad in enumerate(riga):
                if quad != 0:
                    self.quad_rects.append(pygame.Rect(x * self.quad_width, y * self.quad_height, self.quad_width, self.quad_height))

        # self.quad_rects = []
        # for riga in self.game_map:
        #     for quad in riga:
        #          self.quad_rects.append(pygame.Rect(self.quad_width * self.quad_height, self.quad_width, self.quad_height))
    

        # for y, riga in enumerate(self.game_map):
        #     for x, quad in enumerate(riga):
        #             self.quad_rects.append(pygame.Rect(x * self.quad_width, y * self.quad_height, self.quad_width, self.quad_height))
    def draw(self):
        # for y, riga in enumerate(self.game_map):
        #     for x, quad in enumerate(riga):
        #         if quad == 0:
        #             self.quad
        #         if quad == 2:
                    
        for riga in self.game_map:
            c=0
            for el in riga:
               c+=1
               if el == 0:
                    self.quad_rects[c].fill((self.colore0))
               if el == 1:
                    self.quad_rects[c].fill((self.colore0))




        
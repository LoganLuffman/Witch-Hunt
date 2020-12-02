import pygame
from tile import *
class Game_Map:
    def __init__(self, the_game):
        self.rows = 768 // 16
        self.cols = 1360 // 16
        self.tiles = [[Tile(i, j) for i in range(self.cols)] for j in range(self.rows)]
        self.screen = the_game
    def drawTiles(self):
        for i in range(self.rows):
            for j in range(self.cols):
                pygame.draw.rect(self.screen, (51,51,51),
                 [self.tiles[i][j].col * 16, self.tiles[i][j].row * 16, 16, 16], 1, 1)

            
        




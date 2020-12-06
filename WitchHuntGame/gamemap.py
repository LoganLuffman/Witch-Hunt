import pygame, os, csv
from tile import *
import time
class Game_Map:
    def __init__(self, filename, spritesheet):
        self.tile_size = 16
        
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0,0,0))
        self.load_map()
    
    def draw_map(self, surface):
        #print("we doing this?")
        surface.blit(self.map_surface, (0,0))

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_map(self):
        for tile in self.tiles:
            #print(tile)
            tile.draw(self.map_surface)

    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                #print(str(tile))
                if str(tile) != '-1':
                    name = "sprite-" + str(tile) + ".png"
                    #print(name)
                    #print(str(x) + " " + str(y))
                    #time.sleep(0.2)
                    tiles.append(Tile(name, x * self.tile_size, y * self.tile_size, self.spritesheet))
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles
            
        




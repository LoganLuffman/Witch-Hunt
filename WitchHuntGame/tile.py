import pygame

class Tile:
    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.occupied = False
    
    def __str__(self):
        return "Row: " + str(self.row) + "\nCol: " + str(self.col) + "\n"
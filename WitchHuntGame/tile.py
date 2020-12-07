import pygame, csv, os

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, col, row, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = spritesheet.parse_sprite(image)
        #print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = col
        self.rect.y = row
        self.name = image
    
    def draw(self, surface):
        #print(str(self.rect.x) + " : " + str(self.rect.y))
        surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def getPos(self):
        return (self.rect.x, self.rect.y)

    def get_grid(self):
        return (self.rect.x // 16, self.rect.y // 16)
    
    def __str__(self):
        return "< " + self.name + " : " + str(self.rect.x) + " : " + str(self.rect.y) + " >"
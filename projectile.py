import pygame, time


class Projectile:
    def __init__(self, screen, x, y, dir):
        self.dir = dir
        if self.dir == "down":
            self.image = pygame.image.load('images\OtherProjectileDown.png')
        elif self.dir == "up":
            self.image = pygame.image.load('images\OtherProjectileUp.png')
        elif self.dir == "left":
            self.image = pygame.image.load('images\OtherProjectileLeft.png')
        else:
            self.image = pygame.image.load('images\OtherProjectileRight.png')

        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = x * 16
        self.rect.y = y * 16

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def move(self):
        if self.dir == "left":
            self.rect.x -= 16

        elif self.dir == "right":
            self.rect.x += 16

        elif self.dir == "down":
            self.rect.y += 16

        elif self.dir == "up":
            self.rect.y -= 16

    def checkHit(self, player):
        if self.getPos() == player.getPos():
            player.hp -= 1
            return True
        return False

    def checkBoundary(self):
        if self.rect.x < 0 or self.rect.x > 1359 or self.rect.y < 0 or self.rect.y > 767:
            return True
        return False

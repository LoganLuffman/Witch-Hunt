import pygame, random
from projectile import *
class Boss:
    def __init__(self, the_game):
        
        self.width, self.height = 32, 32
        self.image = pygame.image.load("images/WitchIdleLeft.png")
        self.idle_right = pygame.image.load("images/WitchIdleRight.png")
        self.idle_left = pygame.image.load("images/WitchIdleLeft.png")
        self.attack_right = pygame.image.load("images/WitchAttackRight.png")
        self.attack_left = pygame.image.load("images/WitchAttackLeft.png")
        self.screen = the_game
        self.rect = self.image.get_rect()
        self.rect.x = 42 * 16
        self.rect.y = 0 * 16
        self.hp = 10

    def drawBoss(self):
        self.screen.blit(self.image, self.rect)

    def takeHit(self):
        self.hp -= 1
        print(str(self.hp))
        if self.hp <= 0:
            return True
        return False
    
    def getPos(self):
        return ((self.rect.x, self.rect.y), (self.rect.x + 16, self.rect.y), \
            (self.rect.x, self.rect.y + 16), (self.rect.x + 16, self.rect.y + 16))

    def attack(self):
        pattern = random.randint(1, 5)
        projectiles = []
        print(pattern)
        if pattern == 1:
            for i in range(0, 47, 2):
                projectiles.append(Projectile(self.screen, 0, i, "right"))
        elif pattern == 2:
            for i in range(0, 47, 2):
                projectiles.append(Projectile(self.screen, 84, i, "left"))
        elif pattern == 3:
            for i in range(0, 85, 2):
                projectiles.append(Projectile(self.screen, i, 0, "down"))
        elif pattern == 4:
            for i in range(0, 85, 2):
                projectiles.append(Projectile(self.screen, i, 47, "up"))
        elif pattern == 5:
            for i in range(0, 85, 2):
                projectiles.append(Projectile(self.screen, i, 47, "up"))
            for i in range(0, 47, 2):
                projectiles.append(Projectile(self.screen, 84, i, "left"))
        return projectiles

        
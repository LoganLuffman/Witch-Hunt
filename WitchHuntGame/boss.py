import pygame

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
        if self.hp == 0:
            return True
        return False
    
    
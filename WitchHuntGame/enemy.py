import pygame

class Enemy:
    def __init__(self, the_game, x, y):
        
        self.width, self.height = 16, 16
        #self.color = (0, 255, 0)
        self.screen = the_game
        self.image = pygame.image.load('images/EnemyIdleFront.png')
        self.up_image = pygame.image.load('images/EnemyIdleFront.png')
        self.down_image = pygame.image.load('images/EnemyIdleBack.png')
        self.left_image = pygame.image.load('images/EnemyIdleLeft.png')
        self.right_image = pygame.image.load('images/EnemyIdleRight.png')
        self.up_attack = pygame.image.load('images/EnemyAttackFrontBase.png')
        self.down_attack = pygame.image.load('images/EnemyAttackBackBase.png')
        self.left_attack = pygame.image.load('images/EnemyAttackLeftBase.png')
        self.right_attack = pygame.image.load('images/EnemyAttackRightBase.png')
        self.rect = self.image.get_rect()
        self.rect.x = x * 16
        self.rect.y = y * 16

    def drawEnemy(self):
        self.screen.blit(self.image, self.rect)
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
        self.dir = "down"
    
    def drawEnemy(self):
        self.screen.blit(self.image, self.rect)
    
    def set_idle_image(self):
        if self.dir == "up":
            self.image = self.up_image
        elif self.dir == "down":
            self.image = self.down_image
        elif self.dir == "left":
            self.image = self.left_image
        elif self.dir == "right":
            self.image = self.right_image

    def getPos(self):
        return (self.rect.x, self.rect.y)
    
    def getPosInFront(self):
        if self.dir == "up":
            return (self.rect.x, self.rect.y - 16)
        elif self.dir == "down":
            return (self.rect.x, self.rect.y + 16)
        elif self.dir == "left":
            return (self.rect.x - 16, self.rect.y)
        elif self.dir == "right":
            return (self.rect.x + 16, self.rect.y)
    
    def attack(self):
        if self.dir == "up":
            self.image = self.up_attack
            print("attack up")
            self.drawPlayer()
            time.sleep(0.5)
            #self.image = self.up_image
        elif self.dir == "down":
            self.image = self.down_attack
            print("attack down")
            
            time.sleep(0.5)
            #self.image = self.down_image
        elif self.dir == "left":
            self.image = self.left_attack
            print("attack left")
            
            time.sleep(0.5)
            #self.image = self.left_image
        elif self.dir == "right":
            self.image = self.right_attack
            print("attack right")
            
            time.sleep(0.5)
            #self.image = self.right_image

    def move(self, dir):
        self.dir = dir
        if dir == "up":
            if self.rect.y != 0:
                self.image = self.up_image
                self.rect.y -= 16
        elif dir == "down":
            if self.rect.y == 47 * 16:
                self.image = self.down_image
                self.rect.y += 16
        elif dir == "left":
            if self.rect.x != 0:
                self.image = self.left_image
                self.rect.x -= 16
        elif dir == "right":
            if self.rect.x == 84 * 16:
                self.image = self.right_image
                self.rect.x += 16

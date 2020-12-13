import pygame, time

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
        self.up_attack = pygame.image.load('images/EnemyAttackBackBase.png')
        self.down_attack = pygame.image.load('images/EnemyAttackFrontBase.png')
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
            #print("attack up")
            
            time.sleep(0.5)
            #self.image = self.up_image
        elif self.dir == "down":
            self.image = self.down_attack
            #print("attack down")
            
            time.sleep(0.5)
            #self.image = self.down_image
        elif self.dir == "left":
            self.image = self.left_attack
            #print("attack left")
            
            time.sleep(0.5)
            #self.image = self.left_image
        elif self.dir == "right":
            self.image = self.right_attack
            #print("attack right")
            
            time.sleep(0.5)
            #self.image = self.right_image

    def move(self, nextSpot):
        if self.dir == "left":
            
            self.rect.x = nextSpot[0] * 16
        elif self.dir == "right":
            
            self.rect.x = nextSpot[0] * 16
        elif self.dir == "up":
            
            self.rect.y = nextSpot[1] * 16
        elif self.dir == "down":
            
            self.rect.y = nextSpot[1] * 16
        else:
            pass
        
    def getDir(self, nextSpot):
        if self.rect.x // 16 > nextSpot[0]:
            self.dir = "left"
            
        elif self.rect.x // 16 < nextSpot[0]:
            self.dir = "right"
            
        elif self.rect.y // 16 > nextSpot[1]:
            self.dir = "up"
            
        elif self.rect.y // 16 < nextSpot[1]:
            self.dir = "down"
            
        else:
            pass
    def get_grid(self):
        return (self.rect.x // 16, self.rect.y // 16)

    def __eq__(self, enemy):
        return self.get_grid() == enemy.get_grid() and self.dir == enemy.dir

    def checkNeighbors(self, player):
        (x, y) = self.get_grid()
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for neighbor in neighbors:
            if neighbor == player.get_grid():
                return True
        return False
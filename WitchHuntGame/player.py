import pygame
import time
class Player:
    def __init__(self, the_game):
        #self.posX = 42
        #self.posY = 47
        self.image = pygame.image.load('images/PlayerIdleUp.png')
        self.up_image = pygame.image.load('images/PlayerIdleUp.png')
        self.down_image = pygame.image.load('images/PlayerIdleBack.png')
        self.left_image = pygame.image.load('images/PlayerIdleLeft.png')
        self.right_image = pygame.image.load('images/PlayerIdleRight.png')
        self.up_attack = pygame.image.load('images/PlayerAttackFront.png')
        self.down_attack = pygame.image.load('images/PlayerAttackBack.png')
        self.left_attack = pygame.image.load('images/PlayerAttackLeft.png')
        self.right_attack = pygame.image.load('images/PlayerAttackRight.png')
        self.rect = self.image.get_rect()
        self.rect.x = 42 * 16
        self.rect.y = 47 * 16
        self.width, self.height = 16, 16
        self.dir = "up"
        self.screen = the_game
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.hp = 5
        

    def drawPlayer(self):
        #self.screen.set_colorkey((255,255,255))
        self.screen.blit(self.image, self.rect)
        
        #pygame.draw.rect(self.screen, self.color, [self.posX * 16, self.posY * 16, self.width, self.height])
    def isMoving(self):
        return self.movingDown or self.movingLeft or self.movingRight or self.movingUp
    def movePlayer(self):
        
        if self.movingUp == True:
            if self.rect.y != 0:
                
                self.image = self.up_image
                self.rect.y -= 16
            

        elif self.movingDown == True:
            if self.rect.y != 47 * 16:
                
                self.image = self.down_image
                self.rect.y += 16
            

        elif self.movingLeft == True:
            if self.rect.x != 0:
                
                self.image = self.left_image
                self.rect.x -= 16
            

        elif self.movingRight == True:
            if self.rect.x != 84 * 16:
                
                self.image = self.right_image
                self.rect.x += 16
            

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
            self.drawPlayer()
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

    def checkGameOver(self):
        if self.hp == 0:
            return True
        return False

    def getHp(self):
        return self.hp
    
    def get_grid(self):
        return (self.rect.x // 16, self.rect.y // 16)
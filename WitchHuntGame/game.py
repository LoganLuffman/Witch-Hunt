import pygame, sys, time, csv, os

from gamemap import *
from player import *
from boss import *
from enemy import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1360, 768))
        pygame.display.set_caption("Witch Hunt")
        self.game_map = Game_Map(self.screen)
        self.player = Player(self.screen)
        self.boss = Boss(self.screen)
        self.minions = []
        self.gameOver = False
        self.minions.append(Enemy(self.screen, 20, 20))
        self.minions.append(Enemy(self.screen, 22, 20))
        self.minions.append(Enemy(self.screen, 24, 20))
        self.minions.append(Enemy(self.screen, 26, 20))
        self.minions.append(Enemy(self.screen, 28, 20))
        self.minions.append(Enemy(self.screen, 30, 20))
        self.minions.append(Enemy(self.screen, 20, 22))
        self.minions.append(Enemy(self.screen, 22, 22))
        self.minions.append(Enemy(self.screen, 24, 22))
        self.minions.append(Enemy(self.screen, 26, 22))
        self.minions.append(Enemy(self.screen, 28, 22))
        self.score = 0
    def update_screen(self):
        self.screen.fill((42, 156, 101))
        self.game_map.drawTiles()
        self.boss.drawBoss()
        for enemy in self.minions:
            enemy.drawEnemy()
        self.player.drawPlayer()
        
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.movingLeft = True
                        self.player.dir = "left"
                    if event.key == pygame.K_RIGHT:
                        self.player.movingRight = True
                        self.player.dir = "right"
                    if event.key == pygame.K_UP:
                        self.player.movingUp = True
                        self.player.dir = "up"
                    if event.key == pygame.K_DOWN:
                        self.player.movingDown = True
                        self.player.dir = "down"
                    if event.key == pygame.K_SPACE:
                        self.player.attack()
                        if not self.check_collisions():
                            if self.entity_collide(self.player, self.boss):
                                self.gameOver = self.boss.takeHit()
                            else:
                                for enemy in self.minions:
                                    if self.entity_collide(self.player, enemy):
                                        self.minions.remove(enemy)
                                        self.score += 100
                                        self.update_screen()
                        self.update_screen()
                        time.sleep(0.5)
                        self.player.set_idle_image()
                if event.type == pygame.KEYUP:
                    self.player.movingLeft = False
                    self.player.movingUp = False
                    self.player.movingDown = False
                    self.player.movingRight = False

    def entity_collide(self, entity1, entity2):
        if isinstance(entity2, Boss):
            if (entity1.rect.x - 16 == entity2.rect.x or entity1.rect.x - 16 == entity2.rect.x + 16)\
                and (entity1.rect.y == entity2.rect.y or entity1.rect.y == entity2.rect.y + 16) \
                and entity1.dir == "left":
                return True
        
        
            elif (entity1.rect.x + 16 == entity2.rect.x or entity1.rect.x + 16 == entity2.rect.x + 16)\
                and (entity1.rect.y == entity2.rect.y or entity1.rect.y == entity2.rect.y + 16) \
                and entity1.dir == "right":
                return True
            
            elif (entity1.rect.y - 16 == entity2.rect.y or entity1.rect.y - 16 == entity2.rect.y + 16)\
                and (entity1.rect.x == entity2.rect.x or entity1.rect.x == entity2.rect.x + 16) \
                and entity1.dir == "up":
                return True
            
            
        if entity1.rect.x - 16 == entity2.rect.x and entity1.rect.y == entity2.rect.y and entity1.dir == "left":
            return True
        
        
        elif entity1.rect.x + 16 == entity2.rect.x and entity1.rect.y == entity2.rect.y and entity1.dir == "right":
            return True
        
        elif entity1.rect.y - 16 == entity2.rect.y and entity1.rect.x == entity2.rect.x and entity1.dir == "up":
            return True
        
        elif entity1.rect.y + 16 == entity2.rect.y and entity1.rect.x == entity2.rect.x and entity1.dir == "down":
            return True

        else:
            return False
    
    def check_collisions(self):
        if self.entity_collide(self.player, self.boss):
            return False
        for enemy in self.minions:
            if self.entity_collide(self.player, enemy):
                return False
        return True

    def run_game(self):
        while not self.gameOver:
            self.check_events()
            if self.check_collisions():
                self.player.movePlayer()
            self.update_screen()

            
            
            
    


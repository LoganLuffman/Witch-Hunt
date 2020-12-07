import pygame, sys, time, csv, os

from squareGrid import *
from gamemap import *
from player import *
from boss import *
from enemy import *
from spritesheet import *
import timeit
import random
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1360, 768))
        pygame.display.set_caption("Witch Hunt")
        self.spritesheet = Spritesheet('map/finalSheet.png')
        self.game_map1 = Game_Map('map/finalMap_Tile Layer 1.csv', self.spritesheet)
        self.game_map2 = Game_Map('map/finalMap_Tile Layer 2.csv', self.spritesheet)
        self.player = Player(self.screen)
        self.boss = Boss(self.screen)
        self.minions = []
        #self.initialSpawn()
        self.minions.append(Enemy(self.screen, 10, 10))
        self.projectiles = []
        self.gameOver = False
        self.score = 0
        self.bossTime = 0
        self.bossAttackMoveTime = 0
        self.static_grid = SquareGrid(85, 48)
        for tile in self.game_map2.tiles:
            self.static_grid.walls.append(tile.get_grid())
        for grid in self.boss.get_grid():
            self.static_grid.walls.append(grid)
        #print(self.static_grid.walls)
        self.enemyTimer = 0
        self.clock = pygame.time.Clock()

        self.temp = 0

    def update_screen(self):
        self.screen.fill((92, 133, 86))
        self.game_map1.draw_map(self.screen)
        self.game_map2.draw_map(self.screen)
        self.boss.drawBoss()
        for enemy in self.minions:
            enemy.drawEnemy()
        self.player.drawPlayer()
        
        
        for projectile in self.projectiles:
            projectile.draw()
        #time.sleep(0.01)
        
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
                        time.sleep(0.2)
                        self.player.set_idle_image()
                    if event.key == pygame.K_e:
                        print(self.player.get_grid())
                    if event.key == pygame.K_q:
                        self.minions.append(Enemy(self.screen, 42, 24))
                if event.type == pygame.KEYUP:
                    self.player.movingLeft = False
                    self.player.movingUp = False
                    self.player.movingDown = False
                    self.player.movingRight = False
                    
    '''
    Usage here is insert the entity moving as the first parameter and the entity being checked against as the second. 
    '''
    def entity_collide(self, entity1, entity2):
        if isinstance(entity2, Boss):
            temp = entity2.getPos()
            for pos in temp:
                if pos == entity1.getPosInFront():
                    return True
            
        elif entity1.getPosInFront() == entity2.getPos():
            return True
        else:
            return False
    
    # Function returns false if it detects a collision, true if it does not
    def check_collisions(self):
        if self.entity_collide(self.player, self.boss):
            return False
        for enemy in self.minions:
            if self.entity_collide(self.player, enemy):
                return False
        for tile in self.game_map2.tiles:
            if self.entity_collide(self.player, tile):
                return False
        return True

    def check_enemy_collisions(self, currentEnemy):
        for enemy in self.minions:
            if enemy == currentEnemy:
                continue
            if self.entity_collide(currentEnemy, enemy):
                return False
        if self.entity_collide(currentEnemy, self.player):
                return False
        for tile in self.game_map2.tiles:
            if self.entity_collide(currentEnemy, tile):
                return False
        return True



    def run_game(self):
        while not self.gameOver:
            self.clock.tick(10)
            self.check_events()
            #print(self.bossAttackMoveTime)
            if self.player.isMoving():
                if self.check_collisions():
                    self.player.movePlayer()
                    #print(self.player.get_grid())
            #time.sleep(0.05)
            self.bossAttack()
            self.move_projectiles()
            self.moveEnemies()
            self.update_screen()
            if self.player.checkGameOver():
                self.gameOver = True
            self.increment_timers()
        self.reset_game()   
            
    def increment_timers(self):
        self.enemyTimer += 1
        self.bossTime += 1
        self.bossAttackMoveTime += 1

    def reset_game(self):
        self.player = Player(self.screen)
        self.boss = Boss(self.screen)
        self.minions = []
        self.gameOver = False
        self.score = 0

    def moveEnemies(self):
        for enemy in self.minions:
                self.static_grid.entities.append(enemy.get_grid())
        if len(self.minions) != 0:
            #path = pathFind(change_grid, self.minions[0].get_grid(), self.player.get_grid())
            #self.temp += 1
            #print(self.temp)
            #move = findNextMove(self.minions[0].get_grid(), self.player.get_grid())
            for enemy in self.minions:
                #move = pathFind(change_grid, enemy.get_grid(), self.player.get_grid())
                if enemy.checkNeighbors(self.player):
                    enemy.getDir(self.player.get_grid())
                    #enemy.attack()
                    #self.update_screen()
                    #self.player.hp -= 1
                    #time.sleep(0.2)
                    #enemy.set_idle_image()
                    
                else:
                    move = findNextMove(enemy.get_grid(), self.player.get_grid(), self.static_grid)
                    if move != None:
                        enemy.getDir(move)
                        #print(move)
                        if self.check_enemy_collisions(enemy):
                            enemy.move(move)
            #self.enemyTimer = 0
        self.static_grid.clearEntities()
    def move_projectiles(self):
        if self.bossAttackMoveTime >= 2:
            for projectile in self.projectiles:
                projectile.move()
                self.bossAttackMoveTime = 0
        for projectile in self.projectiles:
            if projectile.checkHit(self.player):
                self.projectiles.remove(projectile)
            if projectile.checkBoundary():
                self.projectiles.remove(projectile)

    def bossAttack(self):
        if self.bossTime >= 500 and len(self.projectiles) == 0:
            self.projectiles = self.boss.attack()
            self.bossTime = 0

    def initialSpawn(self):
        self.minions.append(Enemy(self.screen, 47, 32))
        self.minions.append(Enemy(self.screen, 36, 32))
        self.minions.append(Enemy(self.screen, 47, 21))
        self.minions.append(Enemy(self.screen, 36, 21))
        self.minions.append(Enemy(self.screen, 2, 32))
        self.minions.append(Enemy(self.screen, 2, 13))
        self.minions.append(Enemy(self.screen, 47, 40))
        self.minions.append(Enemy(self.screen, 26, 42))
        self.minions.append(Enemy(self.screen, 57, 42))
        self.minions.append(Enemy(self.screen, 80, 40))
        self.minions.append(Enemy(self.screen, 80, 13))
        self.minions.append(Enemy(self.screen, 57, 11))
        
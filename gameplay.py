import pygame, sys, time, csv, os


from squareGrid import *
from gamemap import *
from player import *
from boss import *
from enemy import *
from spritesheet import *
import timeit
import random


class Gameplay:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.WHITE = (255,255,255)
        self.screen = pygame.display.set_mode((1360, 768))
        pygame.display.set_caption("Witch Hunt")
        self.spritesheet = Spritesheet('map/finalSheet.png')
        self.game_map1 = Game_Map('map/finalMap_Tile Layer 1.csv', self.spritesheet)
        self.game_map2 = Game_Map('map/finalMap_Tile Layer 2.csv', self.spritesheet)
        self.player = Player(self.screen)
        self.boss = Boss(self.screen)
        self.minions = []
        self.initialSpawn()
        
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
        
        self.enemyTimer = 0
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.get_default_font()
        self.temp = 0
        self.spawnCounter = 0

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
        # time.sleep(0.01)
        self.draw_text(self.player.getHpStr(), 25, 75, 700)
        self.draw_text(self.boss.getHpStr(), 25, 1200, 40)
        self.draw_text(self.getScoreStr(), 25, 1200, 700)
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self.game.LEFT_KEY:
                    self.player.movingLeft = True
                    self.player.dir = "left"
                if event.key == self.game.RIGHT_KEY:
                    self.player.movingRight = True
                    self.player.dir = "right"
                if event.key == self.game.UP_KEY:
                    self.player.movingUp = True
                    self.player.dir = "up"
                if event.key == self.game.DOWN_KEY:
                    self.player.movingDown = True
                    self.player.dir = "down"
                if event.key == self.game.ATTACK_KEY:
                    self.player.attack()
                    if not self.check_collisions():
                        if self.entity_collide(self.player, self.boss):
                            self.gameOver = self.boss.takeHit()
                            if (self.gameOver):
                                self.score += 20000
                                self.draw_text("YOU WIN", 48, 1360 // 2, 768 // 2)
                                pygame.display.flip()
                                time.sleep(2)
                        else:
                            for enemy in self.minions:
                                if self.entity_collide(self.player, enemy):
                                    self.minions.remove(enemy)
                                    self.score += 100
                                    if self.player.hp < 5:
                                        self.player.hp += 1
                                    self.update_screen()
                    self.update_screen()
                    time.sleep(0.15)
                    self.player.set_idle_image()
                '''
                if event.key == pygame.K_e:
                    print(self.player.get_grid())
                if event.key == pygame.K_q:
                    self.minions.append(Enemy(self.screen, 42, 24))
                '''
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
        start = time.time()
        while not self.gameOver:
            self.clock.tick(10)
            
            self.check_events()
            for enemy in self.minions:
                self.static_grid.entities.append(enemy.get_grid())
            if len(self.static_grid.neighbors(self.player.get_grid())) != 0:
                if self.player.isMoving():
                    if self.check_collisions():
                        self.player.movePlayer()
            else:
                pass
            # time.sleep(0.05)
            self.bossAttack()
            self.move_projectiles()
            if self.enemyTimer > 3:
                self.moveEnemies()
            if self.spawnCounter > 35 and len(self.minions) < 11:
                self.respawnMinions()
                
            self.update_screen()
            if self.player.checkGameOver():
                self.gameOver = True
                self.draw_text("GAME OVER", 48, 1360 // 2, 768 // 2)
                pygame.display.flip()
                time.sleep(2)
            self.increment_timers()
        end = time.time()
        self.score += math.floor(100 * (end - start))
        print(self.score)
        self.reset_game()

    def increment_timers(self):
        self.enemyTimer += 1
        self.bossTime += 1
        self.bossAttackMoveTime += 1
        self.spawnCounter += 1

    def reset_game(self):
        self.player = Player(self.screen)
        self.boss = Boss(self.screen)
        self.minions = []
        self.gameOver = False
        self.score = 0

    def moveEnemies(self):
        
        if len(self.minions) != 0:
            for enemy in self.minions:
                if len(self.static_grid.neighbors(enemy.get_grid())) != 0:
                    #move = pathFind(self.static_grid, enemy.get_grid(), self.player.get_grid())
                    move = findNextMove(enemy.get_grid(), self.player.get_grid(), self.static_grid)
                else:
                    move = None
                if enemy.checkNeighbors(self.player):
                    enemy.getDir(self.player.get_grid())
                    enemy.attack()
                    self.update_screen()
                    self.player.hp -= 1
                    time.sleep(0.2)
                    enemy.set_idle_image()
                    

                else:
                    
                    if move != None:
                        enemy.getDir(move)
                        # print(move)
                        if self.check_enemy_collisions(enemy):
                            enemy.move(move)
                    else:
                        pass
            # self.enemyTimer = 0
        self.static_grid.clearEntities()
        self.enemyTimer = 0

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
        if self.bossTime >= 150 and len(self.projectiles) == 0:
            self.projectiles = self.boss.attack()
            self.bossTime = 0

    def initialSpawn(self):
        self.minions.append(Enemy(self.screen, 47, 32))
        self.minions.append(Enemy(self.screen, 36, 32))
        self.minions.append(Enemy(self.screen, 43, 10))
        self.minions.append(Enemy(self.screen, 42, 10))
        self.minions.append(Enemy(self.screen, 7, 23))
        self.minions.append(Enemy(self.screen, 78, 23))
        

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def respawnMinions(self):
        rand = random.randint(1, 6)
        if rand == 1:
            self.minions.append(Enemy(self.screen, 47, 32))
        elif rand == 2:
            self.minions.append(Enemy(self.screen, 36, 32))
        elif rand == 3:
            self.minions.append(Enemy(self.screen, 36, 21)) 
        elif rand == 4:
            self.minions.append(Enemy(self.screen, 47, 21))
        elif rand == 5:
            self.minions.append(Enemy(self.screen, 26, 11))
        elif rand == 6:
            self.minions.append(Enemy(self.screen, 57, 11))
        self.spawnCounter = 0

    def getScoreStr(self):
        return "SCORE: " + str(self.score)
        

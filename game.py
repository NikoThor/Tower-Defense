import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong

class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Club()]
        self.towers = [ArcherTowerLong(300,300)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))


    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
           # pygame.time.delay(250)
            clock.tick(430)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            to_del  = []
            #   loop through enemies
            for en in self.enemys:
                if en.x < -15:
                    to_del.append(en)
            for d in to_del:
                self.enemys.remove(d)

            self.draw()
        pygame.quit()


    def draw(self):
        self.win.blit(self.bg, (0,0))
        #draw enemies
        for en in self.enemys:
            en.draw(self.win)
        for tw in self.towers:
            tw.draw(self.win)
        pygame.display.update()

g = Game()
g.run()
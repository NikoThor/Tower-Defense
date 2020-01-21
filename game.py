import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowershort
import time
import random


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Club()]
        self.towers = [ArcherTowerLong(300,200), ArcherTowerLong(700,600), ArcherTowershort(200,600)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()


    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            if time.time() - self.timer >= random.randrange(1,5)/2:
                self.timer = time.time()
                self.enemys.append(random.choice([Club(), Scorpion(), Wizard()]))
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
            # delete all enemies off the screen
            for d in to_del:
                self.enemys.remove(d)
            # loop through towers
            for tw in self.towers:
                tw.attack(self.enemys)

            self.draw()
        pygame.quit()


    def draw(self):
        self.win.blit(self.bg, (0,0))
        # draw towers
        for tw in self.towers:
            tw.draw(self.win)
        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        pygame.display.update()

g = Game()
g.run()
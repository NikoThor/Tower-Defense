import pygame
from .tower import Tower
import os
import math

class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 200
        self.inRange = False

        # load archer tower images
        for x in range(7,10):
            self.tower_imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
                (64, 64)))
        # load archer images

        for x in range(38,43):
            self.archer_imgs.append(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")),
            )

    def draw(self, win):
        super().draw(win)

        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0
        archer = self.archer_imgs[self.archer_count // 10]
        win.blit(archer, ((self.x + self.width / 2 - 20), (self.y - archer.get_height() - 15)))

    def change_range(self, r):
        self.range = r

    def attack(self, enemies):

        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis =math.sqrt((self.x-x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

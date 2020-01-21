import pygame
from .tower import Tower
import os
import math
import time
tower_imgs1 = []
archer_imgs1 = []

# load archer tower images
for x in range(7, 10):
    tower_imgs1.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
        (64, 64)))
# load archer images

for x in range(38, 44):
    archer_imgs1.append(pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")), )

class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1[:]
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 200
        self.inRange = False
        self.left = True
        self.damage = 1

    def draw(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))

        super().draw(win)
        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 10:
                self.archer_count = 0
        else:
            self.archer_count = 0
        archer = self.archer_imgs[self.archer_count // 10]
        if self.left == True:
            add = -25
        else:
            add = -archer.get_width() + 10
        win.blit(archer, ((self.x + self.width / 2 + add), (self.y - archer.get_height() - 15)))

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

        enemy_closest.sort(key=lambda  x: x.x)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if self.archer_count == 6:
                if first_enemy.hit(self.damage) == True:
                    enemies.remove(first_enemy)


            if first_enemy.x > self.x and not (self.left):
                self.left =  True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
tower_imgs = []
archer_imgs = []
 # load archer tower images
for x in range(10, 13):
    tower_imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/archer_towers/archer_2", str(x) + ".png")),
        (64, 64)))
# load archer images

for x in range(51, 57):
    archer_imgs.append(
        pygame.image.load(os.path.join("game_assets/archer_towers/archer_top_2", str(x) + ".png")), )

class ArcherTowershort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs[:]
        self.archer_imgs = archer_imgs[:]
        self.archer_count = 0
        self.range = 100
        self.inRange = False
        self.left = True
        self.damage = 2


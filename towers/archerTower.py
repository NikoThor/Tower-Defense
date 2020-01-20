import pygame
from .tower import Tower
import os

class ArcherTowerLong(Tower):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        # load archer tower images
        for x in range(10):
            self.tower_imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_1", str(x) + ".png")),
                (64, 64)))
        # load archer images
        for x in range(37,43):
            self.tower_imgs.append(pygame.transform.scale(
                pygame.image.load(os.path.join("game_assets/archer_towers/archer_top", str(x) + ".png")),
                (64, 64)))

    def draw(self, win):
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs)*3:
            self.archer_count = 0
        archer = self.archer_imgs[self.archer_count//3]
        win.blit(archer, ((self.x + self.width/2) - (archer.get_width()/2),(self.y - archer.get_height())))
    def attack(self, enemies):
        pass
        
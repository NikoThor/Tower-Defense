import pygame
import os
pygame.font.init()

star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")), (50,50))

class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()


    def click(self, X , Y):
        if X <= self.x + self.width and X > self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))




class Menu:
    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width
        self.height = img.get_height
        self.item_cost = item_cost
        self.items = 0
        self.buttons = []
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_btn(self, img, name):
        self.items += 1
        btn_x = self.x - self.bg.get_width()/2 + 10
        btn_y = self.y - 120 + 10
        self.buttons.append(Button(btn_x,btn_y, img, name))

    def draw(self, win):
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width + 5, item.y - 9))
            text = self.font.render(str(self.item_cost[self.tower.level -  1]), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star.get_height()-8))

    def get_clicked(self, X, Y):
        """
        return the cliced item from the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        for btn in self.buttons:
            if btn.click(X, Y):
                return btn.name
        return None
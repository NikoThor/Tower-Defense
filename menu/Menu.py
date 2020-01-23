import pygame
import os
pygame.font.int()

star = pygame.image.load(os.path.join("game_assets", "star"))

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
    def __init__(self,x,y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width
        self.height = img.get_height
        self.item_cost = item_cost
        self.items = 0
        self.buttons = []
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 30)

    def add_btn(self, img, name):
        self.items += 1
        btn_x = self.x - self.bg.get_width()/2 + 10
        btn_y = self.y - 120 + 10
        self.buttons.append(Button(btn_x,btn_y, img, name))

    def draw(self, win):
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
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
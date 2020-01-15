import pygame

class Enemy:
    imgs = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

    def draw(self, win):


        self.animation_count +=1
        self.img = self.imgs[self.animation_count]
        if self.animation_count > len(self.imgs):
            self.animation_count = 0
        win.blit(self.img, (self.x, self.y))
        self.move()



    def collide(self, x, y):

        if x <= self.x + self.width and x >=self.x:
            if y <= self.y + self.height and y  >= self.y:
                return True

        return  False

    def move(self):
        pass

    def hit(self):
        self.health -=1
        if self.health <= 0:
            return True
import pygame
import math
class Enemy:
    imgs = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(19, 224), (177, 235), (282, 283), (526, 277), (607, 217), (641, 105), (717, 57), (796, 83), (855, 222), (973, 284), (1046, 366), (1022, 458), (894, 492), (740, 504), (580, 542), (148, 541), (10, 442), (-20, 335),]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0

    def draw(self, win):



        self.img = self.imgs[self.animation_count]
        self.animation_count += 1
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

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2,y2 = (-10, 347)

        else:
            x2,y2 = self.path[self.path_pos+1]

        move_dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        self.move_count += 1
        dirn = (x2-x1, y2-y1)



        move_x, move_y = (self.x + dirn[0] * self.move_count, self.y + dirn[1] * self.move_count)
        self.move_dis += math.sqrt((move_x - x1) ** 2 + (move_y - y1) ** 2)

        if self.move_dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                return False
        self.x = move_x
        self.y = move_y
        return True
    def hit(self):
        self.health -=1
        if self.health <= 0:
            return True
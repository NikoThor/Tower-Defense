import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowershort
from towers.supportTower import RangeTower, DamageTower
import time
import random


pygame.font.init()
lives_img = pygame.image.load(os.path.join("game_assets","heart.png"))
star_img = pygame.image.load(os.path.join("game_assets","star.png"))

class Game:
    def __init__(self):
        self.width = 1250
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = [Club()]
        self.attack_towers = [ArcherTowerLong(300, 200), ArcherTowerLong(700, 600), ArcherTowershort(200, 600)]
        self.support_towers = [DamageTower(400,200)]
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font =  pygame.font.SysFont("comicsans", 70)
        self.selected_tower = None



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
                    # Look to see if you clicked on a attack tower
                    bnt_clicked = None
                    if self.selected_tower:
                        bnt_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                        if bnt_clicked:
                            if bnt_clicked == "Upgrade":
                                self.selected_tower.upgrade()
                    if not (bnt_clicked):
                        for tw in self.attack_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

                            # look if you clicked on support tower
                        for tw in self.support_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False




            to_del  = []
            #   loop through enemies
            for en in self.enemys:
                if en.x < -15:
                    to_del.append(en)
            # delete all enemies off the screen
            for d in to_del:
                self.lives -= 1
                self.enemys.remove(d)
            # loop through  attack towers
            for tw in self.attack_towers:
                tw.attack(self.enemys)

             # loop through support towers
            for tw in self.support_towers:
                tw.support(self.attack_towers)

            # if you lose
            if self.lives <= 0:
                print("You Lose")
                run = False

            self.draw()
        pygame.quit()


    def draw(self):
        self.win.blit(self.bg, (0,0))
        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)
        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)
        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (0,0,0))
        life = pygame.transform.scale(lives_img, (50,50))
        start_x = self.width - life.get_width() - 10


        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))


        pygame.display.update()
    def draw_menu(self):
        pass
g = Game()
g.run()
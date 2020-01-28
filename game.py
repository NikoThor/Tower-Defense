import pygame
import os
from enemies.scorpion import Scorpion
from enemies.club import Club
from enemies.wizard import Wizard
from towers.archerTower import ArcherTowerLong, ArcherTowershort
from menu.Menu import VerticalMenu
from towers.supportTower import RangeTower, DamageTower
import time
import random

pygame.font.init()
lives_img = pygame.image.load(os.path.join("game_assets", "heart.png"))
star_img = pygame.image.load(os.path.join("game_assets", "star.png"))
side_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "side.png")), (120, 500))

buy_archer = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "buy_archer.png")), (75, 75))
buy_crossbow = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "buy_crossbow.png")), (75, 75))
buy_damage = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "buy_damage.png")), (75, 75))
buy_range = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "buy_range.png")), (75, 75))

attack_tower_names = ["archer", "crossbow"]
support_tower_names = ["range", "damage"]


class Game:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.attack_towers = [ArcherTowerLong(300, 200), ArcherTowerLong(700, 600), ArcherTowershort(200, 600)]
        self.support_towers = [DamageTower(400, 200)]
        self.lives = 10
        self.money = 2500
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.timer = time.time()
        self.life_font = pygame.font.SysFont("comicsans", 70)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 250, side_img)
        self.menu.add_btn(buy_archer, "buy_archer", 500)
        self.menu.add_btn(buy_crossbow, "buy_crossbow", 750)
        self.menu.add_btn(buy_damage, "buy_damage", 1000)
        self.menu.add_btn(buy_range, "buy_range", 1000)
        self.moving_object = None

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(430)
            # gen monsters
            if time.time() - self.timer >= random.randrange(1, 5) / 2:
                self.timer = time.time()
                self.enemys.append(random.choice([Club(), Scorpion(), Wizard()]))

            pos = pygame.mouse.get_pos()
            # check for moving objects
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if you're moving an object and click
                    if self.moving_object:
                        if self.moving_object.name in attack_tower_names:
                            self.attack_towers.append(self.moving_object)
                        elif self.moving_object.name in support_tower_names:
                            self.support_towers.append(self.moving_object)
                        self.moving_object.moving = False
                        self.moving_object = None


                    else:
                        # look if you clicked on side menu
                        side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if side_menu_button:
                            cost = self.menu.get_item_cost(side_menu_button)
                            if self.money >= cost:
                                self.money -= cost
                                self.add_tower(side_menu_button)

                        # Look to see if you clicked on a attack tower or support tower
                        bnt_clicked = None
                        if self.selected_tower:
                            bnt_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if bnt_clicked:
                                if bnt_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
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

            to_del = []
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
                self.money += tw.attack(self.enemys)

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
        self.win.blit(self.bg, (0, 0))
        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)
        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)
        # draw enemies
        for en in self.enemys:
            en.draw(self.win)
        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)
        # Draw menu
        self.menu.draw(self.win)

        # draw lives
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        life = pygame.transform.scale(lives_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 13))
        self.win.blit(life, (start_x, 10))

        # draw money
        text = self.life_font.render(str(self.money), 1, (255, 255, 255))
        money = pygame.transform.scale(star_img, (50, 50))
        start_x = self.width - life.get_width() - 10

        self.win.blit(text, (start_x - text.get_width() - 10, 75))
        self.win.blit(money, (start_x, 65))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_archer", "buy_crossbow", "buy_damage", "buy_range"]
        object_list = [ArcherTowerLong(x, y), ArcherTowershort(x, y), DamageTower(x, y), RangeTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True

        except Exception as e:
            print(str(e) + "NOT VALID NAME")


g = Game()
g.run()

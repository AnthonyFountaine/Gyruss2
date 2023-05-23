import pygame, math
from pygame.math import Vector2 as v2

from assets.code.settings import *
from assets.code.entity import Entity
from assets.code.bullet import Bullet

class Player(Entity):
    def __init__(self, groups, start_angle, allsprites):
        super().__init__(groups)
        self.all_sprites = allsprites

        self.origimage = pygame.image.load('assets/sprites/player/PLAYER.png').convert_alpha()
        self.origimage = pygame.transform.scale(self.origimage, (self.origimage.get_width() * 2.5, self.origimage.get_height() * 2.5))
        self.origimage.set_colorkey((0,0,0))
        self.image = self.origimage.copy()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))

        self.pos = v2(self.rect.center)
        self.downpos = self.pos.copy()
        self.shootdelay = 15

        self.angle = start_angle

        self.name = 'Player'


    def input(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.downpos.y <= WINDOW_HEIGHT//2:
                self.angle += 70 * dt
            else:
                self.angle -= 70 * dt
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.downpos.y <= WINDOW_HEIGHT//2:
                self.angle -= 70 * dt
            else:
                self.angle += 70 * dt

    def move(self):
        self.pos.x = WINDOW_WIDTH//2+370*math.cos(math.radians(self.angle))
        self.rect.x = round(self.pos.x)

        self.pos.y = WINDOW_HEIGHT//2+370*math.sin(math.radians(self.angle))
        self.rect.y = round(self.pos.y)

    def rotate(self):
        self.image = pygame.transform.rotate(self.origimage, -(self.angle - 90))

    def shoot(self):
        Bullet(self.all_sprites, self)

    def update(self, dt, update):
        if update:
            self.downpos = self.pos.copy()
        self.shootdelay +=1
        self.input(dt)
        self.move()
        self.rotate()



        
    


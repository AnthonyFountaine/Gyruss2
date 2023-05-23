import pygame, math
from pygame.math import Vector2 as v2

from assets.code.settings import *
from assets.code.entity import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, player):
        print('new bullet')
        super().__init__(groups)

        self.name = "Bullet"
        self.player = player

        self.image = pygame.image.load('assets/sprites/bullet/bullet.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect(center = (player.rect.x, player.rect.y))

        self.pos = v2(self.rect.center)
        self.speed = 400
        self.direction = v2(((WINDOW_WIDTH//2 - self.rect.x), (WINDOW_HEIGHT//2 - self.rect.y))).normalize()
        self.angle = self.player.angle
        self.update200 = False
        self.update100 = False
        self.rotate()

    def move(self, dt):
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)

    def updatesize(self):
        distance = math.sqrt((WINDOW_WIDTH//2 - self.rect.x)**2 + (WINDOW_HEIGHT//2 - self.rect.y)**2)
        if distance < 250 and not self.update200:
            self.image = pygame.image.load('assets/sprites/bullet/bullet2.png')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.update200 = True
            self.rect = self.image.get_rect(center = (self.rect.x, self.rect.y))
            self.rotate()
        if distance < 80 and not self.update100:
            self.image = pygame.image.load('assets/sprites/bullet/bullet3.png')
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
            self.update100 = True
            self.rect = self.image.get_rect(center = (self.rect.x, self.rect.y))
            self.rotate() 

    def rotate(self):
        self.image = pygame.transform.rotate(self.image, -(self.angle - 90))
        
    def checkmid(self):
        if WINDOW_HEIGHT//2-7<=self.rect.y<=WINDOW_HEIGHT//2+7 and WINDOW_WIDTH//2-7<=self.rect.x<=WINDOW_WIDTH//2+7:
            self.kill()

    def update(self, dt, update):
        self.updatesize()
        self.move(dt)
        self.checkmid()
        
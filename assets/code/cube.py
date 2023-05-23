import pygame, random, math
from pygame.math import Vector2 as v2
from assets.code.settings import *
cubecolors = ['yellow', 'orange', 'pink', 'hot pink', 'purple', 'green', 'blue', 'navy blue']

class Cube(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.name = "Cube"

        self.image = pygame.Surface((4,4))
        self.origwidth = self.image.get_width()
        self.origheight = self.image.get_height()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
        
        self.image.fill(random.choice(cubecolors))

        self.direction = v2()
        if bool(random.choice([True, False])):
            self.direction.x = random.random()
        else:
            self.direction.x = -random.random()
        
        if bool(random.choice([True, False])):
            self.direction.y = random.random()
        else:
            self.direction.y = -random.random()

        self.pos = v2(self.rect.center)

        if self.direction.magnitude() < 0.8:
            self.speed = random.randint(800 * 2, 810 * 2)
        else:
            self.speed = random.randint(800, 810)

    def move(self, dt):
        self.pos.x += self.direction.x * int(self.speed) * dt
        self.rect.x = self.pos.x

        self.pos.y += self.direction.y * int(self.speed) * dt
        self.rect.y = self.pos.y

        self.speed += 7 * dt


    def resize(self):
        distance = math.sqrt((WINDOW_WIDTH//2 - self.rect.centerx)**2 + (WINDOW_HEIGHT//2 - self.rect.centery)**2)

        scalefactor = distance // 80

        self.image = pygame.transform.scale(self.image, (int(self.origwidth + scalefactor), int(self.origheight + scalefactor)))

    def offScreen(self):
        if self.rect.left > WINDOW_WIDTH or self.rect.right < 0:
            self.kill()
        if self.rect.top > WINDOW_HEIGHT or self.rect.bottom < 0:
            self.kill()
        
        
    def update(self, dt, update):
        self.move(dt)
        self.resize()
        self.offScreen()
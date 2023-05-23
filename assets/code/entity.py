import pygame
from os import walk

from assets.code.settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

    def importAssets(self, path):
        self.animations = {}

        for index, folder_name in enumerate(walk(path)):
            if index == 0:
                for folder in folder_name[1]:
                    self.animations[folder] = []
            
            else:
                for index, file_name in enumerate(folder_name[2]):
                    newpath = folder_name[0].replace('\\', '/')
                    slash = newpath.rfind('/')
                    folder = newpath[slash+1:]
                    image = pygame.image.load(newpath + '/' + file_name)
                    self.animations[folder].append(image)
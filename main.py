#main.py
import pygame, sys, random
from pygame import Vector2 as v2
from assets.code.settings import *
from assets.code.cube import Cube
from assets.code.player import Player

class AllSprites(pygame.sprite.Group):
	def __init__(self):
		#initating the sprite.Group properties
		super().__init__()

		self.display = pygame.display.get_surface()

	def my_draw(self):
		for sprite in self.sprites():
			if sprite.name == 'Player':
				self.display.blit(sprite.image, (sprite.rect.x - int(sprite.image.get_width()//2), sprite.rect.y - int(sprite.image.get_height()/2)))
			else:
				self.display.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
class PygameGame():
	def __init__(self):
		#setting the display up
		self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED)
		pygame.display.set_caption('Gyruss 2')
		
		#defining the sprite groups
		self.all_sprites = AllSprites()
	
	def main(self):
		cubeframe = 0
		FPS = pygame.time.Clock()
		self.player = Player(self.all_sprites, -90, self.all_sprites)
		while True:
			update = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
						update = True
					if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL or event.key == pygame.K_SPACE:
						Player.shoot(self.player)

			self.display.fill('black')

			dt = FPS.tick(60) / 1000

			cubeframe += 1
			if cubeframe >= random.randint(35,40):
				for i in range(8):
					Cube(self.all_sprites)
				cubeframe = 0
			elif cubeframe%7 == 0:
				Cube(self.all_sprites)

			self.all_sprites.update(dt, update)

			self.all_sprites.my_draw()

			pygame.display.update()



game = PygameGame()
game.main()


		
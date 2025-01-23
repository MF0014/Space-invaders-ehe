import pygame

class Enemies(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		fileDir = 'Properties/enemy.png'
		self.image =pygame.image.load(fileDir).convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self,direction):
		self.rect.x += direction
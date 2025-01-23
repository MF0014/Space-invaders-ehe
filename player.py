import pygame
from laser import Laser

pygame.init()

playerLaserSound = pygame.mixer.Sound('Properties/effects/user_laser.mp3')

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		# Scale the image to the new dimensions

		self.image = pygame.image.load('Properties/player.png').convert_alpha()
		self.player = pygame.transform.scale(self.image, (500, 500))
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = 5
		self.max_x_constraint = constraint
		self.ready = True
		self.laserTime = 0
		self.laserCD = 500

		self.lasers = pygame.sprite.Group()

	def userInput(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.userLaser()
			playerLaserSound.play()
			self.ready = False
			self.laserTime = pygame.time.get_ticks()

	def recharge(self):
		if not self.ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.laserTime >= self.laserCD:
				self.ready = True


	def userLaser(self):
		self.lasers.add(Laser(self.rect.center, -8,self.rect.bottom))


	def constraint(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= self.max_x_constraint:
			self.rect.right = self.max_x_constraint


	def update(self):
		self.userInput()
		self.constraint()
		self.recharge()
		self.lasers.update()
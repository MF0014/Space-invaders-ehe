import pygame, sys
from player import Player
from enemies import Enemies
from random import choice
from laser import Laser

pygame.init()




enemyLaserSound = pygame.mixer.Sound('Properties/effects/enemy_laser.mp3')
enemyDeadSound = pygame.mixer.Sound('Properties/effects/enemy_dead.mp3')
playerDeadSound = pygame.mixer.Sound('Properties/effects/user_dead.mp3')
victorySound = pygame.mixer.Sound('Properties/effects/victory_music.mp3')
gameoverSound = pygame.mixer.Sound('Properties/effects/gameover_music.mp3')

bounceSound = pygame.mixer.Sound('Properties/effects/bounce_effect.mp3')

background = pygame.image.load('Properties/background.png')

text_font = pygame.font.Font(None, 100)

pygame.display.set_caption("Space Shooting Game")

class Game:

    def __init__(self):
        playerProperty = Player((screen_width / 2, screen_height),screen_width,5) 
        #playerProperty = Player((screen_width / 2)) 
        self.player = pygame.sprite.GroupSingle(playerProperty)

        #enemies dir
        self.enemy = pygame.sprite.Group()
        self.enemyInit(rows = 4, cols = 5)
        self.enemyDirection = 1
        self.enemyLaser = pygame.sprite.Group()

        #Player value setup
        self.lives = 3
        self.live_surf = pygame.image.load('Properties/life.png').convert_alpha()
        self.liveStartPos = screen_width - (self.live_surf.get_size()[0] * 10.3 + 20)
        self.score = 20
        self.font = pygame.font.Font(None, 30)

        self.game_over = False
        self.winUser = False


    

    #enemies properties

    def enemyInit(self,rows,cols, x_distance = 90, y_distance = 60, x_offset = 90, y_offset = 50):
    	for row_index, row in enumerate(range(rows)):
    		for col_index, con in enumerate(range(cols)):
    			x = col_index * x_distance + x_offset
    			y = row_index * y_distance + y_offset
    			enemyProperties = Enemies(x,y)
    			self.enemy.add(enemyProperties)

    def enemyPositionChanger(self):
        # Check if aliens have reached the screen edges and adjust their position accordingly
        all_enemies = self.enemy.sprites()  # Get all alien sprites
        for enemy in all_enemies:
            if enemy.rect.right >= screen_width:
                self.enemyDirection = -1  # Set the alien direction to move left
                bounceSound.play()  # Play a sound indicating that aliens are moving down
            elif enemy.rect.left <= 0:
                self.enemyDirection = 1 # Set the alien direction to move right
                bounceSound.play()  
                #alien_down_sound.play()  # Play a sound indicating that aliens are moving down

    def enemyShoot(self):
    	if self.enemy.sprites():
    		random_enemy = choice(self.enemy.sprites())
    		enemy_laser = Laser(random_enemy.rect.center,8,screen_height)
    		self.enemyLaser.add(enemy_laser)
    		enemyLaserSound.play()

    def collisionChecker(self):
    	if self.player.sprite.lasers:
    		for laser in self.player.sprite.lasers:
    			if pygame.sprite.spritecollide(laser,self.enemy,True):
    				laser.kill()
    				enemyDeadSound.play()
    				self.score -= 1
    				if not self.enemy.sprites():
    					self.winUser = True


    	if self.enemyLaser:
    		for laser in self.enemyLaser:
    			if pygame.sprite.spritecollide(laser,self.player,False):
    				laser.kill()
    				playerDeadSound.play()
    				self.lives -=1
    				if self.lives == 0:
    					self.game_over = True

    					
    					

    def lifeDisplay(self): 
    	for live in range(self.lives):
    		x = self.liveStartPos + (live * self.live_surf.get_size()[0] + 10)
    		screen.blit(self.live_surf,(x,8))

    def scoreDisplay(self):
    	displayScore = self.font.render(f"Enemies: {self.score}", True, 'black')
    	scoreRect = displayScore.get_rect(topright = (600,10))
    	screen.blit(displayScore, scoreRect)

    def gameoverDisplay(self):
	    restart_game = False  # Flag to control game restart

	    while True:
	        gameoverSound.play()
	        game_over_text = text_font.render("Game Over", True, 'red')
	        game_over_position = game_over_text.get_rect(center=(screen_width // 2, 250))
	        screen.blit(game_over_text, game_over_position)
	        pygame.display.flip()

	        button_width = 200
	        button_height = 50
	        button_color = 'black'
	        button_text_color = 'green'
	        button_font = pygame.font.Font(None, 36)
	        button_text = button_font.render("Restart", True, button_text_color)
	        button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height)
	        pygame.draw.rect(screen, button_color, button_rect)
	        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                pygame.quit()
	                sys.exit()
	            if event.type == pygame.MOUSEBUTTONDOWN:
	                mouse_pos = pygame.mouse.get_pos()
	                if button_rect.collidepoint(mouse_pos):
	                    # Set the restart_game flag to True to restart the game
	                    restart_game = True

	        if restart_game:
	            break  # Exit the loop to restart the game

	    # Restart the game
	    self.__init__()  # Reinitialize the game object
	    self.run()

    def winDisplay(self):
	    restart_game = False  # Flag to control game restart

	    while True:
	        victorySound.play()
	        game_over_text = text_font.render("You win!", True, 'green')
	        game_over_position = game_over_text.get_rect(center=(screen_width // 2, 250))
	        screen.blit(game_over_text, game_over_position)
	        pygame.display.flip()

	        button_width = 200
	        button_height = 50
	        button_color = 'black'
	        button_text_color = 'green'
	        button_font = pygame.font.Font(None, 36)
	        button_text = button_font.render("Restart", True, button_text_color)
	        button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height)
	        pygame.draw.rect(screen, button_color, button_rect)
	        screen.blit(button_text, button_text.get_rect(center=button_rect.center))

	        for event in pygame.event.get():
	            if event.type == pygame.QUIT:
	                pygame.quit()
	                sys.exit()
	            if event.type == pygame.MOUSEBUTTONDOWN:
	                mouse_pos = pygame.mouse.get_pos()
	                if button_rect.collidepoint(mouse_pos):
	                    # Set the restart_game flag to True to restart the game
	                    restart_game = True

	        if restart_game:
	            break  # Exit the loop to restart the game

	    # Restart the game
	    self.__init__()  # Reinitialize the game object
	    self.run()

    def startDisplay(self):
    	title_font = pygame.font.Font(20)
    	instruction_font = pygame.font.Font(None, 36)
    	menu_img = pygame.image.load("Properties/background.png").convert() # image used to be bg for start menu 
    	while True:
            screen.blit(menu_img, (0, 0)) # screen blit to show the menu img 

            title_text = title_font.render("SPACE SHOOTER", True, (255, 165, 0))  # this is the TITLE "SPACE SHOOTER"
            title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 3))
            screen.blit(title_text, title_rect)

            instruction_text = instruction_font.render("Press ENTER to start the game", True, (255, 255, 255)) # and the INSTRUCTION for the player
            instruction_rect = instruction_text.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(instruction_text, instruction_rect)

            pygame.display.flip() # to update the display or screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return



    def run(self):



        self.player.sprite.lasers.draw(screen)
        self.player.update()
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.enemy.update(self.enemyDirection)
        self.enemyPositionChanger()

        self.enemyLaser.update()
        self.enemyLaser.draw(screen)

        self.collisionChecker()
        self.lifeDisplay()

        #self.scoreDisplay()
        if self.game_over:
        	self.gameoverDisplay()
        if self.winUser:
        	self.winDisplay()
        

        # Update sprite groups here 



	    	



    




if __name__ == '__main__':


	pygame.init()
	screen_width = 650
	screen_height = 700
	screen = pygame.display.set_mode((screen_width, screen_height))
	clock = pygame.time.Clock()
	game = Game()


	enemyTimer = pygame.USEREVENT + 1
	pygame.time.set_timer(enemyTimer, 500)



	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == enemyTimer:
				game.enemyShoot()
			
				

		

		screen.fill((249, 246, 238))
		screen.blit(background, (0,0))
		#background = pygame.transform.scale(background, (screen_width, screen_height))
		game.run()

		pygame.display.flip()
		clock.tick(60)



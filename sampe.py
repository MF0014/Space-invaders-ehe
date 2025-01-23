import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Example")

# Set up the button
button_width = 200
button_height = 50
button_color = (0, 150, 0)
button_text_color = (255, 255, 255)
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Click Me", True, button_text_color)
button_rect = pygame.Rect(screen_width // 2 - button_width // 2, screen_height // 2 - button_height // 2, button_width, button_height)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                print("Button clicked!")

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the button
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text.get_rect(center=button_rect.center))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 10
player_speed = 5

# Bullet
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Aliens
alien_width = 40
alien_height = 40
alien_speed = 2
alien_direction = 1
aliens = []
rows = 5
cols = 10

def spawn_aliens():
    global aliens
    aliens = []
    for row in range(rows):
        for col in range(cols):
            alien_x = col * (alien_width + 10) + 50
            alien_y = row * (alien_height + 10) + 50
            aliens.append([alien_x, alien_y])

# Initial spawn
spawn_aliens()

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot bullet
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])
    
    # Player movement 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:  # A for left
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < SCREEN_WIDTH - player_width:  # D for right
        player_x += player_speed
    
    # Update bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullets.remove(bullet)
    
    # Update aliens
    move_down = False
    for alien in aliens:
        alien[0] += alien_speed * alien_direction
        if alien[0] <= 0 or alien[0] >= SCREEN_WIDTH - alien_width:
            move_down = True
    if move_down:
        alien_direction *= -1
        for alien in aliens:
            alien[1] += alien_height
    
    # Collision detection
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if (bullet[0] < alien[0] + alien_width and
                bullet[0] + bullet_width > alien[0] and
                bullet[1] < alien[1] + alien_height and
                bullet[1] + bullet_height > alien[1]):
                bullets.remove(bullet)
                aliens.remove(alien)
                score += 10
                break
    
    # Check for new wave
    if not aliens:
        spawn_aliens()
    
    # Check game over
    for alien in aliens:
        if alien[1] >= SCREEN_HEIGHT - alien_height:
            running = False
    
    # Draw player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    
    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))
    
    # Draw aliens
    for alien in aliens:
        pygame.draw.rect(screen, RED, (alien[0], alien[1], alien_width, alien_height))
    
    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

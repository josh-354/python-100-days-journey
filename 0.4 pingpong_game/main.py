import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 7

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Font for scoreboard
font = pygame.font.SysFont(None, 55)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

class Scoreboard:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0

    def draw(self, screen):
        left_text = font.render(str(self.left_score), True, WHITE)
        right_text = font.render(str(self.right_score), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (3 * WIDTH // 4, 20))

# Create game objects
left_paddle = Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
right_paddle = Paddle(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()
scoreboard = Scoreboard()

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move_up()
    if keys[pygame.K_s]:
        left_paddle.move_down()
    if keys[pygame.K_UP]:
        right_paddle.move_up()
    if keys[pygame.K_DOWN]:
        right_paddle.move_down()

    # Move ball
    ball.move()

    # Ball collision with top and bottom
    if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
        ball.bounce_y()

    # Ball collision with paddles
    if ball.rect.colliderect(left_paddle.rect) and ball.speed_x < 0:
        ball.bounce_x()
    if ball.rect.colliderect(right_paddle.rect) and ball.speed_x > 0:
        ball.bounce_x()

    # Scoring
    if ball.rect.left <= 0:
        scoreboard.right_score += 1
        ball.reset()
    if ball.rect.right >= WIDTH:
        scoreboard.left_score += 1
        ball.reset()

    # Draw everything
    left_paddle.draw(screen)
    right_paddle.draw(screen)
    ball.draw(screen)
    scoreboard.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS for smooth gameplay

pygame.quit()

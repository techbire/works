import pygame
import sys
import random




# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position and speed
snake = [(5, 5)]
snake_speed_x = 1
snake_speed_y = 0

# Food initial position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = -1
            elif event.key == pygame.K_DOWN and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = 1
            elif event.key == pygame.K_LEFT and snake_speed_x == 0:
                snake_speed_x = -1
                snake_speed_y = 0
            elif event.key == pygame.K_RIGHT and snake_speed_x == 0:
                snake_speed_x = 1
                snake_speed_y = 0

    # Move the snake
    new_head = (snake[0][0] + snake_speed_x, snake[0][1] + snake_speed_y)
    snake.insert(0, new_head)

    # Check for collisions
    if snake[0] == food:
        score += 1
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

    # Check if the snake hits the wall
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        running = False

    # Check if the snake hits itself
    if snake[0] in snake[1:]:
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the food
    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    # Update the display
    pygame.display.flip()

    # Control game speed
    pygame.time.delay(1000 // SNAKE_SPEED)

# Game over screen
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)
game_over_text = font.render("Game Over", True, BLACK)
game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(game_over_text, game_over_rect)
pygame.display.flip()

# Wait for a moment before closing
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()
sys.exit()

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Paddle dimensions
paddle_width, paddle_height = 10, 100

# Ball dimensions
ball_size = 20

# Paddle positions
left_paddle_y = height // 2 - paddle_height // 2
right_paddle_y = height // 2 - paddle_height // 2

# Ball position and velocity
ball_x, ball_y = width // 2, height // 2
ball_speed_x, ball_speed_y = 7, 7

# Paddle speeds
paddle_speed = 7

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get keys
    keys = pygame.key.get_pressed()
    
    # Left paddle movement
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < height - paddle_height:
        left_paddle_y += paddle_speed
    
    # Right paddle movement
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
        right_paddle_y += paddle_speed
    
    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    # Ball collision with top and bottom
    if ball_y <= 0 or ball_y >= height - ball_size:
        ball_speed_y = -ball_speed_y
    
    # Ball collision with paddles
    if (ball_x <= paddle_width and left_paddle_y <= ball_y <= left_paddle_y + paddle_height) or \
       (ball_x >= width - paddle_width - ball_size and right_paddle_y <= ball_y <= right_paddle_y + paddle_height):
        ball_speed_x = -ball_speed_x
    
    # Ball out of bounds
    if ball_x < 0 or ball_x > width:
        ball_x, ball_y = width // 2, height // 2
        ball_speed_x, ball_speed_y = -ball_speed_x, ball_speed_y
    
    # Clear screen
    screen.fill(black)
    
    # Draw paddles
    pygame.draw.rect(screen, white, (0, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (width - paddle_width, right_paddle_y, paddle_width, paddle_height))
    
    # Draw ball
    pygame.draw.rect(screen, white, (ball_x, ball_y, ball_size, ball_size))
    
    # Update screen
    pygame.display.flip()
    
    # Frame rate
    pygame.time.Clock().tick(60)

import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 300
BALL_SPEED = 5
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle and ball
paddle_width, paddle_height = 10, 60
ball_width, ball_height = 10, 10

# Initial positions
paddle1_x, paddle1_y = 30, HEIGHT // 2 - paddle_height // 2
paddle2_x, paddle2_y = WIDTH - 30 - paddle_width, HEIGHT // 2 - paddle_height // 2
ball_x, ball_y = WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2
ball_dx = random.choice((BALL_SPEED, -BALL_SPEED))
ball_dy = random.choice((BALL_SPEED, -BALL_SPEED))

# Create Q-table
q_table = np.zeros((WIDTH, HEIGHT, 3))  # State space: (ball_x, ball_y, paddle1_y)

# Q-learning parameters
learning_rate = 0.1
discount_factor = 0.9
epsilon = 0.1

# Q-learning update function
def q_learning_update(state, action, reward, next_state):
    predict = q_table[state[0], state[1], action]
    target = reward + discount_factor * np.max(q_table[next_state[0], next_state[1]])
    q_table[state[0], state[1], action] += learning_rate * (target - predict)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Initialize rewards for Paddle 1 and Paddle 2 at the start of each game iteration
    reward1 = 0
    reward2 = 0

    # Rest of the game loop...
    # (The code for moving paddles, updating ball position, collision detection, and Q-learning updates remains the same as in the previous code.)

# Quit Pygame
pygame.quit()

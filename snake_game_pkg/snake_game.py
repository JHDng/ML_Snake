import math
import random
import sys
from collections import namedtuple
from enum import Enum

import numpy as np
import pygame

# CONSTANTS
BLOCK_SIZE = 25
SPEED = 7

# Setup
Point = namedtuple('Point',  'x, y')
background = pygame.image.load('Background.png')
apple = pygame.image.load('Apple.png')
apple_center = apple.get_rect().center
snake_head = pygame.image.load('Head.png')
snake_body = pygame.image.load('Body.png')
snake_tail = pygame.image.load('Tail.png')

pygame.init()
font = pygame.font.Font('ByteBounce.ttf', 40)
# Slower to load option
# font = pygame.font.SysFont('arial', 25)

# Changes to adapt the AI agent
# Reset game
# Each game returns a reward
# modify play_step(action) returns a direction
# Track the current "state"?
# modify is_collision

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class SnakeGameAI:
    def __init__(self, width=800, height=450):
        self.width = width
        self.height = height

        #init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        self.reset()

    def reset(self):
        # init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.width / 2, self.height / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - 2 * BLOCK_SIZE, self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
        self.frame_count = 0

    def _place_food(self):
        x = random.randint(0, (self.width - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.height - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)

        # if food inside snake call again
        if self.food in self.snake:
            self._place_food()

    def play_step(self, action):
        self.frame_count += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         self.direction = Direction.LEFT
            #     elif event.key == pygame.K_RIGHT:
            #         self.direction = Direction.RIGHT
            #     elif event.key == pygame.K_UP:
            #         self.direction = Direction.UP
            #     elif event.key == pygame.K_DOWN:
            #         self.direction = Direction.DOWN

        # 2. move snake
        # update the head
        self._move(action)
        self.snake.insert(0, self.head)

        # 3. check if game over
        reward = 0
        check_game_over = False
        if self.is_collision() or self.frame_count > 100*len(self.snake):
            check_game_over = True
            reward = -10
            return reward, check_game_over, self.score

        # 4. place food or just move
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui(apple)
        self.clock.tick(SPEED)

        # 6. return if game over and score
        return reward, check_game_over, self.score

    def _move(self, action):
        # [straight, right, left]
        clockwise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clockwise.index(self.direction)

        if np.array_equal(action, [1, 0, 0]):
            new_direction = clockwise[idx] # no change
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_direction = clockwise[next_idx] # right turn
        else: # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_direction = clockwise[next_idx]
        self.direction = new_direction

        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x, y)

    def is_collision(self, point=None):
        if point is None:
            point = self.head

        # hits boundary
        if point.x > self.width - BLOCK_SIZE or point.x < 0 or point.y > self.height - BLOCK_SIZE or point.y < 0:
            return True

        #hits itself
        if point in self.snake[1:]:
            return True

        return False

    def _update_ui(self, apple_par):
        self.display.blit(background, (0, 0))

        # draw snake
        self._draw_snake()

        # alternate scale
        factor = 1 + 0.15 * math.sin(self.frame_count)
        apple_scaled = pygame.transform.scale(apple_par, (32 * factor, 32 * factor))

        # get rect centered on the food position
        apple_rect = apple_scaled.get_rect(center=(self.food.x + BLOCK_SIZE // 2, self.food.y + BLOCK_SIZE // 2))
        self.display.blit(apple_scaled, apple_rect.topleft)

        # score
        white = (255, 255, 255)
        text = font.render('Score: ' + str(self.score), True, white)
        self.display.blit(text, (0, 0))
        pygame.display.flip()

    def _draw_snake(self):
        global snake_head
        for point in self.snake:
            if point == self.head: # draw head
                if self.direction == Direction.RIGHT:
                    self.display.blit(snake_head, (point.x, point.y))
                elif self.direction == Direction.LEFT:
                    rotated_snake_head = pygame.transform.rotate(snake_head, 180)
                    self.display.blit(rotated_snake_head, (point.x, point.y))
                elif self.direction == Direction.UP:
                    rotated_snake_head = pygame.transform.rotate(snake_head, 90)
                    self.display.blit(rotated_snake_head, (point.x, point.y))
                elif self.direction == Direction.DOWN:
                    rotated_snake_head = pygame.transform.rotate(snake_head, -90)
                    self.display.blit(rotated_snake_head, (point.x, point.y))
            elif point == self.snake[-1]: # draw tail
                if self.snake[-2].x > point.x: #right
                    self.display.blit(snake_tail, (point.x, point.y))
                elif self.snake[-2].x < point.x: # left
                    rotated_snake_tail = pygame.transform.rotate(snake_tail, 180)
                    self.display.blit(rotated_snake_tail, (point.x, point.y))
                elif self.snake[-2].y > point.y: # up
                    rotated_snake_tail = pygame.transform.rotate(snake_tail, -90)
                    self.display.blit(rotated_snake_tail, (point.x, point.y))
                else: # down
                    rotated_snake_tail = pygame.transform.rotate(snake_tail, 90)
                    self.display.blit(rotated_snake_tail, (point.x, point.y))
            else: # draw body
                self.display.blit(snake_body, (point.x, point.y))

# if __name__ == '__main__':
#     game = SnakeGameAI()
#
#     # game loop
#     while True:
#         reward, game_over, score = game.play_step()
#
#         if game_over:
#             break
#
#     print("Final score:", score)
#
#     pygame.quit()

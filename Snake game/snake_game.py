import math
import sys

import pygame
import random
from enum import Enum
from collections import namedtuple

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


Point = namedtuple('Point',  'x, y')
background = pygame.image.load('Background.png')
apple = pygame.image.load('Apple.png')
apple_center = apple.get_rect().center

BLOCK_SIZE = 25
SPEED = 7

pygame.init()
font = pygame.font.Font('ByteBounce.ttf', 40)
# Slower to load option
# font = pygame.font.SysFont('arial', 25)

BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)

class SnakeGame:

    def __init__(self, width=800, height=450):
        self.width = width
        self.height = height

        #init display
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()

        #init game state
        self.direction = Direction.RIGHT

        self.head = Point(self.width / 2, self.height / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - 2*BLOCK_SIZE, self.head.y)]

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

    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # 2. move snake
        # update the head
        self._move(self.direction)
        self.snake.insert(0, self.head)

        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. place food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        # 5. update ui and clock
        self._update_ui(apple)
        self.clock.tick(SPEED)
        # 6. return if game over and score
        return game_over, self.score

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE

        self.head = Point(x, y)

    def _is_collision(self):
        # hits boundary
        if self.head.x > self.width - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.height - BLOCK_SIZE or self.head.y < 0:
            return True

        #hits itself
        if self.head in self.snake[1:]:
            return True

        return False

    def _update_ui(self, apple_par):
        self.display.blit(background, (0, 0))

        # draw snake
        for point in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(point.x, point.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(point.x + 4, point.y + 4, BLOCK_SIZE / 2, BLOCK_SIZE / 2))

        # alternate scale
        self.frame_count += 1
        factor = 1 + 0.2 * math.sin(self.frame_count)
        apple_scaled = pygame.transform.scale(apple_par, (32 * factor, 32 * factor))

        # get rect centered on the food position
        apple_rect = apple_scaled.get_rect(center=(self.food.x + BLOCK_SIZE // 2, self.food.y + BLOCK_SIZE // 2))
        self.display.blit(apple_scaled, apple_rect.topleft)

        # score
        white = (255, 255, 255)
        text = font.render('Score: ' + str(self.score), True, white)
        self.display.blit(text, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':

    game = SnakeGame()

    # game loop
    while True:
        game_over, score = game.play_step()

        if game_over:
            break

    print("Final score", score)

    pygame.quit()

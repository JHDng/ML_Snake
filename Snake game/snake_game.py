import math
import sys
import pygame
import random
from enum import Enum
from collections import namedtuple

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

class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

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
        check_game_over = False
        if self._is_collision():
            check_game_over = True
            return check_game_over, self.score

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
        return check_game_over, self.score

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
        self._draw_snake()

        # alternate scale
        self.frame_count += 1
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

if __name__ == '__main__':
    game = SnakeGame()

    # game loop
    while True:
        game_over, score = game.play_step()

        if game_over:
            break

    print("Final score:", score)

    pygame.quit()

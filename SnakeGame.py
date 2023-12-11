import pygame
from Direction import Direction
from collections import namedtuple
import random

# lighweight object, takes 2 args only - name, vars
point = namedtuple("point", "x, y") 

BLOCK_SIZE = 20
SPEED = 20

# rgb colours
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)


class SnakeGame:
    def __init__(self, w = 640, h=480):
        # all elements of the game
        self.w = w
        self.h = h
        
        # font
        self.font = pygame.font.Font("Arial.ttf", 25)
        
        # display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        
        # initialize game state
        # place initial food, snake and direction
        self.direction = Direction.RIGHT
        self.head = point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      point(self.head.x - BLOCK_SIZE, self.head.y), 
                      point(self.head.x - 2 * BLOCK_SIZE, self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        
    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = point(x, y)
        # check food is not placed in the snake
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self):
        # 1. collect user input
        # 2. move
        # 3. check if game over
        # 4. place new food or just move
        # 5. update ui and clock
        
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
                    
        # 2. move
        self._move(self.direction)
        self.snake.insert(0, self.head)
        
        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score
        
        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop() # check this
            
        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED) # game speed
        
        # 6. return game over and score
        return game_over, self.score
    
    def _update_ui(self):
        self.display.fill(BLACK)
        
        for pt in self.snake:
            # outline
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            # fill
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
            
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        # label
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.display.blit(text, [0, 0])
        # update  
        pygame.display.flip()
        
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
            
        self.head = point(x, y)
        
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
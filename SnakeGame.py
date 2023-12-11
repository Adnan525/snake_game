import pygame

class SnakeGame:
    def __init__(self, w = 640, h=480):
        self.w = w
        self.h = h
        # display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption("Snake Game")
        # initialize game state
        
    def play_step(self):
        pass
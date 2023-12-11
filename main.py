import pygame
import random
from SnakeGame import SnakeGame

pygame.init()

if __name__ == "main":
    game = SnakeGame()
    
    # game loop
    while True:
        game.play_step()
        
        # game over
        
    pygame.quit()
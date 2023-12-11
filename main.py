import pygame
from SnakeGame import SnakeGame

pygame.init()
pygame.font.init()
if __name__ == "__main__":
    game = SnakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        if game_over:
            break
        
    print(f"Final score is {score}")
        
    pygame.quit()
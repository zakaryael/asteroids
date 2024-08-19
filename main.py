import pygame
from constants import *

def main():
    print(f"Starting asteroids! \nScreen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = game_clock.tick(FPS) / 1000

if __name__ == "__main__":
          main()

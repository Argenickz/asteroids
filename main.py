import pygame
from constants import *
from player import Player
screen_color = 'black'


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    watch = pygame.time.Clock()
    dt = 0
    updatable = player.update(dt)
    drawable = player.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color=screen_color)
        
        for entity in Player.containers(updatable, drawable):
            entity.update(dt)
            entity.draw(screen)

        pygame.display.flip()

        watch.tick(60)
        dt = watch.tick(60) / 1000
        





if __name__ == "__main__":
    main()
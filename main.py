import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
screen_color = 'black'


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Initializes the pygame module
    pygame.init()
    watch = pygame.time.Clock()
    dt = 0


    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)


    # Objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field_object = AsteroidField()
    player.cooldown = PLAYER_SHOOT_COOLDOWN

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        for entity in updatable:
            entity.update(dt)
            

        screen.fill(color=screen_color)


        for entity in drawable:
            entity.draw(screen)

        
        for asteroid in asteroids:
            if asteroid.collide(player):
                print('Game over!')
                sys.exit()
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()


        pygame.display.flip()
    

        dt = watch.tick(60) / 1000
        

if __name__ == "__main__":
    main()
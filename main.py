import pygame
from constants import *
from player import Player
screen_color = 'black'


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Initializes the pygame module
    pygame.init()

    # Creates groups of updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # This was my code:
    # groups = Player.container(updatable, drawable)
    # This is the correct way:
    Player.containers = (updatable, drawable)
    # This is what the instructions meant by 'creating a static variable, this was created in the main.py, not in the class declaration'
    
    # Creates a screen object from the pygame module
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Creates a player object from the Player class
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    watch = pygame.time.Clock()
    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color=screen_color)


        # Note, this iterates over the 'updatables' and like the loop below, it gets the 'Player' 
        # class attributes and methods when added to the containers.
        for entity in updatable:
            entity.update(dt)

        for entity in drawable:
            entity.draw(screen)
        
        

        pygame.display.flip()

        dt = watch.tick(60) / 1000
        





if __name__ == "__main__":
    main()
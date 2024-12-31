from circleshape import CircleShape
import pygame
from constants import *
# import the random module
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    # Add new .split() method to the asteroid class
    def split(self):
        # Asteroid immediatly kills itself, we'll spawn new ones.
        self.kill()
        

        # This checks if it's a small asteroid, returns none if it is.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # The else statement is to return two new asteroids
        else:
            # Create a random angle between and included the given arguments
            rand_angle = random.uniform(20, 50)

            # Use the rotate method on the asteroid's velocity to create two new vectors
            # that are rotated by rand_angle and -rand_angle respectively.
            vector1 = self.velocity.rotate(rand_angle)
            vector2 = self.velocity.rotate(-rand_angle)

            # Compute the new radius of the smaller asteroids using the formula:
            #  old_radius - ASTEROID_MIN_RADIUS
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create two new asteroid objects at the current asteroid position with the
            # new radius
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y,  new_radius)

            # Set both asteroids velocity to the new vectors respectively and multiply
            # by 1.2 to speed them up.
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2




    

        
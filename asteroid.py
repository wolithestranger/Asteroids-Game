from circle_shape import CircleShape
import pygame
import random
#from constants import ASTEROID_MIN_RADIUS
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)
        #return super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: #if asteroid alredy @ smallest size
            return 
        else:
            random_angle = random.uniform(20,50) #generate angle between 20 and 50
            #rotate(random_angle) -> Vector2
            # to split and shoot off in two random but opposite angles.
            # remember velocity is a vector i.e speed and direction
            new_velocity_1 = self.velocity.rotate(random_angle)
            new_velocity_2 = self.velocity.rotate(-random_angle)
            #radius of smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            smaller_asteroid_1 =  Asteroid(self.position.x, self.position.y ,new_radius)
            smaller_asteroid_1.velocity =  new_velocity_1 * 1.2 # to make asteroid slightly faster

            smaller_asteroid_2 =  Asteroid(self.position.x, self.position.y,new_radius)
            smaller_asteroid_2.velocity =  new_velocity_2 * 1.2

            asteroids.add(smaller_asteroid_1)
            asteroids.add(smaller_asteroid_2)

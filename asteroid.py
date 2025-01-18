from circle_shape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)
        #return super().draw(screen)

    def update(self, dt):
        self.position += self.velocity * dt


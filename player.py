import pygame 
from circle_shape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        points = self.triangle()
        print(f"Drawing triangle at points: {points}")
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        # color = "white"
        # points = triangle()
        # width = 2

    def rotate(self, dt):
        self.rotation += (dt*PLAYER_TURN_SPEED) 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]: #left
            self.rotate(-dt)
        if keys[pygame.K_d]: #right 
            self.rotate(dt)
        if keys[pygame.K_w]: #up
            self.move(dt)
        if keys[pygame.K_s]: #down
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        # Decrease timer by dt
        self.timer = self.timer - dt  # or self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        #check if we can shoot
        if self.timer > 0:
            return 
        self.timer = PLAYER_SHOT_COOLDOWN 
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot_velocity = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity = shot_velocity* PLAYER_SHOOT_SPEED
        return new_shot



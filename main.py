import pygame
import sys

from constants import * #import everything from constants file... * means everything
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable,drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Player position: {player.position}")

    pygame.init()

    clock = pygame.time.Clock() #to create pygame clock object
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    #main game loop
    while True:
        #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill(color, rect=None, special_flags=0) -> rect
        screen.fill(color = (0,0,0))#000000
        print("About to draw player")  # Add this debug line

        for sprite in updatable:
            sprite.update(dt)
            #player.update(dt)

        #collision checks
        for asteroid in asteroids:
            if asteroid.collision_check(player):# if player collides with asteroid
                print("Game Over")
                sys.exit()
                #SystemExit

        #couuld just put this for loop within asteroid for loop. so one nested loop
        for asteroid in asteroids:# shot destroys asteroids
            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()# bullet is killed after asteroid is destroyed
                    asteroid.split(asteroids)

        
        for sprite in drawable:
            sprite.draw(screen)
            #player.draw(screen)

        pygame.display.flip() #refreshes the screen

        dt = (clock.tick(60))/1000 ## limit the framerate to 60 FPS


if __name__ == "__main__":
    main()
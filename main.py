import pygame

from constants import * #import everything from constants file... * means everything
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Player position: {player.position}")

    pygame.init()

    clock = pygame.time.Clock() #to create pygame clock object
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    while True:
        #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill(color, rect=None, special_flags=0) -> rect
        screen.fill(color = (0,0,0))#000000
        print("About to draw player")  # Add this debug line
        player.draw(screen)
        pygame.display.flip() #refreshes the screen

        dt = (clock.tick(60))/1000 #Storing the delta time in seconds


if __name__ == "__main__":
    main()
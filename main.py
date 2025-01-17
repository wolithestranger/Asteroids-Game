import pygame

from constants import * #import everything from constants file... * means everything
#from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    while True:
        #This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #fill(color, rect=None, special_flags=0) -> rect
        screen.fill(color = (0,0,0))#000000
        pygame.display.flip() #refreshes the screen

if __name__ == "__main__":
    main()
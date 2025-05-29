import pygame
from constants import *
from player import *

updatables = pygame.sprite.Group()
drawables  = pygame.sprite.Group()
Player.containers = (updatables, drawables)


def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    #print(f'Screen width: {SCREEN_WIDTH}')
    #print(f'Screen height: {SCREEN_HEIGHT}')
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        dt = clock.tick(60) / 1000
        updatables.update(dt)
         
        for draw in drawables:
            draw.draw(screen)
        
        

        
        pygame.display.flip()
        #clock.tick(60)
        
        

        # limit the framerate to 60 FPS
        
if __name__ == "__main__":
    main()

    
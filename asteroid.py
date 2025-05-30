from circleshape import *

class Player(CircleShape):
    def __init__(self,x,y,radius):
    #super().__init__(x,y,PLAYER_RADIUS)



    def draw(self, screen):
            # sub-classes must override
            pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)



    def update(self, dt):
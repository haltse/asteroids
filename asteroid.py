import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):  
        
        randroid =random.uniform(20,50)
        old_radius = self.radius
        old_position = self.position  
        old_velocity = self.velocity
        new_velocity1 = old_velocity.rotate(randroid)
        new_velocity2 = old_velocity.rotate(-randroid)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        self.kill()  
        if old_radius <= ASTEROID_MIN_RADIUS:         
                    
            return # small asteroid cant get smaller.
        else:
            
            new_asteroid1 = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid2 = Asteroid(old_position.x, old_position.y, new_radius)
            new_asteroid1.velocity = new_velocity1 * 1.2
            new_asteroid2.velocity = new_velocity2 * 1.2






from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast_1 = Asteroid(self.position[0], self.position[1], new_radius)
            ast_2 = Asteroid(self.position[0], self.position[1], new_radius)
            angle = random.uniform(20,50)
            vel = self.velocity.rotate(angle)
            vel_inv = self.velocity.rotate(-angle)

            ast_1.velocity = vel * 1.2
            ast_2.velocity = vel_inv * 1.2

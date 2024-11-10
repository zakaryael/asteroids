from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # get the forward which is the direction the player is facing by taking the vector (0, 1) and rotating it by the player's rotation
        self.position += forward * PLAYER_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_h]:
            self.rotate(-dt)
        if keys[pygame.K_k]:
            self.move(dt)
        if keys[pygame.K_j]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        self.timer -= dt

    def shoot(self, dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = PLAYER_SHOOT_SPEED * pygame.Vector2(0, 1).rotate(self.rotation)
            self.timer = PLAYER_SHOOT_COOLDOWN
        

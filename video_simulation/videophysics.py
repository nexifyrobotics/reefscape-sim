import math
import numpy as np

class Robot:
    def __init__(self, x=100, y=100, speed=2):
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = speed
        self.size = 10

    def move_forward(self):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed

    def turn_towards(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        self.angle = math.degrees(math.atan2(dy, dx))

    def detect_collision(self, obstacles):
        for (ox, oy, ow, oh) in obstacles:
            if ox < self.x < ox + ow and oy < self.y < oy + oh:
                return True
        return False

    def bounce(self):
        self.angle += np.random.choice([-90, 90, 135, -135])
        self.x -= math.cos(math.radians(self.angle)) * self.speed * 5
        self.y -= math.sin(math.radians(self.angle)) * self.speed * 5
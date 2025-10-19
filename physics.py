import math

class Robot:
    def __init__(self, x=0, y=0, angle=0, speed=5):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def angle_to(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        return math.degrees(math.atan2(dy, dx))

    def rotate(self, target_angle):
        diff = target_angle - self.angle
        self.angle += diff
        return diff

    def move_forward(self):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed
        return self.x, self.y
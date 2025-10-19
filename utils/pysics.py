import math

class Robot:
    def __init__(self, x=0, y=0, angle=0, speed=0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def rotate(self, target_angle, max_turn=5):
        diff = (target_angle - self.angle + 180) % 360 - 180
        if abs(diff) < max_turn:
            self.angle = target_angle
        else:
            self.angle += max_turn if diff > 0 else -max_turn
        self.angle %= 360

    def move_forward(self):
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

    def distance_to(self, target_x, target_y):
        return math.hypot(target_x - self.x, target_y - self.y)

    def angle_to(self, target_x, target_y):
        dx = target_x - self.x
        dy = target_y - self.y
        return (math.degrees(math.atan2(dy, dx))) % 360
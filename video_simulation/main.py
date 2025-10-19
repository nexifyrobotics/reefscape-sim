import cv2
import numpy as np
from videophysics import Robot

tag_pos = (500, 300)

robot = Robot()

obstacles = [
    (200, 200, 100, 20),
    (350, 100, 30, 150),
    (450, 350, 100, 20)
]

while True:
    sim = np.zeros((480, 640, 3), dtype=np.uint8)

    for (ox, oy, ow, oh) in obstacles:
        cv2.rectangle(sim, (ox, oy), (ox + ow, oy + oh), (100, 100, 100), -1)

    cv2.circle(sim, tag_pos, 15, (0, 0, 255), -1)

    robot.turn_towards(*tag_pos)
    robot.move_forward()

    if robot.detect_collision(obstacles):
        robot.bounce()

    cv2.circle(sim, (int(robot.x), int(robot.y)), robot.size, (255, 255, 255), -1)
    cv2.putText(sim, "Rota: AprilTag'e ilerliyor", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

    cv2.imshow("Simulasyon", sim)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
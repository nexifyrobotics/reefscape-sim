import os
import cv2
import numpy as np
import pupil_apriltags as apriltag
from physics import Robot

TAG_SIZE = 0.16
FOCAL_LENGTH = 700

cap = cv2.VideoCapture(0)
detector = apriltag.Detector()
robot = Robot()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera bulunamadı.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = detector.detect(gray)

    for d in detections:
        (ptA, ptB, ptC, ptD) = np.int32(d.corners)
        center_x, center_y = map(int, d.center)
        perceived_width = np.linalg.norm(ptA - ptB)
        distance = (TAG_SIZE * FOCAL_LENGTH) / perceived_width if perceived_width > 0 else None
        offset_x = center_x - frame.shape[1]/2

        target_angle = robot.angle_to(center_x, center_y)
        diff_angle = robot.rotate(target_angle)
        robot.move_forward()

        if distance:
            if abs(offset_x) < 50:
                action = "İLERİ" if distance > 60 else "DUR"
            elif offset_x > 50:
                action = "SAĞA DÖN"
            else:
                action = "SOLA DÖN"
        else:
            action = "Tag algılanamadı"

        cv2.polylines(frame, [np.array([ptA, ptB, ptC, ptD])], True, (0, 255, 0), 2)
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
        cv2.putText(frame, f"{action}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        print(f"Tag {d.tag_id} | Mesafe: {distance:.1f} | Offset: {offset_x:.1f} | Aksiyon: {action} | Döndüğü açı: {diff_angle:.1f}")

    cv2.imshow("Otonom Simulasyon", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
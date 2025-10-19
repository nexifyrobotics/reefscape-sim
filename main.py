import cv2
import numpy as np
import apriltag
import cairosvg
import os
import matplotlib.pyplot as plt

TAG_DIR = "tags"

def svg_to_png(svg_path, png_path):
    cairosvg.svg2png(url=svg_path, write_to=png_path)

detector = apriltag.Detector()

png_tags = []
for svg_file in os.listdir(TAG_DIR):
    if svg_file.endswith(".svg"):
        png_path = os.path.join(TAG_DIR, svg_file.replace(".svg", ".png"))
        svg_to_png(os.path.join(TAG_DIR, svg_file), png_path)
        png_tags.append(png_path)

for tag_img in png_tags:
    frame = cv2.imread(tag_img, cv2.IMREAD_GRAYSCALE)
    detections = detector.detect(frame)
    
    print(f"\n[{tag_img}]")
    if not detections:
        print("→ Hiç tag algılanmadı.")
    else:
        for d in detections:
            print(f"→ Tag ID: {d.tag_id}")
            for (x, y) in d.corners:
                cv2.circle(frame, (int(x), int(y)), 4, (0, 255, 0), -1)
    
    plt.imshow(frame, cmap="gray")
    plt.title(f"Detection result: {tag_img}")
    plt.axis("off")
    plt.show()
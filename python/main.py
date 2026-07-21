import cv2
from pathlib import Path

project_folder = Path(__file__).parent.parent

img_path = project_folder / "assets" / "basketball.jpg"

img = cv2.imread(img_path)

small_img = cv2.resize(img, (800, 600))
cv2.imshow('Basketball', small_img)

cv2.waitKey(0)

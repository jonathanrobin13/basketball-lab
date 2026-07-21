import cv2
# from pathlib import Path

# project_folder = Path(__file__).parent.parent

# img_path = project_folder / "assets" / "basketball.jpg"

# img = cv2.imread(img_path)

# small_img = cv2.resize(img, (800, 600))
# cv2.imshow('Basketball', small_img)

# cv2.waitKey(0)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

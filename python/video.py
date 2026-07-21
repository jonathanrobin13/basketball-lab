import cv2
from pathlib import Path

project_folder = Path(__file__).parent.parent

video_path = project_folder / "assets" / "real_throw.mp4"

# Takes in video path or integer for camera
video = cv2.VideoCapture(0)

while True:

    # Returns true if there is no frame
    isTrue, frame = video.read()

    if not isTrue:
        break

    # Displays frame
    cv2.imshow('Basketball free throw', frame)

    # waits 20 milliseconds and checks if user pressed q
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Stops connection with video
video.release()

cv2.destroyAllWindows()

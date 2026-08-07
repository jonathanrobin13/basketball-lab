from ultralytics import YOLO
import cv2
from pathlib import Path
import time
import shutil

project_folder = Path(__file__).parent.parent

model_path = project_folder / "models" / "yolov8n.pt"

if model_path.exists():
    model = YOLO(model_path)
else:
    print("This can take a few moments...")

    model = YOLO("yolov8n.pt")

    new_model_path = project_folder / "models" / "yolov8n.pt"
    current_model_path = project_folder / "python" / "yolov8n.pt"

    shutil.move(current_model_path, new_model_path)

    model_path = new_model_path


video_path = project_folder / "assets" / "real_throw.mp4"

cap = cv2.VideoCapture(1)

fps_for_frames = []
fps = 0
average_fps = 0

while cap.isOpened():

    start = time.perf_counter()

    success, frame = cap.read()

    if success:

        results = model.track(
            source=frame, tracker='bytetrack.yaml', persist=True, verbose=False, conf=0.1, classes=[32])

        # Get X Y coords for getting precise calculations for ball
        if len(results[0].boxes) > 0:
            x1, y1, x2, y2 = results[0].boxes.xyxy[0]
            ball_box = frame[int(y1):int(y2), int(x1):int(x2)]

            grayscale = cv2.cvtColor(ball_box, cv2.COLOR_BGR2GRAY)

            grayscale = cv2.medianBlur(grayscale, 5)

            ball = cv2.HoughCircles(grayscale, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                                    param1=70, param2=70, minRadius=30, maxRadius=120)

            if ball is not None:
                ball = ball[0].astype(int)

                # Gets x coord of ball and y coord inside the box
                ball_x_box = ball[0][0]
                ball_y_box = ball[0][1]

                radius = ball[0][2]

                # Gets the actual coord of the ball inside the frame
                ball_x_frame = ball_x_box + int(x1)
                ball_y_frame = ball_y_box + int(y1)

                # Outside circle
                cv2.circle(frame, (ball_x_frame, ball_y_frame),
                           radius, (255, 0, 0), 8)

                # Inner circle
                cv2.circle(frame, (ball_x_frame, ball_y_frame),
                           2, (0, 0, 0), 3)

        cv2.putText(frame, f"FPS {average_fps:.1f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
                    )
        cv2.imshow("Basketball identification", frame)

        end = time.perf_counter()
        fps = 1 / (end - start)
        fps_for_frames.append(fps)

        if len(fps_for_frames) > 20:
            fps_for_frames.pop(0)

        average_fps = sum(fps_for_frames) / len(fps_for_frames)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2
from pathlib import Path
import time
import shutil

project_folder = Path(__file__).parent.parent

try:
    model_path = project_folder / "models" / "yolov8n.pt"
    model = YOLO(model_path)
except FileNotFoundError:

    print("This can take a few moments...")

    model = YOLO("yolov8.pt")
    model_path = project_folder / "python" / "yolov8n.pt"

    new_model_path = project_folder / "models" / "yolov8n.pt"

    shutil.move(model_path, new_model_path)

    model_path = new_model_path


video_path = project_folder / "assets" / "real_throw.mp4"


cap = cv2.VideoCapture(1)

while cap.isOpened():

    success, frame = cap.read()

    if success:

        start = time.perf_counter()
        results = model(source=frame, classes=[32], verbose=False)

        end = time.perf_counter()
        total_time = end - start
        fps = 1 / total_time

        annotated_frame = results[0].plot()

        cv2.putText(annotated_frame, f"FPS {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
                    )
        cv2.imshow("Basketball identification", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

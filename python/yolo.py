from ultralytics import YOLO
import cv2
from pathlib import Path
import time
import shutil

project_folder = Path(__file__).parent.parent

# try:
#     model_path = project_folder / "models" / "yolov8n.pt"
#     model = YOLO(model_path)
# except FileNotFoundError:

#     print("This can take a few moments...")

#     model = YOLO("yolov8.pt")

#     new_model_path = project_folder / "models" / "yolov8n.pt"

#     shutil.move(model_path, new_model_path)

#     model_path = new_model_path

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

fps = 0
skip_frame = False

while cap.isOpened():

    success, frame = cap.read()

    if success:

        start = time.time()
        if not skip_frame:
            results = model.track(source=frame, tracker='bytetrack.yaml', persist=True, classes=[
                32], verbose=False, conf=0.1)

            annotated_frame = results[0].plot()

            skip_frame = True
        else:
            skip_frame = False

        end = time.time()
        fps = 1 / (end - start)

        cv2.putText(annotated_frame, f"FPS {fps:.1f}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1
                    )
        cv2.imshow("Basketball identification", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

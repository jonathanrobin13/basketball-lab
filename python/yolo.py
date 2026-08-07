from ultralytics import YOLO
from pathlib import Path
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

results = model.track(source=0, conf=0.1, verbose=False,
                      classes=[32], tracker="bytetrack.yaml")

import torch
import cv2
from ultralytics import YOLO
import time

# Load YOLOv5s model (small, fast)
model = YOLO('yolov8n.pt')  # Ultralytics YOLOv8 Nano model

# Use GPU if available
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)
print(f"Running on device: {device}")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    start_time = time.time()

    # Run object detection
    results = model(frame, verbose=False)

    end_time = time.time()
    fps = 1 / (end_time - start_time)

    # Plot results
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("GPU Object Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

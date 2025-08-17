# Real-time Object Detection with GPU Acceleration

## Overview
**Project:** Real-time Object Detection with GPU Acceleration.

Demonstrates the use of the AI to detect and label objects visible by a camera. Allows for GPU acceleration to improve performance.

---

## Features
- Real-time object detection and labelling
- Utilises ResNet-18 Convolutional Neural Network (CNN) alongside YOLOv8, OpenCV and CUDA
- GPU acceleration

---

## Code
- Written in Python
- Script located in the `code/` folder

---

## Setup
- Requires installation of PyTorch, OpenCV and Ultralytics YOLO libraries
- Camera required for video stream
- CUDA must be installed for GPU acceleration

```bash
# Clone the repo
git clone https://github.com/musa-z/real-time-object-detection-with-gpu.git

# Navigate to code folder
cd real-time-object-detection-with-gpu/code

# Run main script
python gpu_object_detection.py

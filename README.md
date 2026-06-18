# Real-Time Object Detection with GPU Acceleration

Python-based real-time object detection project using YOLOv8, OpenCV and optional CUDA/GPU acceleration. The system processes a live camera stream, detects objects in each frame and displays labelled detections in real time.

## Overview

This project demonstrates a real-time computer vision pipeline for object detection using a webcam or connected camera.

The system captures video frames, runs object detection using YOLOv8, overlays bounding boxes and class labels, and displays the processed output. CUDA/GPU acceleration can be used when available to improve inference speed compared with CPU-only execution.

## Key Features

- Built a real-time object detection pipeline using Python, YOLOv8 and OpenCV
- Processed live camera frames and displayed labelled object detections
- Used CUDA/GPU acceleration when available for faster inference
- Displayed bounding boxes, class labels and confidence scores on video frames
- Supported CPU fallback for systems without compatible GPU hardware
- Structured as a simple camera-based perception pipeline suitable for robotics and edge-AI applications

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- CUDA
- Webcam / camera input
- Real-time video processing

## Repository Structure

    real-time-object-detection-with-gpu/
    ├── code/
    │   └── gpu_object_detection.py
    ├── README.md
    └── LICENSE.txt

## System Pipeline

    Camera Input
         ↓
    Frame Capture with OpenCV
         ↓
    YOLOv8 Object Detection
         ↓
    Bounding Box and Label Overlay
         ↓
    Real-Time Display
         ↓
    CPU/GPU Performance Comparison

## Method

The script captures frames from a connected camera using OpenCV and passes each frame through a YOLOv8 object detection model. Detected objects are returned with class labels, confidence scores and bounding-box coordinates.

The detections are drawn onto each frame and displayed in real time. When CUDA is available, inference can run on the GPU to improve processing speed. If CUDA is not available, the pipeline can still run on the CPU.

## Setup

Clone the repository:

    git clone https://github.com/musa-z/real-time-object-detection-with-gpu.git
    cd real-time-object-detection-with-gpu/code

Install dependencies:

    pip install -r ../requirements.txt

Run the detection script:

    python gpu_object_detection.py

## Requirements

A connected webcam or camera is required for live detection.

CUDA-compatible GPU acceleration requires:

- NVIDIA GPU
- CUDA installed
- PyTorch build with CUDA support

The project can still run on CPU if CUDA is not available, but inference speed may be lower.

## Limitations and Future Improvements

Performance depends on camera quality, lighting conditions, object visibility, model size, hardware capability and whether CUDA acceleration is available.

Future improvements would include adding FPS logging, saving annotated video output, comparing CPU vs GPU inference speed, supporting image/video file input, and adding a robotics-focused output interface such as ROS2 camera topic integration.

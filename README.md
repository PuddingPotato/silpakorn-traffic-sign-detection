# 🚦 Traffic Sign Detection at Silpakorn University

A custom object detection system designed to identify traffic signs within Silpakorn University’s Sanam Chandra Campus — where many signs differ significantly from standard traffic signage, making public datasets unsuitable. This project builds a full end-to-end pipeline from dataset creation to model training and evaluation using YOLOv8.

---

## 🔍 Project Overview

This project focuses on detecting campus-specific traffic signs using computer vision. Due to the unique nature of the signs found within the university, the model relies entirely on a self-built dataset, tailored to the environment of Silpakorn University's Sanam Chandra Campus.

---

## 🔗 Project Resources

Below are links to the dataset and model results **from this project**:

- 📦 **Dataset on Roboflow Universe (Created by Me):**
  [🔗 View My Dataset →]([https://universe.roboflow.com/your-dataset-link](https://universe.roboflow.com/project-traffic-sign-detection/traffic-sign-detection-67tod))

- 📁 **Model Results on Google Drive (Trained Models from This Project):**  
  [🔗 View My Model Outputs →](https://drive.google.com/drive/folders/1YvFpNQmwjvlRPpupJLrQF4AcKA-t_azF?usp=sharing)

---

## 📸 Data Collection & Preparation

- Captured on-campus video footage containing traffic signs.
- Extracted individual image frames from video files.
- Annotated images using **Roboflow**, labeling various types of signs.
- Performed image resizing and **augmentation** to enhance dataset quality.
- Exported the dataset in YOLOv8-compatible format.

---

## 🧠 Model Training

Trained five variants of the YOLOv8 model to compare performance:

- `yolov8n`
- `yolov8s`
- `yolov8m`
- `yolov8l`
- `yolov8x`

Each model was trained using the prepared dataset with consistent preprocessing settings for fair comparison.

---

## 📈 Monitoring & Evaluation

Model experiments were tracked using **Comet ML**, allowing for:

- Real-time training monitoring
- Metrics comparison across models
- Visualization of model performance

---

## 🛠 Tech Stack

- YOLOv8 | Object detection model
- Roboflow | Annotation, augmentation, export
- Comet ML | Training monitoring and analytics
- OpenCV | Frame extraction from video

---


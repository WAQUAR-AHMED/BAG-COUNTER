# BAG-COUNTER
This project detects and counts bags crossing a defined line using YOLOv8 and OpenCV.
# Bag Counter Using YOLOv8

## Description
This project detects and counts bags crossing a defined line using YOLOv8 and OpenCV.

## Features
- Detects bags in video
- Draws bounding boxes
- Shows tracking ID on each bag
- Counts bags crossing Vertical line(Depends on Enviroment) 
- Prevents duplicate counting

## Technologies Used
- Python
- OpenCV
- YOLOv8 (Ultralytics)

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python BagCounter.py

## YOLOv8 Model Training Results

The model was trained using a custom annotated dataset for bag detection.

### Training Metrics

| Metric        | Value |
|--------------|--------|
| mAP@0.5      | 0.98   |
| mAP@0.5:0.95 | 0.77   |
| Precision    | 0.99   |
| Recall       | 0.99   |

### Training Details

- Epochs: 25
- Model: YOLOv8
- Framework: Ultralytics
- Dataset: Custom annotated bag dataset
- Image size: 640

### Observations

- The model achieved high detection accuracy.
- Precision and Recall values indicate stable detection.
- The model performs well under real-world loading conditions.
---

## Sample Detection Output
- Sample Output Video https://drive.google.com/file/d/1w2HTaiU49IP0v-QVTHJ44p1GNiYArCPd/view?usp=drive_link
- [![Watch the demo](https://drive.google.com/file/d/1w2HTaiU49IP0v-QVTHJ44p1GNiYArCPd/view?usp=drive_link)]
<img width="1044" height="632" alt="image" src="https://github.com/user-attachments/assets/802c7f7e-9e26-49fb-b1fa-4956d22c439f" />

<img width="1046" height="635" alt="image" src="https://github.com/user-attachments/assets/3e786fc7-b4c9-4924-9523-840378fee2d8" />

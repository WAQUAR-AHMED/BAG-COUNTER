import cv2
from ultralytics import YOLO

# -----------------------------
# Load model
# -----------------------------
model = YOLO(r"Processed_data/runs/detect/train/weights/best.pt")

# -----------------------------
# Open video
# -----------------------------
cap = cv2.VideoCapture(r"Dataset\Problem Statement Scenario1.mp4")

# -----------------------------
# Counter setup
# -----------------------------
count = 0
counted_ids = set()
previous_x = {}

# -----------------------------
# Vertical counting line
# Adjust this value if needed
# -----------------------------
line_x = 450

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        conf=0.5
    )

    # Draw vertical line
    cv2.line(frame, (line_x, 0), (line_x, frame.shape[0]), (0, 0, 255), 3)

    if results[0].boxes.id is not None:

        boxes = results[0].boxes.xyxy.cpu()
        ids = results[0].boxes.id.cpu()

        for box, track_id in zip(boxes, ids):

            x1, y1, x2, y2 = map(int, box)
            track_id = int(track_id)

            # Bottom-center point
            cx = int((x1 + x2) / 2)
            cy = int(y2)

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Draw ID text
            cv2.putText(frame,
                        f"ID: {track_id}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 255),
                        2)

            # Draw bottom-center point
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

            # Count LEFT -> RIGHT crossing
            if track_id in previous_x:
                prev_cx = previous_x[track_id]

                if prev_cx > line_x and cx <= line_x:
                    if track_id not in counted_ids:
                        count += 1
                        counted_ids.add(track_id)
                        print(f"Counted ID: {track_id}")

            previous_x[track_id] = cx

    # Show counter
    cv2.putText(frame,
                f"Count: {count}",
                (50, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (0, 255, 0),
                4)

    cv2.imshow("Bag Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

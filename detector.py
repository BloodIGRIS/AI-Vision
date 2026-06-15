from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image):

    results = model(image)

    detections = []
    counts = {}

    for box in results[0].boxes:

        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls]

        detections.append((label, conf))

        counts[label] = counts.get(label,0)+1

    return detections, counts, results[0].plot()





        
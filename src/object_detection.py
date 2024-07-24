import cv2

class ObjectDetector:
    def __init__(self):
        self.model = cv2.dnn.readNetFromONNX('models/yolov8n.pt')

    def detect_objects(self):
        # Capture frame from camer
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            return []
        
        blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(640, 640), swapRB=True, crop=False)
        self.model.setInput(blob)
        
        # Perform detection
        detections = self.model.forward()
        
        objects = []
        for detection in detections[0, 0, :, :]:
            confidence = detection[2]
            if confidence > 0.5:  # confidence threshold
                objects.append((detection[3:7] * frame.shape[1::-1]).astype(int).tolist())

        cap.release()
        return objects

import numpy as np
import requests
import tarfile
import os

# Define the URL and the local filename
url = "http://download.tensorflow.org/models/ssd_mobilenet_v2_coco_2018_03_29.tar.gz"
filename = "ssd_mobilenet_v2_coco_2018_03_29.tar.gz"

# Download the file
response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Extract the tar.gz file
with tarfile.open(filename, 'r:gz') as tar:
    tar.extractall(path="ssd_mobilenet_v2_coco_2018_03_29")



import tensorflow as tf

# Load a pre-trained model (e.g., SSD MobileNet)
model = tf.saved_model.load('ssd_mobilenet_v2_coco/saved_model')

def detect_objects(image):
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]
    
    detections = model(input_tensor)
    return detections

import cv2
import numpy as np

def preprocess_image(image):
    # Resize the image to the model's input size (300x300 for SSD MobileNet)
    image_resized = cv2.resize(image, (300, 300))
    
    # Convert the image to a tensor and normalize
    input_tensor = tf.convert_to_tensor(image_resized)
    input_tensor = input_tensor[tf.newaxis, ...]  # Add batch dimension
    return input_tensor

def detect_objects(image):
    input_tensor = preprocess_image(image)
    
    # Run inference
    detections = model(input_tensor)
    
    # Extract detection results
    return detections

def process_detections(detections, threshold=0.5):
    # Extract relevant information
    boxes = detections['detection_boxes'][0].numpy()
    class_ids = detections['detection_classes'][0].numpy().astype(int)
    scores = detections['detection_scores'][0].numpy()

    detected_objects = []
    
    for i in range(len(scores)):
        if scores[i] >= threshold:  # Filter by confidence threshold
            box = boxes[i]
            class_id = class_ids[i]
            detected_objects.append((class_id, box, scores[i]))
    
    return detected_objects

def main():
    # Capture an image from the drone's camera (pseudo-code)
    image = capture_image()  # Replace with actual SDK call
    
    # Detect objects in the image
    detections = detect_objects(image)
    
    # Process the detections
    detected_objects = process_detections(detections)
    
    # Define class IDs for buildings and roads (based on COCO dataset)
    BUILDING_CLASS_ID = 1  # Example class ID for buildings
    ROAD_CLASS_ID = 3      # Example class ID for roads
    
    for class_id, box, score in detected_objects:
        if class_id in [BUILDING_CLASS_ID, ROAD_CLASS_ID]:
            print(f"Detected object: Class ID {class_id}, Score: {score}, Box: {box}")

if __name__ == "__main__":
    main()
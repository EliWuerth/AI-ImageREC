from dronekit import connect, VehicleMode
import cv2
import time
import numpy as np

# Connect to the drone
def connect_drone(connection_string):
    vehicle = connect(connection_string, wait_ready=True)
    return vehicle

# Capture an image from the drone's camera
def capture_image(vehicle):
    # Assuming the drone has a camera and can capture images
    # This is a placeholder for actual image capture logic
    # You may need to use a specific method based on your camera setup
    image = np.zeros((300, 300, 3), dtype=np.uint8)  # Placeholder for an actual image
    return image

# Save the captured image
def save_image(image, filename):
    cv2.imwrite(filename, image)

def main():
    connection_string = 'udp:127.0.0.1:14550'  # Replace with your connection string
    vehicle = connect_drone(connection_string)
    
    try:
        while True:
            # Capture an image
            image = capture_image(vehicle)
            
            # Save the image with a timestamp
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"image_{timestamp}.jpg"
            save_image(image, filename)
            print(f"Captured and saved image: {filename}")
            
            time.sleep(5)  # Capture an image every 5 seconds

    except KeyboardInterrupt:
        print("Stopping image capture.")
    finally:
        vehicle.close()  # Close the vehicle connection

if __name__ == "__main__":
    main()
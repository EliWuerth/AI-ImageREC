import dji_sdk
import cv2
import time

# Initialize the DJI SDK
def initialize_sdk():
    # Connect to the drone
    dji_sdk.connect()

# Capture an image from the drone's camera
def capture_image():
    # Assuming the SDK has a method to capture an image
    image = dji_sdk.camera.capture()  # Replace with actual SDK call
    return image

# Save the captured image
def save_image(image, filename):
    cv2.imwrite(filename, image)

def main():
    initialize_sdk()
    
    try:
        while True:
            # Capture an image
            image = capture_image()
            
            # Save the image with a timestamp
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"image_{timestamp}.jpg"
            save_image(image, filename)
            print(f"Captured and saved image: {filename}")
            
            time.sleep(5)  # Capture an image every 5 seconds

    except KeyboardInterrupt:
        print("Stopping image capture.")
    finally:
        dji_sdk.disconnect()  # Disconnect from the drone

if __name__ == "__main__":
    main()

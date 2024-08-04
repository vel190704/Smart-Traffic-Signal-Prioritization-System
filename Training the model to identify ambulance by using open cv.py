import cv2
import numpy as np

# Load the pre-trained vehicle detection classifier (you may need to download it)
vehicle_cascade = cv2.CascadeClassifier('ambulance.xml')

# Load your video or image
cap = cv2.VideoCapture('Traffic.mp4')  # Replace with your video file

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for vehicle detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect vehicles in the frame
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through detected vehicles
    for (x, y, w, h) in vehicles:
        # Draw a rectangle around the detected vehicle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop the region of interest (ROI) containing the detected vehicle
        vehicle_roi = frame[y:y + h, x:x + w]

        # Apply ambulance detection logic here
        # You can use color, shape, or other features to identify ambulances in the ROI

        # For example, let's assume we identify an ambulance based on color (red)
        # Convert the ROI to HSV color space
        hsv_roi = cv2.cvtColor(vehicle_roi, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv_roi, lower_red, upper_red)

        # Calculate the percentage of red pixels in the ROI
        red_pixel_percentage = (cv2.countNonZero(mask) / (w * h)) * 100

        # If a certain threshold of red pixels is exceeded, consider it an ambulance
        if red_pixel_percentage > 20:
            cv2.putText(frame, 'Ambulance', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the frame with vehicle and ambulance detection
    cv2.imshow('Traffic with Ambulance Detection', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
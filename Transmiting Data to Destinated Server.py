import requests
import json
import time

# Define the destination HTTP endpoint on the traffic signal network
destination_url = "http://traffic-signal-server.com/api/receive-data"

# Function to send data to the destination server
def send_data(data):
    try:
        response = requests.post(destination_url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Error: {e}")
        return None

# Function to fetch real-time GPS data (replace with your actual data source)
def fetch_realtime_data():
    # Replace this with code to fetch real-time GPS data from your device
    latitude = 40.7128  # Replace with the actual latitude value
    longitude = -74.0060  # Replace with the actual longitude value
    speed = 60.5  # Replace with the actual speed value

    # Create a dictionary with the GPS data
    data = {
        f"ambulance_id": {ambulance _id},
        "location": f"Latitude: {latitude}, Longitude: {longitude}",
        "speed": f"{speed} mph",
        # Add more data fields as needed
    }

    return data

# Continuously send real-time data
def send_realtime_data():
    while True:
        # Fetch real-time GPS data
        data = fetch_realtime_data()

        # Send the data to the traffic signal network via HTTP POST
        status_code = send_data(data)

        if status_code is not None:
            if status_code == 200:
                print("Data sent successfully to the traffic signal network.")
            else:
                print(f"Failed to send data. Status code: {status_code}")

        # Adjust the delay as needed to control the data transmission frequency
        time.sleep(5)  # Example: Send data every 5 seconds

if _name_ == "_main_":
    send_realtime_data()

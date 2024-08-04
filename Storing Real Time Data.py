import requests
import json
import time

# Define the URL of your EC2 instance or endpoint where data will be received
url = 'http://your-ec2-instance-ip:port/endpoint'  # Replace with your EC2 instance IP and port

# Function to send data to the EC2 instance
def send_data(data):
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request Error: {e}")
        return None

# Function to fetch real-time GPS data (replace with your actual data source)
def fetch_gps_data():
    # Replace this with code to fetch real-time GPS data from your device
    latitude = 40.7128  # Replace with the actual latitude value
    longitude = -74.0060  # Replace with the actual longitude value
    speed = 60.5  # Replace with the actual speed value

    # Create a dictionary with the GPS data
    data = {
        'latitude': latitude,
        'longitude': longitude,
        'speed': speed,
        # Add more data fields as needed
    }

    return data

# Continuously send real-time data
def send_realtime_data():
    while True:
        # Fetch real-time GPS data
        gps_data = fetch_gps_data()

        # Send the data to the EC2 instance via HTTP POST
        status_code = send_data(gps_data)

        if status_code is not None:
            if status_code == 200:
                print('Data sent successfully.')
            else:
                print(f'Failed to send data. Status code: {status_code}')

        # Adjust the delay as needed to control the data transmission frequency
        time.sleep(5)  # Example: Send data every 5 seconds

if _name_ == '__main__':
    send_realtime_data()

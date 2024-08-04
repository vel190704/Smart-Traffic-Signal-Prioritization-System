import pandas as pd
import math
# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('your_ambulance_data.csv')

# Assuming your CSV file has columns 'ambulance_lat', 'ambulance_lon', 'dest_lat', 'dest_lon', and 'speed'
# Adjust column names accordingly
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in km
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

total_distances = []  # To store the total distances
average_times = []    # To store the average times

for index, row in df.iterrows():
    ambulance_location = (row['ambulance_lat'], row['ambulance_lon'])
    destination_location = (row['dest_lat'], row['dest_lon'])
    speed = row['speed']  # Speed should be in km/h

    # Calculate the distance between ambulance and destination
    distance = haversine(*ambulance_location, *destination_location)

    # Calculate the time required to reach the destination
    time_required = distance / speed

    total_distances.append(distance)
    average_times.append(time_required)

# Add the calculated values to the DataFrame
df['total_distance'] = total_distances
df['average_time'] = average_times

# You can now access the DataFrame to see the results, or save it to a new CSV file
print(df)


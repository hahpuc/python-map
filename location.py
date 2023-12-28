import math

# Given coordinates
original_latitude = 10.794411
original_longitude = 106.707550

# Convert to radians
original_latitude_rad = math.radians(original_latitude)
original_longitude_rad = math.radians(original_longitude)

# Approximate length of one degree of latitude in meters
one_degree_latitude_length = 111000

# Calculate change in latitude (in degrees)
change_in_latitude_deg = 100 / one_degree_latitude_length

# Calculate new latitude
new_latitude_rad = original_latitude_rad + math.radians(change_in_latitude_deg)
new_latitude = math.degrees(new_latitude_rad)

# Approximate length of one degree of longitude at the given latitude in meters
one_degree_longitude_length = one_degree_latitude_length * math.cos(original_latitude_rad)

# Calculate change in longitude (in degrees)
change_in_longitude_deg = 100 / one_degree_longitude_length

# Calculate new longitude
new_longitude_rad = original_longitude_rad + math.radians(change_in_longitude_deg)
new_longitude = math.degrees(new_longitude_rad)

# Display the new coordinates
print("Original Coordinates:", original_latitude, original_longitude)
print("New Coordinates:", new_latitude, new_longitude)

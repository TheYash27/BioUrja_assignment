import csv

# Read the input data file
with open("https://s3.amazonaws.com/coderbyteprojectattachments/biourja-efzrr-y7i38ed9-input.csv", "r") as f:
    reader = csv.reader(f)
    wind_farm_data = []
    for row in reader:
        wind_farm_data.append(row)

# Get the individual wind farm level power output forecast
individual_wind_farm_forecast = {}
for row in wind_farm_data:
    wind_farm_name = row[0]
    individual_wind_farm_forecast[wind_farm_name] = float(row[1]) if row[1].isnumeric() else None

# Get the zonal level power output forecast
zonal_level_forecast = {}
for row in wind_farm_data:
    wind_farm_name = row[0]
    zone = row[2]
    if zone not in zonal_level_forecast:
        zonal_level_forecast[zone] = 0.0
    if individual_wind_farm_forecast[wind_farm_name] is not None:
        zonal_level_forecast[zone] += individual_wind_farm_forecast[wind_farm_name]

# Get the state level power output forecast
try:
    state_level_forecast = float(wind_farm_data[0][3])
except IndexError:
    state_level_forecast = None

# Calculate the re-dispatched wind farm levels
re_dispatched_wind_farm_levels = {}
for wind_farm_name, individual_forecast in individual_wind_farm_forecast.items():
    if individual_forecast is None:
        continue

    # Check if the wind farm name is a valid integer
    if wind_farm_name.isnumeric():
        # Get the wind farm capacity
        wind_farm_capacity = float(wind_farm_data[int(wind_farm_name)][4])

        # Calculate the weight for the wind farm
        wind_farm_weight = individual_forecast / wind_farm_capacity

        # Calculate the re-dispatched wind farm level
        re_dispatched_wind_farm_level = individual_forecast * (state_level_forecast / sum(zonal_level_forecast.values())) * wind_farm_weight

        # Ensure that the re-dispatched wind farm level does not exceed the wind farm capacity
        re_dispatched_wind_farm_level = min(re_dispatched_wind_farm_level, wind_farm_capacity)

        re_dispatched_wind_farm_levels[wind_farm_name] = re_dispatched_wind_farm_level

# Write the re-dispatched wind farm levels to a file
with open("redispatched_wind_farm_levels.csv", "w") as f:
    writer = csv.writer(f)
    for wind_farm_name, re_dispatched_wind_farm_level in re_dispatched_wind_farm_levels.items():
        writer.writerow([wind_farm_name, re_dispatched_wind_farm_level])

# Print the re-dispatched wind farm levels to the console
print("Re-dispatched wind farm levels:")
for wind_farm_name, re_dispatched_wind_farm_level in re_dispatched_wind_farm_levels.items():
    print(f"{wind_farm_name}: {re_dispatched_wind_farm_level:.2f}")

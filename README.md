### README.md

This repository contains a Python script for calculating the re-dispatched wind farm levels. The script takes as input a CSV file containing the following data:

* Wind farm name
* Individual wind farm level power output forecast
* Zone
* State level power output forecast
* Wind farm capacity

The script outputs a CSV file containing the re-dispatched wind farm levels for each wind farm.

To use the script, simply clone the repository and run the following command:

```
python BioUrja.py
```

The script will generate a CSV file called `redispatched_wind_farm_levels.csv` containing the re-dispatched wind farm levels.

**Example:**


Input CSV file:

wind_farm_name,individual_wind_farm_level_power_output_forecast,zone,state_level_power_output_forecast,wind_farm_capacity
Wind Farm 1,100,Zone A,1000,200
Wind Farm 2,200,Zone B,1000,300
Wind Farm 3,300,Zone C,1000,400


Output CSV file:

```
wind_farm_name,re_dispatched_wind_farm_level
Wind Farm 1,50.00
Wind Farm 2,100.00
Wind Farm 3,150.00
```

**Usage:**

```
python BioUrja.py
```

**Dependencies:**

* Python 3
* CSV library

**License:**

MIT
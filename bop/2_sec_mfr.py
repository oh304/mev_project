# 2_sec_mfr.py

import math
import config

# Read primary mass flow rate from file
with open("primary_mass_flow_rate.txt", "r") as f:
    primary_mass_flow_rate = float(f.read())

# Extract configuration parameters
hx_power = config.config["total_power"] / config.config["num_HX"]
htc = config.config["htc"]
delta_T = config.config["delta_T_secondary"]
rod_thickness = config.config["rod_thickness"]
rod_height = config.config["rod_height"]
helium_pressure = config.config["helium_pressure"]
operating_temp = config.config["operating_temp"]
R_helium = config.config["R_helium"]
Cp_helium = config.config["Cp_helium"]

# Density of helium at given pressure and temperature
rho_helium = helium_pressure / (R_helium * operating_temp)

# Heat transfer area required
Q_per_HX = hx_power
A_required = Q_per_HX / (htc * delta_T)

# Assume the radius of the rods and calculate the number of rods needed
rod_radius = 0.01  # Rod radius in meters
rod_circumference = 2 * math.pi * rod_radius
rod_surface_area = rod_circumference * rod_height  # Surface area per rod in m^2

num_rods = math.ceil(A_required / rod_surface_area)  # Number of rods required per heat exchanger

# Calculate the flow area for helium
flow_area_per_rod = math.pi * (rod_radius**2 - (rod_radius - rod_thickness)**2)
total_flow_area = flow_area_per_rod * num_rods

# Calculate mass flow rate of helium
mass_flow_rate_helium = Q_per_HX / (Cp_helium * delta_T)

# Output the results
print(f"Power per heat exchanger: {hx_power/10**6:.2f} MW")
print(f"Required heat transfer area: {A_required:.2f} m^2")
print(f"Number of rods required per heat exchanger: {num_rods}")
print(f"Surface area of each rod: {rod_surface_area:.4f} m^2")
print(f"Radius of each rod: {rod_radius*1000:.2f} mm")
print(f"Total flow area for helium: {total_flow_area:.4f} m^2")
print(f"Density of helium at {helium_pressure:.1e} Pa and {operating_temp} K: {rho_helium:.4f} kg/m^3")
print(f"Mass flow rate of helium: {mass_flow_rate_helium:.2f} kg/s")
print(f"Operating temperature: {operating_temp} K")

# Save output to a file
with open("secondary_mass_flow_rate.txt", "w") as f:
    f.write(f"{mass_flow_rate_helium:.2f}")

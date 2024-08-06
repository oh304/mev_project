# 3_turbine_power.py

import config

# Read secondary mass flow rate from file
with open("secondary_mass_flow_rate.txt", "r") as f:
    secondary_mass_flow_rate = float(f.read())

# Extract configuration parameters
delta_h = config.config["delta_h"]

# Calculate turbine power
turbine_power = secondary_mass_flow_rate * delta_h

# Print the result
print(f"Singular turbine power is approximately {turbine_power/10**6:.2f} MW")

# Save output to a file
with open("turbine_power.txt", "w") as f:
    f.write(f"{turbine_power:.2f}")

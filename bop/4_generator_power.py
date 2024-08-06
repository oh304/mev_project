# 4_generator_power.py

import config

# Read turbine power from file
with open("turbine_power.txt", "r") as f:
    turbine_power = float(f.read())

# Extract configuration parameters
system_efficiency = config.config["system_efficiency"]

# Calculate generator power
generator_power = turbine_power * system_efficiency

# Print the result
print(f"Total generator power (for both) is approximately {generator_power*2/10**6:.2f} MW")

# Save output to a file
with open("generator_power.txt", "w") as f:
    f.write(f"{generator_power:.2f}")

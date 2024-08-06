# 1_prim_mfr.py

import config

# Calculate the primary mass flow rate
delta_P = config.config["total_power"]
delta_T = config.config["delta_T_primary"]
Cp_sodium = config.config["Cp_sodium"]
mass_flow_rate_primary = delta_P / (Cp_sodium * delta_T)

# Print the result
print(f"The primary mass flow rate is approximately {mass_flow_rate_primary:.2f} kg/s")

# Save output to a file
with open("primary_mass_flow_rate.txt", "w") as f:
    f.write(f"{mass_flow_rate_primary:.2f}")

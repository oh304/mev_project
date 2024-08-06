# run_all.py

import subprocess

# Run the script to calculate reactor properties
subprocess.run(["python", "calculate_reactor_properties.py"])

# Run the primary mass flow rate script
subprocess.run(["python", "prim_mfr.py"])

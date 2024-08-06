# run_all.py

import subprocess

# Run the script to calculate reactor properties and write them to a text file
subprocess.run(["python", "calculate_reactor_properties.py"])

# Run the script to update the config file with the new values
subprocess.run(["python", "update_config.py"])

# Run the primary mass flow rate script
subprocess.run(["python", "prim_mfr.py"])
# run_all.py

import subprocess

# Run primary mass flow rate script
subprocess.run(["python", "1_prim_mfr.py"])

# Run secondary mass flow rate script
subprocess.run(["python", "2_sec_mfr.py"])

# Run turbine power calculation script
subprocess.run(["python", "3_turbine_power.py"])

# Run generator power calculation script
subprocess.run(["python", "4_generator_power.py"])

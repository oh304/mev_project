# prim_mfr.py

import math
import config
from calculate_reactor_properties import calculate_reactor_properties

# Retrieve reactor properties
props = calculate_reactor_properties()

# Constants
density_sodium = config.density_sodium
g = config.g
mass_reactor = config.mass_haleu
C_d = config.C_d
initial_area = config.initial_area
additional_area = config.additional_area
effective_volume_cylinder = props["effective_volume_cylinder"]

# Calculate the required buoyant force for the reactor to float
required_buoyant_force = mass_reactor * g

# Lists to store mass flow rates and corresponding total upward forces
mass_flow_rates = list(range(3400, 3550, 10))
total_upward_forces = []

print("\nMass Flow Rate (kg/s) | Buoyant Force (N) | Drag Force (N) | Total Upward Force (N) | Additional Buoyant Force Needed (N)")
print("-" * 110)

for mass_flow_rate in mass_flow_rates:
    # Calculate the velocity at the initial area
    velocity = mass_flow_rate / (density_sodium * initial_area)
    
    # Calculate the drag force
    drag_force = 0.5 * density_sodium * velocity**2 * C_d * additional_area
    
    # Calculate the buoyant force acting on the reactor
    buoyant_force = effective_volume_cylinder * density_sodium * g
    
    # Calculate the total upward force
    total_upward_force = buoyant_force + drag_force
    
    # Calculate the additional buoyant force needed
    additional_buoyant_force = required_buoyant_force - total_upward_force
    
    # Print the results
    print(f"{mass_flow_rate:<20} | {buoyant_force:<15.2f} | {drag_force:<13.2f} | {total_upward_force:<20.2f} | {additional_buoyant_force:<25.2f}")

    # Store the total upward force for plotting if needed later
    total_upward_forces.append(total_upward_force)

# Optionally, you can save the results to a file
with open('buoyancy_results.txt', 'w') as file:
    file.write("Mass Flow Rate (kg/s) | Buoyant Force (N) | Drag Force (N) | Total Upward Force (N) | Additional Buoyant Force Needed (N)\n")
    file.write("-" * 110 + "\n")
    for mass_flow_rate, total_upward_force in zip(mass_flow_rates, total_upward_forces):
        # Calculate the velocity at the initial area
        velocity = mass_flow_rate / (density_sodium * initial_area)
        
        # Calculate the drag force
        drag_force = 0.5 * density_sodium * velocity**2 * C_d * additional_area
        
        # Calculate the buoyant force acting on the reactor
        buoyant_force = effective_volume_cylinder * density_sodium * g
        
        # Calculate the total upward force
        total_upward_force = buoyant_force + drag_force
        
        # Calculate the additional buoyant force needed
        additional_buoyant_force = required_buoyant_force - total_upward_force
        
        # Write the results to the file
        file.write(f"{mass_flow_rate:<20} | {buoyant_force:<15.2f} | {drag_force:<13.2f} | {total_upward_force:<20.2f} | {additional_buoyant_force:<25.2f}\n")

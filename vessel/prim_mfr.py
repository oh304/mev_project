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
effective_volume_cylinder = props["effective_volume_cylinder"]
total_effective_area = props["total_effective_area"]
area_cylinder = props["area_cylinder"]
volume_buoyant_float = props["volume_buoyant_float"]

def calculate_and_print_results(mass_flow_rate, additional_areas):
    # Calculate the required buoyant force for the reactor to float
    required_buoyant_force = mass_reactor * g

    print(f"\nResults for Mass Flow Rate: {mass_flow_rate} kg/s")
    print("Mass Flow Rate (kg/s) | Total Area (m^2) | Velocity (m/s) | Buoyant Force (N) | Drag Force (N) | Total Upward Force (N) | Additional Buoyant Force Needed (N)")
    print("-" * 150)

    for additional_area in additional_areas:
        total_area = initial_area + additional_area
        
        # Calculate the velocity at the total area
        velocity = mass_flow_rate / (density_sodium * total_area)
        
        # Calculate the drag force
        drag_force = 0.5 * density_sodium * velocity**2 * C_d * total_area
        
        # Calculate the buoyant force acting on the reactor
        buoyant_force_cylinder = effective_volume_cylinder * density_sodium * g
        buoyant_force_float = volume_buoyant_float * density_sodium * g
        total_buoyant_force = buoyant_force_cylinder + buoyant_force_float
        
        # Calculate the total upward force
        total_upward_force = total_buoyant_force + drag_force
        
        # Calculate the additional buoyant force needed
        additional_buoyant_force = required_buoyant_force - total_upward_force
        
        # Print the results
        print(f"{mass_flow_rate:<20} | {total_area:<15.2f} | {velocity:<15.2f} | {total_buoyant_force:<15.2f} | {drag_force:<15.2f} | {total_upward_force:<20.2f} | {additional_buoyant_force:<25.2f}")

    # Optionally, you can save the results to a file
    with open('buoyancy_results.txt', 'a') as file:
        file.write(f"\nResults for Mass Flow Rate: {mass_flow_rate} kg/s\n")
        file.write("Mass Flow Rate (kg/s) | Total Area (m^2) | Velocity (m/s) | Buoyant Force (N) | Drag Force (N) | Total Upward Force (N) | Additional Buoyant Force Needed (N)\n")
        file.write("-" * 150 + "\n")
        for additional_area in additional_areas:
            total_area = initial_area + additional_area
            
            # Calculate the velocity at the total area
            velocity = mass_flow_rate / (density_sodium * total_area)
            
            # Calculate the drag force
            drag_force = 0.5 * density_sodium * velocity**2 * C_d * total_area
            
            # Calculate the buoyant force acting on the reactor
            buoyant_force_cylinder = effective_volume_cylinder * density_sodium * g
            buoyant_force_float = volume_buoyant_float * density_sodium * g
            total_buoyant_force = buoyant_force_cylinder + buoyant_force_float
            
            # Calculate the total upward force
            total_upward_force = total_buoyant_force + drag_force
            
            # Calculate the additional buoyant force needed
            additional_buoyant_force = required_buoyant_force - total_upward_force
            
            # Write the results to the file
            file.write(f"{mass_flow_rate:<20} | {total_area:<15.2f} | {velocity:<15.2f} | {total_buoyant_force:<15.2f} | {drag_force:<15.2f} | {total_upward_force:<20.2f} | {additional_buoyant_force:<25.2f}\n")

# Calculate results for each set of mass flow rates and additional areas

calculate_and_print_results(200, [area for area, _ in config.additional_areas_and_mfr_200])
calculate_and_print_results(400, [area for area, _ in config.additional_areas_and_mfr_400])
calculate_and_print_results(600, [area for area, _ in config.additional_areas_and_mfr_600])
calculate_and_print_results(800, [area for area, _ in config.additional_areas_and_mfr_800])
calculate_and_print_results(1000, [area for area, _ in config.additional_areas_and_mfr_1000])

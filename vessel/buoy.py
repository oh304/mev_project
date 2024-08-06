import math

# Constants
density_sodium = 927  # kg/m^3
g = 9.81  # m/s^2
mass_reactor = 5500  # kg
density_haleu = 18700  # kg/m^3
height_cylinder = 2  # m
diameter_channel = 0.05  # m
number_of_channels = 40
C_d = 1.28  # drag coefficient for a flat plate (approximate)
initial_area = 0.5  # m^2
additional_area = 1.5  # m^2 (additional area for drag)
volume_solid = 0.294118  # m^3 (initially calculated)

# Volume of one hollow channel
volume_channel = math.pi * (diameter_channel / 2)**2 * height_cylinder

# Total volume of all hollow channels
volume_channels_total = number_of_channels * volume_channel

# Effective volume of the cylinder (including channels)
volume_eff = volume_solid + volume_channels_total

# Effective density of the cylinder
rho_eff = mass_reactor / volume_eff

# Calculate the required buoyant force for the reactor to float
required_buoyant_force = mass_reactor * g

# Lists to store mass flow rates and corresponding total upward forces
mass_flow_rates = list(range(3000, 4001, 100))
total_upward_forces = []

print("Mass Flow Rate (kg/s) | Buoyant Force (N) | Drag Force (N) | Total Upward Force (N) | Additional Buoyant Force Needed (N)")
print("-" * 100)

for mass_flow_rate in mass_flow_rates:
    # Calculate the velocity at the initial area
    velocity = mass_flow_rate / (density_sodium * initial_area)
    
    # Calculate the drag force
    drag_force = 0.5 * density_sodium * velocity**2 * C_d * additional_area
    
    # Calculate the buoyant force acting on the reactor
    buoyant_force = volume_eff * density_sodium * g
    
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
    file.write("-" * 100 + "\n")
    for mass_flow_rate, total_upward_force in zip(mass_flow_rates, total_upward_forces):
        # Calculate the velocity at the initial area
        velocity = mass_flow_rate / (density_sodium * initial_area)
        
        # Calculate the drag force
        drag_force = 0.5 * density_sodium * velocity**2 * C_d * additional_area
        
        # Calculate the buoyant force acting on the reactor
        buoyant_force = volume_eff * density_sodium * g
        
        # Calculate the total upward force
        total_upward_force = buoyant_force + drag_force
        
        # Calculate the additional buoyant force needed
        additional_buoyant_force = required_buoyant_force - total_upward_force
        
        # Write the results to the file
        file.write(f"{mass_flow_rate:<20} | {buoyant_force:<15.2f} | {drag_force:<13.2f} | {total_upward_force:<20.2f} | {additional_buoyant_force:<25.2f}\n")

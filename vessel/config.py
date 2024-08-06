# config.py

# Given values
mass_haleu = 5500  # kg
density_haleu = 18700  # kg/m^3

# Initial values for height and diameter (these will be updated by the update_config.py script)
height_cylinder = 0.440567  # m (calculated value)
diameter_cylinder = 1.0  # m (calculated value)

diameter_channel = 0.05  # m
number_of_empty_rods = 40  # Number of empty space rods
number_of_sodium_flow_rods = 20  # Number of rods where sodium flows through
density_sodium = 927  # kg/m^3
g = 9.81  # m/s^2
C_d = 1.28  # drag coefficient for a flat plate (approximate)
initial_area = 0.0000001  # m^2

# Define additional areas and their corresponding mass flow rates
additional_areas_and_mfr = [
    (0, 10000),    # (additional area, mfr) pair
    (0.1, 9000),
    (0.2, 8000),
    (0.3, 7000),
    (0.4, 6000),
    (0.5, 5000),
    (0.6, 4000),
    (0.7, 3500),
    (0.8, 3200),
    (0.9, 3100),
    (1.0, 3000),
    (1.1, 2900),
    (1.2, 2800),
    (1.3, 2700),
    (1.4, 2600),
    (1.5, 2500)
]

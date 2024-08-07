# config.py

# Given values
mass_haleu = 5500  # kg
density_haleu = 18700  # kg/m^3

# Initial values for height and diameter (these will be updated by the update_config.py script)
height_cylinder = 0.416091  # m (calculated value)
diameter_cylinder = 1.0  # m (calculated value)
height_float = 4  # m

diameter_channel = 0.05  # m
number_of_empty_rods = 20  # Number of empty space rods
number_of_sodium_flow_rods = 20  # Number of rods where sodium flows through
density_sodium = 927  # kg/m^3
g = 9.81  # m/s^2
C_d = 1.28  # drag coefficient for a flat plate (approximate)
initial_area = 0.8  # m^2

# Define additional areas and their corresponding mass flow rates for each scenario
additional_areas_and_mfr_5000 = [
    (0, 5000),
    (0.04, 5000),
    (0.08, 5000),
    (0.12, 5000),
    (0.16, 5000),
    (0.20, 5000)
]

additional_areas_and_mfr_5200 = [
    (0, 5200),
    (0.04, 5200),
    (0.08, 5200),
    (0.12, 5200),
    (0.16, 5200),
    (0.20, 5200)
]

additional_areas_and_mfr_5400 = [
    (0, 5400),
    (0.04, 5400),
    (0.08, 5400),
    (0.12, 5400),
    (0.16, 5400),
    (0.20, 5400)
]

additional_areas_and_mfr_5600 = [
    (0, 5600),
    (0.04, 5600),
    (0.08, 5600),
    (0.12, 5600),
    (0.16, 5600),
    (0.20, 5600)
]

additional_areas_and_mfr_5800 = [
    (0, 5800),
    (0.04, 5800),
    (0.08, 5800),
    (0.12, 5800),
    (0.16, 5800),
    (0.20, 5800)
]

# config.py

# Given values
mass_haleu = 5500  # kg
density_haleu = 18700  # kg/m^3

# Initial values for height and diameter (these will be updated by the update_config.py script)
height_cylinder = 0.419588  # m (calculated value)
diameter_cylinder = 1.0  # m (calculated value)

diameter_channel = 0.05  # m

number_of_sodium_flow_rods = 20  # Number of rods where sodium flows through
density_sodium = 10007   # kg/m^3
g = 9.81  # m/s^2
C_d = 1.28  # drag coefficient for a flat plate (approximate)
initial_area = 0.8  # m^2

# number_of_empty_rods = 20  # Number of empty space rods
# height_float = 4  # m

number_of_empty_rods = 23  # Number of empty space rods
height_float = 0.28  # m

additional_areas_and_mfr_200 = [
    (0, 200),
    (0.04, 200),
    (0.08, 200),
    (0.12, 200),
    (0.16, 200),
    (0.20, 200)
]

additional_areas_and_mfr_400 = [
    (0, 400),
    (0.04, 400),
    (0.08, 400),
    (0.12, 400),
    (0.16, 400),
    (0.20, 400)
]

additional_areas_and_mfr_600 = [
    (0, 600),
    (0.04, 600),
    (0.08, 600),
    (0.12, 600),
    (0.16, 600),
    (0.20, 600)
]

additional_areas_and_mfr_800 = [
    (0, 800),
    (0.04, 800),
    (0.08, 800),
    (0.12, 800),
    (0.16, 800),
    (0.20, 800)
]

additional_areas_and_mfr_1000 = [
    (0, 1000),
    (0.04, 1000),
    (0.08, 1000),
    (0.12, 1000),
    (0.16, 1000),
    (0.20, 1000)
]

import math

# Given values
mass_haleu = 5500  # kg
density_haleu = 18700  # kg/m^3
height_cylinder = 2  # m
diameter_channel = 0.05  # m
number_of_channels = 40

# Calculate the volume of the HALEU (mass / density)
volume_haleu = mass_haleu / density_haleu

# Volume of one hollow channel
volume_channel = math.pi * (diameter_channel / 2)**2 * height_cylinder

# Total volume of all hollow channels
volume_channels_total = number_of_channels * volume_channel

# Effective volume of the cylinder (excluding channels)
effective_volume_cylinder = volume_haleu + volume_channels_total

# Calculate the radius of the cylinder (volume = pi * r^2 * h)
radius_cylinder = (effective_volume_cylinder / (math.pi * height_cylinder)) ** 0.5

print(f"Volume of the HALEU cylinder: {volume_haleu:.6f} m^3")
print(f"Total volume of hollow channels: {volume_channels_total:.6f} m^3")
print(f"Effective volume of the cylinder: {effective_volume_cylinder:.6f} m^3")
print(f"Radius of the cylinder: {radius_cylinder:.6f} m")

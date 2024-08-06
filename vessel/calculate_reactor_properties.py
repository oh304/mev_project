# calculate_reactor_properties.py

import math
import config

def calculate_reactor_properties():
    # Calculate the volume of the HALEU (mass / density)
    volume_haleu = config.mass_haleu / config.density_haleu

    # Volume of one empty space rod
    volume_empty_rod = math.pi * (config.diameter_channel / 2)**2 * config.height_cylinder

    # Total volume of all empty space rods
    volume_empty_rods_total = config.number_of_empty_rods * volume_empty_rod

    # Volume of one sodium flow rod
    volume_sodium_rod = math.pi * (config.diameter_channel / 2)**2 * config.height_cylinder

    # Total volume of all sodium flow rods
    volume_sodium_rods_total = config.number_of_sodium_flow_rods * volume_sodium_rod

    # Effective volume of the cylinder (including all rods)
    effective_volume_cylinder = volume_haleu + volume_empty_rods_total + volume_sodium_rods_total

    # Calculate the radius of the cylinder (volume = pi * r^2 * h)
    radius_cylinder = config.diameter_cylinder / 2

    # Calculate the height of the cylinder (volume = pi * r^2 * h)
    height_cylinder = effective_volume_cylinder / (math.pi * radius_cylinder**2)

    # Calculate the cross-sectional area of the cylinder
    area_cylinder = math.pi * radius_cylinder**2

    # Total cross-sectional area of all sodium flow channels
    area_sodium_channels = config.number_of_sodium_flow_rods * math.pi * (config.diameter_channel / 2)**2

    # Total effective area for sodium flow
    total_effective_area = area_cylinder + area_sodium_channels

    properties = {
        "volume_haleu": volume_haleu,
        "volume_empty_rods_total": volume_empty_rods_total,
        "volume_sodium_rods_total": volume_sodium_rods_total,
        "effective_volume_cylinder": effective_volume_cylinder,
        "radius_cylinder": radius_cylinder,
        "height_cylinder": height_cylinder,
        "total_effective_area": total_effective_area,
        "area_cylinder": area_cylinder
    }

    # Write properties to a text file
    with open('calculated_properties.txt', 'w') as f:
        for key, value in properties.items():
            f.write(f"{key}={value:.6f}\n")

    return properties

if __name__ == "__main__":
    props = calculate_reactor_properties()
    for key, value in props.items():
        print(f"{key}: {value:.6f}")

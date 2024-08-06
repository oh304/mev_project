# calculate_reactor_properties.py

import math
import config

def calculate_reactor_properties():
    # Calculate the volume of the HALEU (mass / density)
    volume_haleu = config.mass_haleu / config.density_haleu

    # Volume of one hollow channel
    volume_channel = math.pi * (config.diameter_channel / 2)**2 * config.height_cylinder

    # Total volume of all hollow channels
    volume_channels_total = config.number_of_channels * volume_channel

    # Effective volume of the cylinder (including channels)
    effective_volume_cylinder = volume_haleu + volume_channels_total

    # Calculate the radius of the cylinder (volume = pi * r^2 * h)
    radius_cylinder = (effective_volume_cylinder / (math.pi * config.height_cylinder)) ** 0.5

    properties = {
        "volume_haleu": volume_haleu,
        "volume_channels_total": volume_channels_total,
        "effective_volume_cylinder": effective_volume_cylinder,
        "radius_cylinder": radius_cylinder
    }

    return properties

if __name__ == "__main__":
    props = calculate_reactor_properties()
    for key, value in props.items():
        print(f"{key}: {value:.6f}")

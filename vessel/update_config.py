# update_config.py

def update_config_file():
    # Read calculated properties from the text file
    properties = {}
    with open('calculated_properties.txt', 'r') as f:
        for line in f:
            key, value = line.strip().split('=')
            properties[key] = value

    # Read the original config file
    with open('config.py', 'r') as f:
        lines = f.readlines()

    # Update the config file with the new values
    with open('config.py', 'w') as f:
        for line in lines:
            if line.startswith('height_cylinder'):
                f.write(f"height_cylinder = {properties['height_cylinder']}  # m (calculated value)\n")
            elif line.startswith('diameter_cylinder'):
                f.write(f"diameter_cylinder = {2 * float(properties['radius_cylinder'])}  # m (calculated value)\n")
            else:
                f.write(line)

if __name__ == "__main__":
    update_config_file()

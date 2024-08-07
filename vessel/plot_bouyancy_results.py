import matplotlib.pyplot as plt
import pandas as pd

# Function to read results from file and create a DataFrame
def read_results(file_path):
    data = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Mass Flow Rate") or line.startswith("-") or "Results for Mass Flow Rate:" in line:
                continue
            if line.strip():
                values = line.split('|')
                try:
                    mfr = float(values[0].strip())
                    total_area = float(values[1].strip())
                    velocity = float(values[2].strip())
                    additional_buoyant_force_needed = float(values[6].strip())  # Use the correct column
                    
                    if 200 <= mfr <= 1000 and -500 <= additional_buoyant_force_needed <= 500:
                        data.append({
                            'Mass Flow Rate (kg/s)': mfr,
                            'Total Area (m^2)': total_area,
                            'Velocity (m/s)': velocity,
                            'Additional Buoyant Force Needed (N)': additional_buoyant_force_needed
                        })
                except (ValueError, IndexError):
                    continue
    return pd.DataFrame(data)

# Read results from file
df = read_results('buoyancy_results.txt')

# Ensure correct filtering and sorting
df = df[df['Mass Flow Rate (kg/s)'].between(200, 1000)]
df = df[df['Additional Buoyant Force Needed (N)'].between(-65, 15)]
df = df.sort_values(by=['Mass Flow Rate (kg/s)', 'Total Area (m^2)'])

# Remove duplicate points
df = df.drop_duplicates(subset=['Mass Flow Rate (kg/s)', 'Total Area (m^2)'])

# Plot configuration
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot additional buoyant force needed vs. total area for each mass flow rate
for mfr in sorted(df['Mass Flow Rate (kg/s)'].unique()):
    df_mfr = df[df['Mass Flow Rate (kg/s)'] == mfr]
    ax1.plot(df_mfr['Total Area (m^2)'], df_mfr['Additional Buoyant Force Needed (N)'], marker='o', linestyle='-', label=f'MFR {mfr} kg/s')

# Add horizontal dashed line for 'additional buoyancy needed = 0'
ax1.axhline(0, color='gray', linestyle='--', linewidth=1, label='Additional Buoyancy Needed = 0')

# Label for left y-axis
ax1.set_ylabel('Additional Buoyant Force Required to Float (N)')
ax1.set_xlabel('Total Area (m^2)')

# Create a second x-axis for velocity
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())
velocity_labels = df.groupby('Total Area (m^2)')['Velocity (m/s)'].mean().round(2)
ax2.set_xticks(velocity_labels.index)
ax2.set_xticklabels(velocity_labels, rotation=45)
ax2.set_xlabel('Velocity (m/s)')

# Add grid, legend, and title
ax1.grid(True)
ax1.legend()
plt.title('Additional Buoyant Force vs. Total Area and Velocity for Various Mass Flow Rates')

# Save the plot
plt.savefig('buoyancy_plot.png')

# Show the plot
plt.show()

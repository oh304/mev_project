# config.py

# Constants and shared parameters
config = {
    "total_power": 25 * 10**6,  # Total power in W (25 MW)
    "num_HX": 2,  # Number of heat exchangers
    "htc": 4000,  # Heat transfer coefficient in W/(m^2.K)
    "delta_T_primary": 6,  # Temperature difference for primary coolant in K
    "Cp_sodium": 1300,  # Specific heat capacity of liquid sodium in J/(kg.K)
    "delta_T_secondary": 100,  # Temperature difference for secondary coolant in K - updated
    "rod_thickness": 1e-3,  # Rod thickness in meters
    "rod_height": 5,  # Rod height in meters
    "helium_pressure": 1e7,  # Helium pressure in Pa
    "operating_temp": 500,  # Operating temperature in K
    "R_helium": 2077,  # Ideal gas constant for helium in J/(kg.K)
    "Cp_helium": 5193,  # Specific heat capacity of helium in J/(kg.K)
    "delta_h": 500000,  # Enthalpy drop in J/kg (adjusted to a more typical value)
    "system_efficiency": 0.40  # System efficiency
}

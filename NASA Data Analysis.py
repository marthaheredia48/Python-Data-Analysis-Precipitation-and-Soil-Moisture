import xarray as xr
import matplotlib.pyplot as plt

# Open your dataset from the Downloads folder
dataset = xr.open_dataset('/Users/marthaandradeaparicio/Downloads/GLDAS_NOAH025_M.A202404.021.nc4.SUB.nc4')

# Extract the precipitation DataArray
precipitation_array = dataset['SoilMoi0_10cm_inst']
print("promedio: ")

print( precipitation_array.mean())
print("min ")

print( precipitation_array.min()) 

print("max: ")

print( precipitation_array.max()) 

# Extract the coordinates
lon = dataset['lon'].values  # Extracting longitude values
lat = dataset['lat'].values  # Extracting latitude values

# Check if lon and lat are defined correctly
print("Longitude values:", lon)
print("Latitude values:", lat)

# Plotting the precipitation data
plt.figure(figsize=(10, 6))
plt.imshow(precipitation_array[0], extent=[lon.min(), lon.max(), lat.min(), lat.max()], origin='lower', cmap='Greens')
plt.colorbar(label='Soil Moisture Content (kg m⁻²)')
plt.title('Soil Moisture on April, 2024')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

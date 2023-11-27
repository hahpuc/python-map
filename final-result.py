
import pygmt
import numpy as np
import xarray as xr

fig = pygmt.Figure()

# Define the grid dimensions and spacing
lon_min, lon_max, lat_min, lat_max = 102, 110, 8, 16
lon_spacing, lat_spacing = 1, 1
region = [lon_min, lon_max, lat_min, lat_max]

# Generate synthetic data (you can replace this with your own data)
lons = np.arange(lon_min, lon_max, lon_spacing)
lats = np.arange(lat_min, lat_max, lat_spacing)
lons, lats = np.meshgrid(lons, lats)
data = np.random.randint(0, 10, size=(len(lons), len(lats)))

# Create xarray.DataArray
grid_data_array = xr.DataArray(
    data, 
    coords=[lats[:, 0], lons[0, :]],
    dims=["lat", "lon"]
)

# Show the data
fig.grdimage(
    grid=grid_data_array,
    cmap="haxby",
    projection="M12c",
)
fig.grdcontour(
    interval=250,
    annotation=1000,
    grid=grid_data_array,
    limit=[-4000, -2000],
)
fig.coast(
    region=region,
    projection="M12c",
    borders="1/0.5p",
    shorelines="1/0.5p",
    water="lightblue",
    frame="ag",
    transparency=50,
)

fig.colorbar(frame=["x+lPolution", "y+lm"])

fig.show()

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

# Show arrows 
x = np.linspace(lon_min, lon_min, 12)  # x vector coordinates
y = np.linspace(lat_min + 2, lat_max - 2, 12)  # y vector coordinates
direction = np.zeros(x.shape)  # direction of vectors
length = np.linspace(0.5, 2.4, 12)  # length of vectors

# ARROW vectors (v) with red fill and pen (+g, +p), vector head at
# end (+e), and 40 degree angle (+a) with no indentation for vector head (+h)
style = "v0.2c+e+a40+gred+h0+p1p,red"
fig.plot(x=x, y=y, style=style, pen="1p,red", direction=[direction, length])

fig.text(text="ARROW", x=103, y=10, font="13p,Helvetica-Bold,red", fill="white")

fig.colorbar(frame=["x+lPolution", "y+lm"])

fig.show()

import pygmt
import numpy as np
import xarray as xr

fig = pygmt.Figure()

# HARD CODE VIETNAM REGION
region = [102, 110.1, 8, 17.8]

## SET UP lat, long variables
lat_min, lat_max = 8, 17.8
lon_min, lon_max = 102, 110.1

lat = np.arange(lat_min, lat_max, 0.2)
lon = np.arange(lon_min, lon_max, 0.2)

# Load Data File
file_data = "data.d"
with open(file_data, "r") as file:
    dataFile = [[float(num) for num in line.split()] for line in file]

data = np.array(dataFile)
# data = np.random.uniform(-5, 5, size=(len(lat), len(lon)))

grid = xr.DataArray(
    data=data,
    dims=["lat", "lon"],
    coords={
        "lon": lon,
        "lat": lat,
    },
)

## SHOW DATA Contour
fig.grdimage(
    grid=grid,
    cmap="viridis",
    projection="M12c",
)
fig.grdcontour(
    interval=250,
    grid=grid,
    limit=[-4000, -2000],
)

## Show map line
fig.coast(
    region=region,
    projection="M12c",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)

# Set color bar bottom
fig.colorbar(frame=["x+lContour DATA", "y+lm"])

fig.show()
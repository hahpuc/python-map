
import pygmt
import numpy as np
import xarray as xr

fig = pygmt.Figure()

# grid = pygmt.datasets.load_earth_relief(resolution="05m", region="VN")

region = [102, 110, 8, 24]

## SET UP DATA
lat_min, lat_max = 8, 24
lon_min, lon_max = 102, 110

# create xr.DataArray
lat = np.arange(lat_min, lat_max, 0.25)
lon = np.arange(lon_min, lon_max, 0.25)
# create random data array in shape (lat,lon)
data = np.random.uniform(-5, 5, size=(len(lat), len(lon)))

grid = xr.DataArray(
    data=data,
    dims=["lat", "lon"],
    coords={
        "lon": lon,
        "lat": lat,
    },
)

print(grid)

## SHOW DATA 
fig.grdimage(
    grid=grid,
    cmap="haxby",
    projection="M12c",
)
fig.grdcontour(
    interval=250,
    grid=grid,
    limit=[-4000, -2000],
)
fig.coast(
    region="VN",
    projection="M12c",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)

fig.colorbar(frame=["x+lelevation", "y+lm"])

fig.show()
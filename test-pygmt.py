import pygmt
import xarray as xr
import numpy as np

# setting up projection
proj = "Cyl_stere/12c"

# define region
lat_min, lat_max = -15.0, 15.0
lon_min, lon_max = 90.0, 140.0

# cut large topo file to region of interest
topo_data = "@earth_relief_10m"
topo_data_SEA = pygmt.grdcut(
    topo_data,
    region=[lon_min, lon_max, lat_min, lat_max],
)

# create xr.DataArray
lat = np.linspace(start=lat_min, stop=lat_max, num=2)
lon = np.linspace(start=lon_min, stop=lon_max, num=2)
# create random data array in shape (lat,lon)
data = np.random.randint(-5, 5, size=(2, 2))

ds = xr.DataArray(
    data=data,
    dims=["lat", "lon"],
    coords={
        "lon": lon,
        "lat": lat,
    },
)
print(ds)

fig = pygmt.Figure()

# create colorbar for xarray.DataArray
pygmt.makecpt(
    cmap="polar",
    series="-5/5/0.5",
    continuous=True,
    reverse=True,
)

# plot

fig.coast(
    region=[lon_min, lon_max, lat_min, lat_max],
    projection=proj,
    land="darkgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
)

with fig.inset(position="jBL+w3c+o0.5c/0.2c", box="+pblack"):
    # Use a plotting function to create a figure inside the inset
    fig.grdview(
        grid=topo_data_SEA,
        drapegrid=ds,  # xarray.DataArray containing values to use for colormap
        cmap=True,
        region=[lon_min, lon_max, lat_min, lat_max],
        projection=proj,
        surftype="i",
        shading=True,
        frame=True,
    )

# fig.grdview(
#     grid=topo_data_SEA,
#     drapegrid=ds,  # xarray.DataArray containing values to use for colormap
#     cmap=True,
#     region=[lon_min, lon_max, lat_min, lat_max],
#     projection=proj,
#     surftype="i",
#     shading=True,
#     frame=True,
# )


fig.show()
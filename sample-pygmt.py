import numpy as np
import pygmt

# https://forum.generic-mapping-tools.org/t/grdimage-with-two-datasets-on-top-of-each-other/1642/2

# create a plot with coast, Mercator projection (M) over the continental US
# fig = pygmt.Figure()
# fig.coast(
#     region="VN",
#     projection="M12c",
#     land="lightgray",
#     water="blue",
#     borders="1/0.5p",
#     shorelines="1/0.5p",
#     frame="a",
# )

# # build the contours underlying data with the function z = x^2 + y^2
# X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
# Z = X**2 + Y**2
# x, y, z = X.flatten(), Y.flatten(), Z.flatten()

# fig.contour(
#     region=[-10, 10, -10, 10],
#     projection="X10c/10c",
#     frame="ag",
#     pen="0.5p",
#     # pass the data as 3 1-D data columns
#     x=x,
#     y=y,
#     z=z,
#     # set the contours z values intervals to 10
#     levels=10,
#     # set the contours annotation intervals to 20
#     annotation=20,
# )
# fig.show()


# import os

# fig = pygmt.Figure()
# fig.coast(
#     region=[120, 150, 20, 50],
#     projection="M12c",
#     land="lightgray",
#     water="blue",
#     borders="1/0.5p",
#     shorelines="1/0.5p",
#     frame="a",
# )

# # place and center the GMT logo from the GMT website to the position 1/1
# # on a basemap, scaled up to be 3 cm wide and draw a rectangular border
# # around the image
# fig.image(
#     imagefile="contour.png",
# )

# # clean up the downloaded image in the current directory

# fig.show()

import pygmt
import numpy as np
import xarray as xr


# Define the grid dimensions and spacing
lon_min, lon_max, lat_min, lat_max = 120, 150, 20, 50
lon_spacing, lat_spacing = 1, 1

# Generate synthetic data (you can replace this with your own data)
lons = np.arange(lon_min, lon_max + lon_spacing, lon_spacing)
lats = np.arange(lat_min, lat_max + lat_spacing, lat_spacing)
lons, lats = np.meshgrid(lons, lats)
data = np.sin(np.radians(lons)) * np.cos(np.radians(lats))

# Create xarray.DataArray
grid_data_array = xr.DataArray(data, coords=[lats[:, 0], lons[0, :]], dims=["lat", "lon"])




# Plot figure
fig = pygmt.Figure()
fig.grdimage(
    grid=grid_data_array, cmap="viridis" ,
    frame=["a", "WSne"]
)
# fig.coast(
#     region=[120, 150, 20, 50],
#     projection="M12c",
#     land="lightgray",
#     water="white",
#     borders="1/0.5p",
#     shorelines="1/0.5p",
#     frame="a",
# )


fig.colorbar(position="JMR")
fig.show()
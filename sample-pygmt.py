import numpy as np
import pygmt

# create a plot with coast, Mercator projection (M) over the continental US
fig = pygmt.Figure()
fig.coast(
    region="VN",
    projection="M12c",
    land="lightgray",
    water="blue",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="a",
)

# build the contours underlying data with the function z = x^2 + y^2
X, Y = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
Z = X**2 + Y**2
x, y, z = X.flatten(), Y.flatten(), Z.flatten()

fig.contour(
    region=[-10, 10, -10, 10],
    projection="X10c/10c",
    frame="ag",
    pen="0.5p",
    # pass the data as 3 1-D data columns
    x=x,
    y=y,
    z=z,
    # set the contours z values intervals to 10
    levels=10,
    # set the contours annotation intervals to 20
    annotation=20,
)
fig.show()

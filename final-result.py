
import pygmt


fig = pygmt.Figure()

grid = pygmt.datasets.load_earth_relief(resolution="05m", region="VN")

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
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
    frame="ag",
    transparency=50,
)

fig.colorbar(frame=["x+lelevation", "y+lm"])

fig.show()
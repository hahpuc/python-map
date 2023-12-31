import matplotlib.pyplot as plt
import numpy as np
import pygmt

region = [102, 110, 8, 16]

# Show Map
figGMT = pygmt.Figure()
figGMT.coast(
    region= region,
    projection="M15c",
    land="lightgray",
    water="white",
    borders="1/0.5p",
    shorelines="1/0.5p",
)

# Save the PyGMT figure to a file
figGMT.savefig('map.png', transparent=True, dpi=300)

# Contour Data
xlist = np.arange(102, 110, 1)
ylist = np.arange(8, 16, 1)

dataCountour = np.random.randint(0, 10, size=(len(ylist), len(xlist)))

fig, ax = plt.subplots(1, 1)

cp = ax.contourf(xlist, ylist, dataCountour, levels=10, cmap='viridis', alpha=0.5)
fig.colorbar(cp)

ax.set_title('Filled Contours Plot')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')

# Load and display the PyGMT map within the Matplotlib plot
img = plt.imread('map.png')
ax.imshow(img, extent=region, aspect='auto', zorder=0)

# Display the Matplotlib plot
plt.show()


# #Load Contour Data Map
# grid = pygmt.datasets.load_earth_relief(resolution="05m", region="VN")

# fig.grdimage(
#     grid=grid,
#     cmap="haxby",
#     projection="M10c",
# )
# fig.grdcontour(
#     annotation=1000,
#     grid=grid,
# )

# # Load CSV data file => Show in Map
# quakes = pd.read_csv(
#     "earthquakes.csv",
#     skipinitialspace=True
# )

# quakes.head()
# pygmt.makecpt(cmap="batlow", series=[3.5, 6.5])
# fig.plot(x=quakes.longitude, y=quakes.latitude, style="c0.3c", color="yellow", cmap=True)


# # Show Color bottom bar 
# fig.colorbar(position="JBC", frame=["af", "y+lMagnitude"])


# # Show Text in Map
# fig.text(x=108, y=12, text="TP.HO CHI MINH", font="12p,Helvetica-Bold,black")

# fig.show()

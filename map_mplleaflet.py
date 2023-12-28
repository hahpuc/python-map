import matplotlib.pyplot as plt
import numpy as np
import mplleaflet

# Create a simple plot using Matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Matplotlib Plot')

# Convert the Matplotlib plot to a Leaflet web map
# mplleaflet.display()

# Alternatively, you can save the map to an HTML file

mplleaflet.display(fig=plt.gcf(), tiles='cartodb_positron', crs=mplleaflet.crs.EPSG3857, path='output_map.html')


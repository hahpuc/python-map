import numpy as np
import matplotlib.pyplot as plt



#### Contour Data 
xlist = list(range(104, 108))
ylist = list(range(8, 12))

dataCountour = np.zeros([len(ylist), len(xlist)])

# set random values for each cell of dataCountour
for i in range(0, len(ylist)):
    for j in range(0, len(xlist)):
        dataCountour[i][j] = np.random.randint(0, 40)

fig,ax=plt.subplots(1,1)


cp = ax.contourf(xlist, ylist, dataCountour, levels=10, cmap='viridis')
fig.colorbar(cp) # Add a colorbar to a plot

ax.set_title('Filled Contours Plot')
ax.set_xlabel('x (cm)')
ax.set_ylabel('y (cm)')

plt.show()

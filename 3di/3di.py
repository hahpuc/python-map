from matplotlib import pyplot as plt
from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
from threedigrid.admin.gridadmin import GridH5Admin
import os

result_path = "./"
nc = os.path.join(result_path,'aggregate_results_3di.nc')
f = os.path.join(result_path,'gridadmin.h5')

ga = GridH5Admin(f)
gr = GridH5ResultAdmin(f,nc)

plt.figure()
#plotting only your 2d open water grid
xyc = ga.nodes.subset('2d_open_water').coordinates
plt.plot(xyc[0], xyc[1], '.', label='2D open water')

plt.gcf().set_facecolor('none')
plt.axis('off')

print(plt.style.available)

# plt.savefig('3di.png')

plt.show()



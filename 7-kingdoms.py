import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import helper

strongholds = pd.read_csv("Cities.csv")

# Compute Voronoi Tesselation
vor = Voronoi(strongholds[["X","Y"]])
# Get the finite regions
regions, vertices = helper.voronoi_finite_polygons_2d(vor)

# Colourize the regions
for region in regions:
    polygon = vertices[region]
    plt.fill(*zip(*polygon), alpha=0.9)

# Annotate the strongholds
for index, row in strongholds.iterrows():
    plt.annotate(row["City"], (row["X"]+10, row["Y"]+10))

#Set the plot limits
x_min = min(strongholds["X"])-100
x_max = max(strongholds["X"])+150
y_min = min(strongholds["Y"])-100
y_max = max(strongholds["Y"])+100

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.scatter(strongholds["X"], strongholds["Y"], c="black", marker="*")
plt.show()

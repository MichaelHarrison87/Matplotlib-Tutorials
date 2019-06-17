import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")

### DATA
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

data = pd.read_csv("../data/youtube-views-2019-05-31.csv")
view_count = data["view_count"]
likes = data["likes"]
like_ratio = data["ratio"]



### PLOT

# Plot 1 - scatter plot, change color, marker, edge etc
plt.scatter(x, y, c = "blue", marker = "o", edgecolors="black", alpha = 0.5)

plt.tight_layout()
plt.show()
plt.clf()

# Plot 2 - can also specify color and size for each point individually:
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5] # can use these to pick out values from a colourmap

sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
         538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(x, y, c = colors, sizes = sizes, edgecolors="black", cmap = "Greens") # Greens colourmap

cbar = plt.colorbar() # legend for the colourmap
cbar.set_label("Rating")

plt.tight_layout()
plt.show()
plt.clf()


# Plot 3 - plot youtube views/likes data
plt.scatter(view_count, likes, c = like_ratio, cmap = "summer", 
            edgecolors="black", linewidth=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

# Data has one outlier with ~100m views, so plot on a log-scale:
plt.xscale("log")
plt.yscale("log")

plt.title("Youtube - Likes vs Views ")
plt.xlabel("Views")
plt.xlabel("Likes")

plt.tight_layout()
plt.show()
plt.clf()

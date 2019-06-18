# Plotting data that changes live

import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")


# Plot 1 - stream a series of (x,y) values and plot the series as it is generated

x_vals = []
y_vals = []
index = count() # generator for successive integers - i.e. 0, 1, 2, ...

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    
    plt.cla() # clear axis
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000) 

plt.tight_layout()
plt.show()
plt.clf()

# Plot 2 - plot data from a csv that's being updated from some other source (created by data-gen.py script)
# Need to leave data-gen.py script running to get the animation to live-update
def new_animate(i):
    data = pd.read_csv("../data/generated-data.csv")
    x = data["x_values"]
    y1 = data["total_1"]
    y2= data["total_2"]
    
    plt.cla() # clear axis
    plt.plot(x, y1, label = "Channel 1")
    plt.plot(x, y2, label = "Channel 2")

    plt.legend(loc = "upper left")
    plt.tight_layout()

ani_2 = FuncAnimation(plt.gcf(), new_animate, interval=1000) 

plt.show()
plt.clf()

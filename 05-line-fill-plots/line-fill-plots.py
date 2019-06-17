import pandas as pd
from matplotlib import pyplot as plt

### DATA
data = pd.read_csv("../data/data_by_age.csv")

ages = data["Age"]
all_devs = data["All_Devs"]
python_devs = data["Python"]
js_devs = data["JavaScript"]

overall_median = 57287

### PLOT

# Can use fill_between() to fill regions of the plot with colour
plt.plot(ages, all_devs, color = "#444444", linestyle = "--", label = "All Devs")
plt.plot(ages, python_devs, label = "Python")

plt.fill_between(ages, y1 = all_devs, y2 = python_devs, alpha = 0.25) # color the space between the two lines y1 & y2; alpha controls the fill's transparency
plt.fill_between(ages, y1 = all_devs, alpha = 0.25) # if don't specify y2, the fill goes between the line and the x-axis
plt.fill_between(ages, y1 = python_devs, y2 = overall_median, alpha = 0.25) # can specify a scalar to fill between a horizontal line

plt.legend()
plt.xlabel("Age")
plt.ylabel("Median Salary")
plt.title("Median Salary by Age")

plt.show()
plt.clf()


# Can also specify conditionals, which must be satisfied for the fill to be displayed
plt.plot(ages, all_devs, color = "#444444", linestyle = "--", label = "All Devs")
plt.plot(ages, python_devs, label = "Python")

plt.fill_between(ages, y1 = python_devs, y2 = overall_median, 
                 where = python_devs >= overall_median,
                 interpolate = True,
                 alpha = 0.25, color = "blue") 

plt.fill_between(ages, y1 = python_devs, y2 = overall_median, 
                 where = python_devs < overall_median,
                 interpolate = True,
                 alpha = 0.25, color = "red") 
plt.legend()
plt.xlabel("Age")
plt.ylabel("Median Salary")
plt.title("Median Salary by Age")

plt.show()
plt.clf()


# Can pass labels to fill_between methods to explain what's being highlighted
plt.plot(ages, all_devs, color = "#444444", linestyle = "--", label = "All Devs")
plt.plot(ages, python_devs, label = "Python")

plt.fill_between(ages, y1 = all_devs, y2 = python_devs, 
                 where = python_devs >= all_devs,
                 interpolate = True,
                 alpha = 0.25, color = "blue", label = "Python Above Average") 

plt.fill_between(ages, y1 = all_devs, y2 = python_devs, 
                 where = python_devs < all_devs,
                 interpolate = True,
                 alpha = 0.25, color = "red", label = "Python Below Average") 
plt.legend()
plt.xlabel("Age")
plt.ylabel("Median Salary")
plt.title("Median Salary by Age")

plt.show()
plt.clf()
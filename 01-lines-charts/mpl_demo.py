from matplotlib import pyplot as plt


### DATA
# From Data Snippets: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/01-Introduction/snippets.py

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# All developers
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Python developers
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Javascript developers
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


### PLOT

# Basic plot of median salaries by age
plt.figure(1)

plt.plot(ages_x, py_dev_y, color = "#5a7d9a", label = "Python") # Make line plot, change colour via hex code 
plt.plot(ages_x, js_dev_y, color = "#adad3b", label = "Javascript") # adds new line to the plot
plt.plot(ages_x, dev_y, color = "k", linestyle = "--", marker = ".", label = "All Developers") # Apply some other formatting; can also specify colour using letter code
# Note: the last data plotted will be over the top of that plotted previously

plt.title("Median Salary by Age")
plt.xlabel("Age")
plt.ylabel("Salary ($)")

plt.legend() # Adds legend, using the labels specified in plot()
plt.grid()

plt.tight_layout() # puts padding into the plot
plt.savefig("median_salary_by_age.png")
plt.show()

# Matplotlib also has built-in styles, can see which are available via:
print(plt.style.available)

# Change style and re-plot the data using this new style: 
plt.style.use("ggplot")

plt.figure(2)
plt.plot(ages_x, py_dev_y)
plt.plot(ages_x, js_dev_y)
plt.plot(ages_x, dev_y)
plt.show()




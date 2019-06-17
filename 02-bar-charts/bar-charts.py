from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter

### DATA
# From Data Snippets: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/01-Introduction/snippets.py

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Note: simply using successive plt.bar(), plt.bar() with the same x values will just stack the bars on top of each other

# To put the sets of bars next to each other, need to offset the x values:
width = 0.25 # apporx width of each bar
ages_len = len(ages_x)
x_indices = np.arange(ages_len)

# All developers
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Python developers
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# Javascript developers
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

# Read in developer survey data
with open("../data/dev_survey_data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Can use Counter from the collections module to keep running count of the languages in the data
    language_counter = Counter()
    
    for row in csv_reader:
        language_list = row["LanguagesWorkedWith"].split(";")
        language_counter.update(language_list)

# Prepare data on 15 most common languages
most_common_languages = language_counter.most_common(15) # list of (language, count) tuples e.g. [("Python", 100), ("Java", 75)]
most_common_languages = list(zip(*most_common_languages)) # unpack the above list, e.g. [("Python", "Java"), (100, 75)]

languages = list(most_common_languages[0])
counts = list(most_common_languages[1])


### PLOT

plt.bar(x_indices - width, dev_y, width =  width, label = "All")
plt.bar(x_indices, py_dev_y, width =  width, label = "Python") 
plt.bar(x_indices + width, js_dev_y, width =  width, label = "Javascript") 
plt.plot(x_indices, dev_y, color="k") # adds a line to the chart

plt.xticks(ticks=x_indices, labels=ages_x) # Relabel the x-axis

plt.title("Median Salary by Age")
plt.xlabel("Age")
plt.ylabel("Salary ($)")

plt.legend() # Adds legend, using the labels specified in plot()
plt.grid()

plt.tight_layout() # puts padding into the plot
plt.show()
plt.clf()


# Plot top 15 language counts in horizontal bar chart
languages.reverse() # Sort the list in-place, to get highest count first - as .most_common(15) results came in ascending order. Note: sort wouldn't work here
counts.reverse()

plt.barh(languages, counts)

plt.ylabel("Language")
plt.xlabel("Number of Developers")

plt.show()

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

### DATA
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

data = pd.read_csv("../data/responder_age_data.csv")
data_ids = data["Responder_id"]
data_ages = data["Age"]

### PLOT

# Plot 1 - specify number of evenly-spaced bins
plt.hist(ages, bins = 5, edgecolor = "black") # split the input into 5 evenly-spaced bins

plt.title("Number of Respondents by Age")
plt.xlabel("Age")
plt.ylabel("Number of Respondents")

plt.tight_layout()
plt.show()
plt.clf()


# Plot 2 - specify start-point of own bins
my_bins = range(10, 70, 10) # 10-60 in jumps of 10
plt.hist(ages, bins = my_bins, edgecolor = "black")

plt.title("Number of Respondents by Age")
plt.xlabel("Age")
plt.ylabel("Number of Respondents")

plt.tight_layout()
plt.show()
plt.clf()


# Plot 3 - plot dev survey data
my_bins_2 = range(10, 110, 5) # 10-100 in jumps of 5
plt.hist(data_ages, bins = my_bins_2, edgecolor = "black", log = True) # can plot log(counts) 

# Plot vertical line showing median age of all respondents:
median_age = 29
plt.axvline(median_age, color = '#fc4f30', linewidth = 2, label="Median Age")

plt.title("Number of Respondents by Age")
plt.xlabel("Age")
plt.ylabel("Number of Respondents")

plt.xticks(my_bins_2)

plt.legend()
plt.tight_layout()
plt.show()
plt.clf()
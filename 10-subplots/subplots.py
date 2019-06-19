import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("seaborn")


### DATA
data = pd.read_csv("../data/dev_salary_by_age.csv")
ages = data["Age"]
salaries_all_dev = data["All_Devs"]
salaries_python = data["Python"]
salaries_js = data["JavaScript"]


### Plot

# Figure 1 - Use figure and axes explicitly

# In Matplotlib, the plotting window is the "figure", while the individual charts in the figure are the "axes"
fig1, ax1 = plt.subplots() # by default, 1x1 grid of charts

# cf below: plt.plot()
ax1.plot(ages, salaries_all_dev, color="black", linestyle="--", label="All Devs")
ax1.plot(ages, salaries_python, label="Python")
ax1.plot(ages, salaries_js, label="JavaScript")

ax1.set_title("Developer Salary by Age")
ax1.set_xlabel("Age")
ax1.set_ylabel("Salary")

ax1.legend()


# Figure 2 - Plot All Devs separately in the same figure

# In Matplotlib, the plotting window is the "figure", while the individual charts in the figure are the "axes"
fig2, ax2 = plt.subplots(nrows=2, ncols=1, sharex=True)

print(ax2) # Note: ax is a (nested)  list of AxesSubplot objects

# 1st subplot
ax2[0].plot(ages, salaries_all_dev, color="black", linestyle="--", label="All Devs")

ax2[0].legend()
ax2[0].set_title("Developer Salary by Age")
ax2[0].set_ylabel("Salary")

# 2nd subplot
ax2[1].plot(ages, salaries_python, label="Python")
ax2[1].plot(ages, salaries_js, label="JavaScript")

ax2[1].legend()
ax2[1].set_xlabel("Age")
ax2[1].set_ylabel("Salary")


# The below will now show both Figures in separate windows
plt.tight_layout()
plt.show()
plt.clf()

# When saving, save each figure individually:
fig1.savefig("fig1.png")
fig2.savefig("fig2.png")
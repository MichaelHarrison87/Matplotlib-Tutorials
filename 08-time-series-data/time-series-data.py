import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use("seaborn")

### DATA

# Dummy Data
dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]


# Bitcoin Data
bitcoin_data = pd.read_csv("../data/bitcoin_data.csv")
price_date = bitcoin_data["Date"]
price_close = bitcoin_data["Close"]


### PLOT

# Plot 1 - dummy data
plt.plot_date(dates, y, linestyle = "solid") # plot_date default to plotting markers with no line

plt.gcf().autofmt_xdate() # get current figure, format x-axis date (e.g. rotate, prevent overlap)

# Can supply a date format string, to specify how dates should appear: (default format seems to be yyyy-mm-dd)
date_format = mpl_dates.DateFormatter("%d %b %Y") # e.g. 01 Jan 2000 

plt.gca().xaxis.set_major_formatter(date_format) # get current axis, set x-axis format

plt.tight_layout
plt.show()
plt.clf()
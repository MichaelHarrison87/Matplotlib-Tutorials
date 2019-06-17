from matplotlib import pyplot as plt

slices = [60, 40, 20, 50] # don't need to sum to 1 or 100
labels = ["A", "B", "C", "D"]
wedge_colours = ["#008fd5", "#fc4f30", "#e5ae37", "#6d904f"]

plt.pie(slices, labels = labels, wedgeprops = {"edgecolor": "black"}, colors = wedge_colours)
plt.title("Pie Chart")
plt.legend()
plt.show()
plt.clf()


# Plot Language Popularity - data from: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/03-PieCharts/snippets.txt
languages = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
counts = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]

# Package data into a dictionary
lang_count_dict = {lang:cnt for lang, cnt in zip(languages, counts)}

plt.pie(counts, labels = languages, wedgeprops = {"edgecolor": "black"})
plt.title("Language Popularity")
plt.legend()
plt.show()
plt.clf()

# Plot top 5 most popular language, emphasising python and demo'ing some other pie chart formatting features:
languages_top_5 = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
counts_top_5 = [59219, 55466, 47544, 36443, 35917]
explode_propns = [0, 0, 0, 0.1, 0] 

plt.pie(counts_top_5, 
        labels = languages_top_5, 
        wedgeprops = {"edgecolor": "black"}, 
        explode = explode_propns, # specifies how far out from the radius each slice is removed
        shadow = True, # puts a shadow under each slide, for a 3D effect
        startangle = 90, # rotates the pie chart
        autopct = "%1.1f%%") # superimposes the percentages of each slice, with a given format (1dp in %)
plt.title("Language Popularity - Top 5")
plt.show()
plt.clf()


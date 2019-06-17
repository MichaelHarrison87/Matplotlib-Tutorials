from matplotlib import pyplot as plt


### Data

# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Matplotlib/04-StackPlots/snippets.txt
# Note sum over all players in each minute is constant, 8
player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

minutes = [i+1 for i in range(9)] # 1-9


### Plot

# Stacked bar plot
plt.bar(minutes, player1)
plt.bar(minutes, player2)
plt.bar(minutes, player3)

plt.title("Number of Points by Minute, by Player")
plt.xlabel("Minute")
plt.xticks(ticks = minutes)
plt.ylabel("Points")
plt.legend()

plt.show()
plt.clf()


# Area plot - constant total
plt.stackplot(minutes, player1, player2, player3, labels = ["Player 1", "Player 2", "Player 3"])

plt.title("Number of Points by Minute, by Player")
plt.xlabel("Minute")
plt.ylabel("Points")
plt.legend(loc = "lower left")

plt.show()
plt.clf()


# Area plot - variable total
player1_alt = [1, 2, 3, 3, 4, 4, 4, 4, 5]
player2_alt = [1, 1, 1, 1, 2, 2, 2, 3, 4]
player3_alt = [1, 1, 1, 2, 2, 2, 3, 3, 3]

plt.stackplot(minutes, player1_alt, player2_alt, player3_alt, labels = ["Player 1", "Player 2", "Player 3"])

plt.title("Number of Points by Minute, by Player")
plt.xlabel("Minute")
plt.ylabel("Points")
plt.legend()

plt.show()
plt.clf()
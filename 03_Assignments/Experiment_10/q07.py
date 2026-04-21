#  Create a program to demonstrate different visual forms using Matplotlib. 

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 52]
categories = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
percentages = [15, 30, 45, 10]
pie_labels = ['Apples', 'Bananas', 'Cherries', 'Dates']

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y, marker='o', color='blue', linestyle='--')
axs[0, 0].set_title("Line Plot")
axs[0, 0].set_xlabel("X-axis")
axs[0, 0].set_ylabel("Y-axis")

axs[0, 1].bar(categories, y, color='green')
axs[0, 1].set_title("Bar Chart")

axs[1, 0].scatter(x, y, color='red', s=100)
axs[1, 0].set_title("Scatter Plot")

axs[1, 1].pie(percentages, labels=pie_labels, autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title("Pie Chart")

plt.tight_layout()
plt.show()
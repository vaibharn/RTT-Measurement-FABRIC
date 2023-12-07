import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['STAR-CLEM','CLEM-CERN','CERN-STAR','CERN-MASS','CERN-MAX','CERN-MICH','CERN-NCSA','CERN-UTAH','MASS-MAX','MASS-MICH','MASS-NCSA','MASS-STAR','MASS-UTAH','MAX-MICH','MAX-NCSA','MAX-STAR','MAX-UTAH','MICH-NCSA','MICH-STAR','MICH-UTAH','NCSA-STAR','NCSA-UTAH','STAR-UTAH']
data1 = [30.51,115.52,113.33,106.88,107.22,123.50,120.73,139.68,15.39,31.84,29.06,26.64,57.58,22.32,19.41,17.02,47.93,7.67,5.25,36.18,2.47,33.41,30.98]
data2 = [30.53,105.83,113.41,109.40,102.16,128.31,105.84,144.23,16.55,33.44,30.01,28.11,58.99,22.37,19.60,17.31,48.12,7.74,5.34,36.26,2.51,33.45,31.05]
data3 = [28.164, 104.723, 110.469, 105.999, 100.112, 122.284, 102.937, 138.184, 14.127, 29.025, 27.008, 23.695, 55.231, 21.502, 19.317, 14.849, 45.269,  6.666,  3.324, 34.697,  2.278, 32.618, 28.745]
data4 = [35.390, 118.716, 116.754, 113.139, 107.337, 133.599, 125.720, 149.098, 20.906, 36.959, 33.374, 29.575, 64.566, 23.991, 21.640, 22.120, 52.016, 9.819, 7.589, 38.384, 4.108, 37.090, 36.876]
# Set up the figure and axes
fig, ax = plt.subplots()

# Set the bar width
bar_width = 0.2

# Set the positions of bars on X-axis
bar_positions1 = np.arange(len(categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width
bar_positions4 = bar_positions3 + bar_width

# Create the bar plots
bar1 = ax.barh(bar_positions1, data1, bar_width, label='One-Way Latency')
bar2 = ax.barh(bar_positions2, data2, bar_width, label='Ping')
bar3 = ax.barh(bar_positions3, data3, bar_width, label='P4 Programmable Data Plane Switch')
bar4 = ax.barh(bar_positions4, data4, bar_width, label='TCP Application Layer (Scapy)')

# Customize the plot
ax.set_yticks(bar_positions1 + 4*bar_width / 2)
ax.set_yticklabels(categories)
ax.legend()

# Show the plot
plt.show()

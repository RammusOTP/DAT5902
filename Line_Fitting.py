"""Import necessary libraries"""
import numpy as np
import matplotlib.pyplot as plt

"""Set the file path to open"""
path = '/Users/emmanuel/Documents/DAT5902/linear_data.csv'

"""Load the data as a variable"""
linear_data = np.loadtxt(path, delimiter = ',', skiprows = 1)

#print(linear_data)

"""Split the data into two lists"""
data_x = linear_data[:, 0]
data_y = linear_data[:, 1]

#print(data_x)
#print(data_y)

"""Plot the data points as a scatter plot"""
plt.scatter(data_x, data_y)

"""Create a line of best fit using numpy polyfit"""
slope, intercept = np.polyfit(data_x, data_y, 1)
best_fit_line = slope * data_x + intercept
plt.plot(data_x, best_fit_line, color='red', label='Best Fit Line')

"""Show the plot"""
plt.show()
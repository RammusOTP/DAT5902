"""Import necessary libraries"""
import numpy as np
import matplotlib.pyplot as plt

"""Create a function to load the csv"""
def load_data(file_path):
    try:
        return np.loadtxt(file_path, delimiter=',', skiprows=1)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except ValueError as e:
        print(f"Error: Could not convert data to an array. {e}")
        return None

"""Create a function to split the data into two separate variables"""
def split_data(data):
    data_x = data[:, 0]
    data_y = data[:, 1]
    return data_x, data_y

"""Create a function to plot the data as a scatter plot"""
def plot_scatter_graph(data_x, data_y):
    plt.scatter(data_x, data_y)
    plt.show()


def main(file_path):
    data = load_data(path)
    data_x, data_y = split_data(data)
    plot_scatter_graph(data_x, data_y)

if __name__ == "__main__":
    path = '/Users/emmanuel/Documents/DAT5902/linear_data.csv'
    main(path)


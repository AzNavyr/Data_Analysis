# -*- coding: utf-8 -*-
'''
 @author:   srattigan
 @date:     18-Feb-2022
 @project:  ass2 data analysis
 @description:  simplified chart creation
'''

# -- imports
import tempfile
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# -- globals
# set up local temp file
os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()


# -- functions
def custom_make_bar(x_values, y_values, title="", y_lable="", x_lable=""):
    '''
    (list of str, list of num) -> None
    Creates a bar chart from data supplied.
    '''
    x = np.arange(len(x_values))  # the label locations
    width = 0.2  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in y_values.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(y_lable)
    ax.set_xlabel(x_lable)
    ax.set_title(title)
    ax.set_xticks(x + width, x_values)
    ax.legend(loc='best', ncols=3)
    plt.show()
    
def make_bar_horizontal(x_values, y_values, title="", x_label="", y_label=""):
    '''
    (list of str, list of num) -> None
    Creates a bar chart from data supplied.
    x_values, y_values, title="", x_label="", y_label=""
    '''
    colors = ["C2", "C3", "C4"]
    plt.figure(figsize=(15, 6))
    plt.barh(x_values, y_values, color=colors, edgecolor = 'black', height = 0.5)
    plt.grid()
    plt.xlabel(x_label, fontsize=10, color='blue')
    plt.ylabel(y_label, fontsize=10, color='blue')
    plt.title(title, fontweight='bold', fontsize=15, color='blue', loc='center')
    plt.show()

def custom_make_pi(values, legend, pctdistance=1.1, labeldistance=1.5, size=1.4, dp=1):
    '''
    (list of str, list of num, int, int) -> None
    Creates a pi chart from data supplied.
    Other settings for this chart are here:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
    '''
    plt.axis("equal")
    plt.pie(values,
            radius=size,
            pctdistance=pctdistance,
            labeldistance=labeldistance,
            counterclock=False,
            autopct=f'%0.{dp}f%%')
    plt.legend(legend, loc='best', ncols=3)
    plt.show()
    
def make_bar(x_labels, y_values, title=""):
    '''
    (list of str, list of num) -> None
    Creates a bar chart from data supplied.
    '''
    plt.bar(x=x_labels, height=y_values)
    plt.title(title)
    plt.show()

def make_pi(labels, values, title="", size=1, dp=1):
    '''
    (list of str, list of num, str, int, int) -> None
    Creates a pi chart from data supplied.
    Other settings for this chart are here:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html
    '''
    plt.title(title)
    plt.axis("equal")
    plt.pie(values, labels=labels, radius=size, autopct=f'%0.{dp}f%%')
    plt.show()

def make_plot(x_vals, y_vals, x_axis='x axis', y_axis='y axis', line='o'):
    '''
    (list of num, list of num, str, str, str) -> None
    line as o creates a scatter chart.
    Using -b creates a solid line joining the points.
    Create a plot or scatter chart from data supplied.
    Other settings for this chart are here:
    https://matplotlib.org/stable/api/pyplot_summary.html
    '''
    plt.plot(x_vals, y_vals, line)
    plt.ylabel(y_axis)
    plt.xlabel(x_axis)
    plt.show()


def make_hist(arr):
    '''
    (list of num) -> None
    Generates a histogram from a list of numbers
    '''
    plt.hist(arr)
    plt.show()

# -- main body- just runs some test code to demo functions
if __name__ == "__main__":
    make_bar_horizontal()
    #pi_vals = [1400, 600, 300, 410, 250]
    #pi_labels = ["Rent", "Food", "Data/TV", "Car", "Utilities"]
    #plt_x = [1, 2, 3, 4, 5, 6, 7]
    #plt_y = [50, 51, 52, 48, 47, 49, 46]
    #print("Running test data for charts...")
    #make_bar(pi_labels, pi_vals)
    #make_pi(pi_labels, pi_vals)
    #make_plot(plt_x, plt_y)
    #make_plot(plt_x, plt_y, "just numbers", "bigger numbers", "-b")
    # make_hist(norm_arr)
    #input("Enter to finish...")
    #print("Done")
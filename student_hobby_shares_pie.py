# -*- coding: utf-8 -*-
"""
 @author:   Dmytro
 @date:     23 May 2024 01:30
 @project:  assignment 2 
 @description: Makes hobbies pie chart for men and women
"""

import matplotlib.pyplot as plt
from chartmaker import make_pi
from helpers import file_to_list

def make_hobby_shares_pie():
    """
    Reads data from a CSV file and generates pie charts showing hobby distribution by gender.
    Args:
    filename (str): Path to the CSV file containing hobby and gender data.
    Returns:
    None, displays the pie charts.
    """
    # Read CSV using helpers.py
    data = file_to_list('datasets_full/student_attitude_behavior.csv')

    # Create dictionaries to store hobby counts for each gender
    hobby_counts = {'Male': {}, 'Female': {}}

    # Iterate through rows (excluding header row)
    for row in data[1:]:  # Start from index 1 to skip headers
        hobby = row[8]
        gender = row[1]

        # Update the count for the specific hobby and gender
        if hobby in hobby_counts[gender]:
            hobby_counts[gender][hobby] += 1
        else:
            hobby_counts[gender][hobby] = 1

    # Create pie charts for each gender
    for gender in hobby_counts:
        labels = list(hobby_counts[gender].keys())
        values = list(hobby_counts[gender].values())

        plt.figure(figsize=(8, 8))
        make_pi(labels, values, size=1.2)  # Using make_pi from chartmakers.py
        #plt.title(f'Top Hobbies for {gender} Students', fontsize=14)
        #plt.show()

# This block ensures the function runs only when the script is executed directly (not when imported)
if __name__ == '__main__':
    make_hobby_shares_pie()

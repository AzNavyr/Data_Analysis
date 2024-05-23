# -*- coding: utf-8 -*-
"""
@author:   Dmytro (with integrations from srattigan)
@date:     23 May 2024 02:00
@project:  assignment 2 
@description: Analyzes student hobbies and generates a bar chart by gender
"""

import pandas as pd
import matplotlib.pyplot as plt

# Import from teacher's modules
from helpers import file_to_list  
from chartmaker import make_bar

def make_hobby_comparison_chart():
    """
    Generates a bar chart showing the count of students' hobbies by gender.

    Parameters:
        file_path (str): The path to the CSV file containing student data.
    """
    # Read CSV file using the helper function
    data = file_to_list('datasets_full/student_attitude_behavior.csv')[1:]  # Exclude header row

    # Create a DataFrame for easier manipulation
    df = pd.DataFrame(data, columns=file_to_list('datasets_full/student_attitude_behavior.csv')[0])

    # Data processing
    hobby_gender_df = df[['hobbies', 'Gender']]
    hobby_gender_counts = hobby_gender_df.groupby(['hobbies', 'Gender']).size().unstack().fillna(0)

    # Prepare data for plotting
    hobbies = hobby_gender_counts.index
    male_counts = hobby_gender_counts['Male']
    female_counts = hobby_gender_counts['Female']

    # Plot with improved clarity and style
    plt.figure(figsize=(10, 6))  # Adjust the figure size for better readability
    make_bar(hobbies, male_counts, title="Students by Hobby and Gender (Male)")
    make_bar(hobbies, female_counts, title="Students by Hobby and Gender (Female)")

    plt.show()

if __name__ == "__main__":
    make_hobby_comparison_chart()

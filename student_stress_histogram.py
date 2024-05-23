# -*- coding: utf-8 -*-
"""
 @author:   Dmytro
 @date:     23 May 2024 01:00
 @project:  assignment 2 
 @description: makes hobbies pichart for men and women
"""

# Import the necessary functions
from helpers import file_to_list
from chartmaker import make_hist

def make_stress_levels():
    """
    Generates a histogram of daily studying times for students with high stress levels from a CSV file.
    The function filters student data by 'Bad' or 'Awful' stress levels, extracts studying times, and creates a histogram.
    """    
    # Read the CSV data
    data = file_to_list('datasets_full/student_attitude_behavior.csv')

    # Extract the header and data separately
    header = data[0]
    data = data[1:]

    # Find the indices for 'Stress Level' and 'Daily Studying Time'
    stress_level_index = header.index('Stress Level ')
    daily_studying_time_index = header.index('daily studing time')

    # Filter the data for students with 'Bad' stress level
    filtered_data = []
    for row in data:
        if row[stress_level_index] in ['Bad', 'Awful']:
            filtered_data.append(row)

    # Collect the daily studying time for filtered data
    daily_studying_times = []
    for row in filtered_data:
        daily_studying_times.append(row[daily_studying_time_index])

    # Create the histogram
    make_hist(daily_studying_times)

if __name__ == "__main__":
    make_stress_levels()
# -*- coding: utf-8 -*-
"""
 @author:   Dmytro
 @date:     23 May 2024   03-30
 @project:  assignment 2 
 @description: create main menu
"""

import easygui
import matplotlib.pyplot as plt
from helpers import file_to_list

# Import functions from the chart modules
from student_hobby_comparison_function import make_hobby_comparison_chart
from student_hobby_shares_pie import make_hobby_shares_pie
from student_stress_histogram import make_stress_levels

def main():
    """
    creates main menu to display charts
    allows the user to select between charts or to quit the application
    """
    data = file_to_list("datasets_full/student_attitude_behavior.csv")  # Load data
    while True:
        choices = ["Hobby Shares", "Hobby Comparison", "Stress Levels", "Quit"]
        image = "images/student_behavior.jpg"
        choice = easygui.buttonbox("Choose an option:", image=image, choices=choices)
        if choice == "Hobby Shares":
            make_hobby_shares_pie()
        elif choice == "Hobby Comparison":
            make_hobby_comparison_chart()
        elif choice == "Stress Levels":
            make_stress_levels()
        elif choice == "Quit":
            break

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
 @author:   Maksym Makiienko
 @date:     10 May 2024
 @project:  assignment 2 
 @description: file process csv file onlinefoods and makes charts
"""
# -- imports
#import csv
import doctest
import re
import matplotlib.pyplot as plt
import numpy as np
from pylint.lint import Run
import easygui as eg
import chartmaker as cm
import helpers as h
# -- globals
TEST_DATA = 'datasets_test/onlinefoods.csv'
FULL_DATA = 'datasets_full/onlinefoods.csv'
ARR = h.file_to_list(FULL_DATA)
# print(ARR[1:])
# HEADER = ARR[0]  # perhaps?
HEADER = ['Age',
          'Gender',
          'Marital Status',
          'Occupation',
          'Monthly Income',
          'Educational Qualifications',
          'Family size',
          'latitude',
          'longitude',
          'Pin code',
          'Output',
          'Feedback',
          'Yes/No']

# -- functions
def ocupation_pi():
    """
    (None)->None
    Generate a pi chart to show the breakdown of ocupation
    pi chart (idx 4)
    """
    ocupation_dict = {}
    for row in ARR[1:]:  # drop header row
        ocupation = row[3]
        if ocupation not in ocupation_dict:
            ocupation_dict[ocupation] = 1
        else:
            ocupation_dict[ocupation] += 1
    # print(country_dict)
    labels = list(ocupation_dict)
    # print(labels)
    values = []
    for label in labels:
        values.append(ocupation_dict[label])
    # print(values)
    cm.make_pi(labels, values)

def age_representation():
    '''
    (None) -> None
    This function counts how often people of different ages get food
    through online
    '''
    ages = []
    for row in ARR[1:]:
        ages.append(row[0])
    cm.make_hist(ages)

def extract_max(string):
    '''
    (string) -> int
    This function takes a string find there numbers and return maximum.
    >>> extract_max('fkgjd345dkfj565slfdj-45lkj5677')
    5677
    '''
    numbers = re.findall('\d+', string)
    numbers = map(int, numbers)
    return max(numbers)

def sort_list_by_max_num(arr):
    '''
    (list of strings) -> (sorted list of strings)
    This function takes list of strings and returns list of strings sorted according to largest
    number that containts this string.
    >>> sort_list_by_max_num(['wwrw56', 'dfdf45', 'fgf34', 'fffff'])
    ['fffff', 'fgf34', 'dfdf45', 'wwrw56']
    '''
    sorted_list = sorted(arr, key=lambda x: \
    int(re.search('\d+', x).group()) if re.search('\d+', x) else 0)
    return sorted_list

def sort_dict_by_max_num(dictionary):
    '''
    (dictionary of strings) -> sorted dictionary of strings
    This function takes a dictionary of strings and returns list of strings sorted according to 
    largest number in key string
    >>> sort_dict_by_max_num({'565dd': [2, 67], '545ff': [0, 4], 'fggf667': [1, 77]})
    {'545ff': [0, 4], '565dd': [2, 67], 'fggf667': [1, 77]}
    '''
    new_list = list(dictionary)
    #print(new_list)
    sorted_list = sort_list_by_max_num(new_list)
    #print(sorted_list)
    sorted_dict = {}
    for _, value in enumerate(sorted_list):
        sorted_dict[value] = dictionary[value]
    return sorted_dict

def list_to_dct(arr, column1, column2):
    """
    (list, int, int) -> dict
    This function takes number of first column and second column and returns
    a dictionary where key is taken from first column and value is a list
    of values of second column which belong to column of keys. Also it removes
    first line with headings.
    >>> list_to_dct([['Number by order', 'Name', 'Job Title', 'Age',\
    'Salary per hour'], ['1', 'Bob', 'Plumber', '34', '12'], ['2', 'Jeck',\
    'Plumber', '23', '10'], ['3', 'Mike', 'Carpenter', '40', '15']], 3, 5)
    {'Plumber': '12, 10', 'Carpenter': '15'}
    """
    income_feedback = {}
    incomes = []
    feedbacks = []
    for row in arr[1:]:
        feedback = row[column2-1]  # Assuming you have an 'feedback' column
        income = row[column1-1]  # Assuming you have a 'income' column
        feedbacks.append(feedback)
        incomes.append(income)
    for index, income in enumerate(incomes):
        if incomes[index] not in income_feedback:
            income_feedback[incomes[index]] = feedbacks[index]
        else:
            income_feedback[incomes[index]] += ', ' + feedbacks[index]
    return sort_dict_by_max_num(income_feedback)

def dct_to_zero_labels(arr, column1, column2):
    """
    (arr, int, int) -> list, dct
    This function takes a directory with level of income as a key and list of
    feedbacks as a value and returns x_label as list of keys and dictionary
    where feedbacks are keys and values are the lists of numbers which show
    positive and negative feedbacks according to order of incomes in x_label list.
    >>> dct_to_zero_labels([['Number by order', 'Name', 'Job Title', 'Age',\
    'Salary per hour'], ['1', 'Bob', 'Plumber', '34', '12'], ['2', 'Jeck',\
    'Plumber', '23', '10'], ['3', 'Mike', 'Carpenter', '40', '15'], ['4',\
    'Hanna', 'Hairdresser', '24', '15']], 3, 5)
    (['Plumber', 'Carpenter', 'Hairdresser'], {'12': [0, 0, 0], '10': [0, 0, 0], '15': [0, 0, 0]}, {'Plumber': ['12', '10'], 'Carpenter': ['15'], 'Hairdresser': ['15']})
    """
    income_feedback = list_to_dct(arr, column1, column2)
    for key, values in income_feedback.items():
        income_feedback[key] = values.split(', ')
    for key, values in income_feedback.items():
        for index, value in enumerate(values):
            values[index] = value.strip()
    #print(income_feedback)
    x_labels = list(income_feedback)
    #print(x_labels)
    pos_neg = {}
    for key, values in income_feedback.items():
        for index, value in enumerate(values):
            #print(index, value)
            if value not in pos_neg:
                pos_neg[value] = []
                #print(pos_neg)
                for key, values in income_feedback.items():
                    pos_neg[value].append(0)
    return x_labels, pos_neg, income_feedback

def zero_labels_to_labels(arr, column1, column2):
    '''
    (arr, int, int) -> list, dct
    This function gets list made from csv file number of first and second columns
    and returns list and dictionary for building bar chart.
    >>> zero_labels_to_labels([['Number by order', 'Name', 'Job Title', 'Age',\
    'Salary per hour'], ['1', 'Bob', 'Plumber', '34', '12'], ['2', 'Jeck',\
    'Plumber', '23', '10'], ['3', 'Mike', 'Carpenter', '40', '15'], ['4',\
    'Hanna', 'Hairdresser', '24', '15']], 3, 5)
    (['Plumber', 'Carpenter', 'Hairdresser'], {'12': [1, 0, 0], '10': [1, 0, 0], '15': [0, 1, 1]})
    '''
    x_labels, pos_neg, income_feedback = dct_to_zero_labels(arr, column1, column2)
    num = 0
    for _, values in income_feedback.items():
        if num > len(income_feedback) - 1:
            break
        for _, value in enumerate(values):
            pos_neg[value][num] += 1
        num += 1
    return x_labels, pos_neg

def income_feedbacks():
    """
    (None) -> None
    This function makes a plot chart based on age and feedback.
    """
    x_labels, pos_neg = zero_labels_to_labels(ARR, 5, 12)
    width = 0.6
    _, axis = plt.subplots(figsize=(8, 4))
    #fig = 640*640
    #print(fig, axis)
    bottom = np.zeros(5)
    for key, value in pos_neg.items():
        plot = axis.bar(x_labels, value, width, label=key, bottom=bottom)
        bottom += value
        axis.bar_label(plot, label_type='center')
    axis.set_title('Feedback depending on income level')
    axis.legend()
    plt.show()

def main():
    '''
    (None) -> None
    Create main menu for making charts in onlinefoods.py using easygui
    '''
    menu = ["Histogram Ages",
            "Pie Chart For Ocupations",
            "Bar Chart For Feedbacks by Income Level",
            "Quit"]
    while True:
        pick= eg.indexbox(msg="Select the type of Chart",
                          title="Information About Selling Of Food Through Online",
                          choices=menu, image="images/Delivery_Driver_Delivering_Takeout_short.png")
        if pick == 0:
            age_representation()
        elif pick == 1:
            ocupation_pi()
        elif pick == 2:
            income_feedbacks()
        elif pick == 3:
            eg.msgbox(msg="Back To The Main Menu...",
                      title="Leaving Online Foods Data...")
            break

def lint_me():
    """
    (None) -> None
    This is a workaround to allow the pylint module be run from this file.
    Usually, pylint would be installed and run trough the shell/terminal,
    but since we do not have a terminal here, this gets the module and
    checks the current file for compliance.
    """
    #clear_scr()
    print("Checking for lint errors...")
    Run(['onlinefoods.py'])

# -- main body
if __name__ == "__main__":
    main()
    #doctest.testmod(verbose=True)
    #lint_me()
    
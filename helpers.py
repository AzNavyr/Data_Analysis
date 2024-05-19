# -*- coding: utf-8 -*-
"""
 @author:   srattigan
 @date:     12 Jan 2024
 @project:  assignment 2 prep
 @description: file and data processing helpers
               Provided: csv file reader
               Use: any data cleaning code can be created and saved here
               separating this processing code from the main code logic.
"""

# imports
import csv
import pycountry
import pycountry_convert as pc

# functions

def file_to_list(fname):
    '''
    (csv file obj) -> list of list of obj
    Reads a csv file and returns a python list of list,
    where each sub-list is a line from the database table.
    The list at index zero holds the column headings, while
    those that follow hold data.
    '''
    if fname[-3:].lower() == 'csv':
        with open(fname, encoding="utf-8", mode='r') as read_obj:  # open file read only mode
            csv_reader = csv.reader(read_obj)  # get reader object
            list_arr = list(csv_reader)  # get a list of lists
        # next, run through all data and convert valid str objs to nums
        list_arr_nums = []
        for line in list_arr:
            newline = []
            for elem in line:
                try:
                    e = float(elem)
                    newline.append(e)
                except TypeError:
                    newline.append(elem)
            list_arr_nums.append(newline)
        return list_arr_nums
    else:
        raise TypeError("Unexpected file extension received")
    
def get_country(state):
    """
    (None) -> None
    The function decrypts the name of the country by means of the ISO 3166-1 standard.
    Alpha_2 form to a user-readable form
    """
    country_eng = pycountry.countries.get(alpha_2=state).name
    return country_eng

def get_currencies(curr):
    """
    (None) -> None
    The function decrypts the name of currencies by means of the ISO 4217 standard.
    Alpha_2 form to a user-readable form
    """
    currency_name = pycountry.currencies.lookup(curr).name
    return currency_name

def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name
    
    
if __name__ == "__main__":
    print("You just ran the helpers file!")

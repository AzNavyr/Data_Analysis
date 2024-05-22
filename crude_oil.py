'''
 @authors: Olena Pavlenko  
 @date:     09-May-2024
 @project:  teamwork
 @description:  Crude Oil Analys
'''

import operator
import easygui as eg
from pylint.lint import Run
import chartmaker as cm
import helpers as h

TEST_DATA = 'datasets_test/crudeoil_usa_2009.csv'
FULL_DATA = 'datasets_full/crudeoil_usa_2009.csv'
ARR = h.file_to_list(TEST_DATA)

def quantity_by_year_bar():
    """
    (None) -> None
    Generate a bar chart to show Bar of quantati imported oil by  year.
    """
    crude_dict={'2009-2013':0,
                 '2014-2018':0,
                 '2019-2023':0,
                 '2024':0}
    for row in ARR[1:]:  # drop header row
        year = row[0]
        quantity=row[7]
        year_n=int(year)
        if 2009 <= year_n <= 2013:
            crude_dict['2009-2013']+=quantity
        elif 2014 <= year_n <= 2018:
            crude_dict['2014-2018']+=quantity
        elif 2019 <= year_n <= 2023:
            crude_dict['2019-2023']+=quantity
        elif year_n == 2024:
            crude_dict['2024']+=quantity
    x_labels = list(crude_dict)
    y_values = []
    for lab in x_labels:
        y_values.append(crude_dict[lab])
    cm.make_bar(x_labels, y_values, title="Quantity by release year")

def top_5_suppliers():
    """
    (None) -> None
    Generate a pi chart to show TOP 5 suppliers. Data not include "Country not found"
    """
    suppliers_dict = {}
    for row in ARR[1:]:
        supplier = row[2]
        if supplier not in ["Country not known", "World"]:
            if supplier not in suppliers_dict:
                suppliers_dict[supplier] = [row[7]]
            else:
                suppliers_dict[supplier].append(row[7])
    for key, var in suppliers_dict.items():
        suppliers_dict[key] = sum(var) / len(var)
    sorted_dict = dict(sorted(suppliers_dict.items(), key=operator.itemgetter(1)))
    top_5_sales = dict(list(sorted_dict.items())[-5:])
    labels = list(top_5_sales)
    values = []
    for lab in labels:
        values.append(top_5_sales[lab])
    cm.make_pi(labels, values)

def type_oil_for_last_5_years():
    """
    (None) -> None
    Generate a plot chart of type of imported oil for the last 5 years
    """
    type_oil_dict = {}
    for row in ARR[1:]:
        type_oil = row[6]
        year_n=int(row[0])
        if year_n >= 2020:
            if type_oil not in type_oil_dict:
                type_oil_dict[type_oil] = [row[7]]
            else:
                type_oil_dict[type_oil].append(row[7])
    for key, var in type_oil_dict.items():
        type_oil_dict[key] = sum(var) / len(var)
    x_vals = list(type_oil_dict)
    y_vals = []
    for lab in x_vals:
        y_vals.append(type_oil_dict[lab])
    cm.make_plot(x_vals, y_vals, x_axis='x axis', y_axis='y axis', line='-b')
'''
def type_oil_new():
    """
    (None) -> None
    Generate a pi chart for types of imported oil by years.
    """
    type_oil_dict = {'2009-2013': {"Heavy Sour":0,
                                   "Light Sweet": 0,
                                   "Light Sour": 0,
                                   "Heavy Sweet":0,
                                   "Medium": 0},
                     '2014-2018': {"Heavy Sour":0,
                                   "Light Sweet": 0,
                                   "Light Sour": 0,
                                   "Heavy Sweet":0,
                                   "Medium": 0},
                     '2019-2023': {"Heavy Sour":0,
                                   "Light Sweet": 0,
                                   "Light Sour": 0,
                                   "Heavy Sweet":0,
                                   "Medium": 0},
                     '2024': {"Heavy Sour":0,
                                   "Light Sweet": 0,
                                   "Light Sour": 0,
                                   "Heavy Sweet":0,
                                   "Medium": 0}
                                }
    for row in ARR[1:]:
        type_oil = row[-2]
        quantity=int(row[-1])
        year = row[0]
        year_n=int(year)
        if 2013 >= year_n >= 2009:
            type_oil_dict["2009-2013"][type_oil] += quantity
        elif 2018 >= year_n >= 2014:
            type_oil_dict["2014-2018"][type_oil] += quantity
        elif 2023 >= year_n >= 2019:
            type_oil_dict["2019-2023"][type_oil] += quantity
        elif year_n == 2024:
            type_oil_dict["2024"][type_oil] += quantity
    select=eg.choicebox(msg='Select oil type:',
                              title='Oil Type',
                              choices=type_oil_dict)
    if select:
        labels = list(type_oil_dict[select])
        values = []
        for lab in labels:
            values.append(type_oil_dict[select][lab])
        cm.make_pi(labels, values)
'''
def type_oil_new():
    """
    (None) -> None
    Generate a pi chart for types of imported oil by years.
    """
    type_oil_dict={}
    for year in range(2009, 2025):
        type_oil_dict[year]={"Heavy Sour":0,
                                   "Light Sweet": 0,
                                   "Light Sour": 0,
                                   "Heavy Sweet":0,
                                   "Medium": 0}
    for row in ARR[1:]:
        type_oil = row[-2]
        quantity=int(row[-1])
        year = row[0]
        type_oil_dict[year][type_oil] += quantity
    selected_year = eg.choicebox(msg='Select year:', title='Oil Import Year', choices=type_oil_dict)
    if selected_year:
        selected_year = int(selected_year)
        labels = list(type_oil_dict[selected_year].keys())
        values = list(type_oil_dict[selected_year].values())
        cm.make_pi(labels, values)
        
def main():
    '''
    (None) -> None
    Create main menu for datasets using easygui
    '''
    menu = ["Bar quantity by year",
            "Pi chart Top 5 suppliers",
            "Plot of types of oil for last 5 years",
            "Type of oil by years",
            "Exit"]
    while True:
        pick= eg.indexbox(msg="Select data to view",
                          title="Crude Oil menu",
                          choices=menu,
                          image="images/picture_oil.jpeg")
        if pick == 0:
            quantity_by_year_bar()
        elif pick == 1:
            top_5_suppliers()
        elif pick == 2:
            type_oil_for_last_5_years()
        elif pick == 3:
            type_oil_new()
        elif pick == 4:
            eg.msgbox(msg="Goodbye...",
                      title="Leaving Crude Oil module...",
                      image="images/thank_you_oil.jpg")
            break

def lint_me():
    """
    (None) -> None
    This is a workaround to allow the pylint module be run from this file.
    Usually, pyylint would be installed and run trough the shell/terminal,
    but since we do not have a terminal here, this gets the module and
    checks the current file for compliance.
    """
    print("Checking for lint errors...")
    Run(['crude_oil.py'])

if __name__ == "__main__":
    main()
    #lint_me()

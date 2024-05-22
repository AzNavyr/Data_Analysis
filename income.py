'''
 @authors: Nataliia Tytovets  
 @date:     09-May-2024
 @project:  teamwork
 @description:  US Incomes
'''
import pandas as pd
import easygui as eg
from pylint.lint import Run
import matplotlib.pyplot as plt
import numpy as np
import chartmaker as cm
import helpers as h

TEST_DATA = 'datasets_test/usa_income.csv'
FULL_DATA = 'datasets_full/usa_income_full.csv'
ARR = h.file_to_list(FULL_DATA)

def comparison_countries():
    '''
    (None) -> None
    Bar chart comparing Native Americans and non-Native Americans.
    '''
    nationalities = {"Native American": 0,
                     "Non-native American": 0}
    for row in ARR[1:]:
        country = row[13]
        if country == 'United-States':
            nationalities['Native American'] += 1
        else:
            nationalities['Non-native American'] += 1
    x_labels = list(nationalities)
    y_values = []
    for k in x_labels:
        y_values.append(nationalities[k])
    cm.make_bar(x_labels, y_values, title="Comparison between native American and non-native")

def education_comparison():
    '''
    (None) -> None
    This function compare educational level with gender.
    '''
    education = {'Male': {'Tertiary education': 0,
                          'High-School education': 0},
                 'Female': {'Tertiary education': 0,
                          'High-School education': 0}}
    for row in ARR[1:]:
        education_num = row[4]
        if education_num < 10 and row[9] == "Male":
            education['Male']['Tertiary education'] += 1
        elif education_num > 10 and row[9] == 'Male':
            education['Male']['High-School education'] += 1
        elif education_num < 10 and row[9] == 'Female':
            education['Female']['Tertiary education'] += 1
        elif education_num > 10 and row[9] == 'Female':
            education['Female']['High-School education'] += 1
    option = ['Male', 'Female']
    select = eg.multchoicebox(msg='Select gender:', choices=option)
    if not select:
        eg.msgbox(msg="Nothing to show",
                      title="Operation cancelled",)
        return
    if 'Male' in select and 'Female' in select:
        level_education = ('Tertiary education', 'High-School education')
        gender_counts = {
            'Male': np.array([education['Male']['Tertiary education'],
                              education['Male']['High-School education']]),
            'Female': np.array([education['Female']['Tertiary education'],
                                education['Female']['High-School education']])
        }
        width = 0.8
        _, graph = plt.subplots()
        bottom = np.zeros(len(level_education))
        for name, gender_counts in gender_counts.items():
            graphic = graph.bar(level_education, gender_counts, width, label=name, bottom=bottom)
            bottom += gender_counts
            graph.bar_label(graphic, label_type='center')
        graph.set_title('Comparison of education level')
        graph.legend()
        plt.show()
    elif 'Male' in select:
        x_vals = list(education['Male'])
        y_vals = []
        for k in x_vals:
            y_vals.append(education['Male'][k])
        cm.make_plot(x_vals, y_vals, x_axis='Level of Education', y_axis='Count', line='-')
    elif 'Female' in select:
        x_vals = list(education['Female'])
        y_vals = []
        for k in x_vals:
            y_vals.append(education['Female'][k])
        cm.make_plot(x_vals, y_vals, x_axis='Level of Education', y_axis='Count', line='-')

def hours_per_week():
    '''
    (None) -> None
    Create a pie chart to compare hours worked by race.
    The function contains a filtered list by gender
    '''
    df_data = pd.read_csv(FULL_DATA)
    gender = df_data['gender'].drop_duplicates().sort_values()
    select = eg.multchoicebox(msg='Select gender:', choices=gender)
    if select:
        filtered_df = df_data[df_data['gender'].isin(select)]
        grouped_by = filtered_df.groupby('race')
        x_labels = filtered_df['race'].unique()
        y_values = grouped_by['hours-per-week'].mean()
        cm.make_pi(x_labels, y_values)
    else:
        eg.msgbox(msg="Selection was cancelled...",
                      title="Operation cancelled",)

def main():
    '''
    (None) -> None
    Create main menu for datasets using easygui
    '''
    menu = ["Сomparison between non-native and native American",
            "Comparison of education by gender",
            "Comparison of hours each week by race",
            "Exit"]
    while True:
        pick= eg.indexbox(msg="Select data you want to see",
                          title="US Incomes",
                          choices=menu,
                          image='images/income_small.jpg')
        if pick == 0:
            comparison_countries()
        elif pick == 1:
            education_comparison()
        elif pick == 2:
            hours_per_week()
        elif pick == 3:
            eg.msgbox(msg="Goodbye...",
                      title="Leaving US module...",
                      image='images/goodbye.jpg')
            break

def lint_me():
    '''
    (None) -> None
    This function checks code for errors, using pylint module.
    '''
    print("Checking for lint errors...")
    Run(['main.py'])
if __name__ == "__main__":
    main()
    #lint_me()
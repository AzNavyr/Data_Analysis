'''
 @authors: Enver Osmanov
 @date:     09-May-2024
 @project:  teamwork
 @description:  DS Salaries
'''
import pandas as pd
import easygui as eg
import chartmaker as cm
import helpers as h
import threading
import windows_tk as wtk 

TEST_DATA = 'datasets_test/dataScience_salaries_2024.csv'
FULL_DATA = 'datasets_full/dataScience_salaries_2024.csv'
CHOICE = ['View Salary by Job Type',
          'Top 3 IT specialists by continent',
          'Top 5 by national composition',
          'Exit']

def show_message(title, alpha_2):
    """
    (str, list) -> None
    Create a message box
    """
    message = {}
    for indx, val in enumerate(alpha_2[:5]):
        message[val]=h.get_country(alpha_2[indx])
    eg.msgbox(msg=message, title=title)

#Show average salary in USD
def avg_salary_by_type():
    """
    (None) -> None
    The average salary in USD is relative to the size of the company and the type of employment
    """
    company_size = ['Large', 'Medium', 'Small']
    employment_types = {'FT': 0,
                        'PT': 0,
                        'CT': 0,
                        'FL': 0}
    
    df = pd.read_csv(FULL_DATA)#Create data frame
    df = df.loc[df['work_year'] != 2024]#Delete all rows with work_year==2024
    
    #Group by employment_type and company_size and count average salary in USD
    df_group = df.groupby(['employment_type',
                           'company_size'])['salary_in_usd'].mean()
    
    for key in employment_types.keys():#Via for loop fill out employment_types(dict)
        employment_types[key] = list(df_group[key]) 
    
    #Determine the data on the x and y axes
    x_labels = company_size
    y_values = employment_types
    #Using my custom function to create a graph
    cm.custom_make_bar(x_labels, y_values,
                       title="Average salary in USD, depending on the type of employment",
                       y_lable="Salary",
                       x_lable="Company size")
    
def top_it_jobs_by_continent():
    """
    (None) -> None
    The function shows the top 3 specialties by
    salary level on the continents in the IT field,
    depending on the level of experience
    """
    countries = {}
    df = pd.read_csv(FULL_DATA)#Create data frame
    df = df.loc[df['work_year'] != 2024]#Delete all rows with work_year==2024
    uniq_countries = list(set(df['company_location']))#List of uniq countries(alpha_2)
    for indx, val in enumerate(sorted(uniq_countries)):
        countries[val] = countries.get(val,[]) + [h.get_country(val),
                                                  h.country_to_continent(h.get_country(val))]
        #creating a new column in the date frame based on Alpha_2 country code
        df['continent'] = df.company_location.apply(lambda x: h.country_to_continent(h.get_country(x)))
        
    choice = eg.choicebox(msg='Сhoose a continent',
                          title='The first question',
                          choices=['Asia',
                                   'Africa',
                                   'Europe',
                                   'North America',
                                   'Oceania',
                                   'South America'])
    if choice == 'Asia':
        df = df.loc[df['continent'] == 'Asia'] 
    elif choice == 'North America':
        df = df.loc[df['continent'] == 'North America']
    elif choice == 'Europe':
        df = df.loc[df['continent'] == 'Europe']
    elif choice == 'Africa':
        df = df.loc[df['continent'] == 'Africa']
    elif choice == 'Oceania':
        df = df.loc[df['continent'] == 'Oceania']
    elif choice == 'South America':
        df = df.loc[df['continent'] == 'South America']
  
    choice = eg.choicebox(msg='Сhoose an experience level',
                          title='The second question',
                          choices=['Entry-level / Junior',
                                   'Mid-level / Intermediate',
                                   'Senior-level / Expert',
                                   'Executive-level / Director'])
    if choice == 'Entry-level / Junior':
        df = df.loc[df['experience_level'] == 'EN']
    elif choice == 'Mid-level / Intermediate':
        df = df.loc[df['experience_level'] == 'MI']
    elif choice == 'Executive-level / Director':
        df = df.loc[df['experience_level'] == 'EX']
    elif choice == 'Senior-level / Expert':
        df = df.loc[df['experience_level'] == 'SE']
    
    df_group = df.groupby(['job_title'])['salary_in_usd'].mean()#group by job_title and count an average salary
    series_group = df_group.sort_values(ascending = False).head(3)#determine the top 3 specialists based on the average salary
    df_new = pd.DataFrame({'job_title':series_group.index,
                           'salary_in_usd':series_group.values})#conver series to dataframe 
    x_values = list(df_new['job_title'])
    y_values = list(df_new['salary_in_usd'])
    cm.make_bar_horizontal(x_values, y_values,
                           title="Top 3 salaries from the continent and experience",
                           x_label="Average salary in USD")  
    
def top_5_by_national_composition():
    """
    (None) -> None
    
    """
    df = pd.read_csv(FULL_DATA)#Create data frame
    #Choiceebox of the type of remote ratio
    choice = eg.choicebox(msg='Сhoose the format of the work',
                          title='The first question',
                          choices=['No remote work',
                                   'Partially remote',
                                   'Fully remote'])
    #input processing
    if choice == 'No remote work':
        df = df.loc[df['remote_ratio'] == 0]
    elif choice == 'Partially remote':
        df = df.loc[df['remote_ratio'] == 50]
    elif choice == 'Fully remote':
        df = df.loc[df['remote_ratio'] == 100]
    
    #Choiceebox of the company size
    choice = eg.choicebox(msg='Сhoose the company size',
                          title='The second question',
                          choices=['Large',
                                   'Medium',
                                   'Small'])
    #input processing
    if choice == 'Large':
        df = df.loc[df['company_size'] == 'L']
    elif choice == 'Medium':
        df = df.loc[df['company_size'] == 'M']
    elif choice == 'Small':
        df = df.loc[df['company_size'] == 'S']
        
    employees_residence = df['employee_residence']#Create Series   
    for val in employees_residence:
        #Group by 'employee_residence' and calculate percentage
        top_5_nation = (df.groupby('employee_residence').size() / len(df)) * 100
        #sorted result and take top-5
        top_5_nation = top_5_nation.sort_values(ascending=False)[:5]
        #Count rest percents
        others = round(100 - top_5_nation.sum(), 2)
        #Series to DF with make from Series index name of column DF
        top_5_nation = top_5_nation.reset_index()
        #added the remaining percentages to the column 'employee_residence' in DF 
        top_5_nation.loc[5] = ['Other',others]
    #create multiflow output   
    thread1 = threading.Thread(target=show_message,
                               args=("Decryption of Alphs_2",
                                     list(top_5_nation['employee_residence'])))
    thread2 = threading.Thread(target=cm.custom_make_pi,
                               args=(list(top_5_nation[0]),
                                     list(top_5_nation['employee_residence'])))
    thread2.start()
    thread1.start()

def main():
    """
    (None) -> None
    Create main menu
    """
    while True:
        #tkinter main menu
        #wtk.main_window(CHOICE, title="Select box",lable_text="Data scientice salary")
        pick = eg.indexbox(msg="Data scientice salary",
                           title="Select box",
                           choices=CHOICE,
                           image="images/DS-image.jpg")
        if pick == 0:
            avg_salary_by_type()
        elif pick == 1:
            top_it_jobs_by_continent()
        elif pick == 2:
            top_5_by_national_composition()
        elif pick == 3:
            eg.msgbox(msg="Leaving Data Analytics...",
                      title="Goodbye",
                      image="images/goodbye.jpg")
            break
        
if __name__ == "__main__":
    main()
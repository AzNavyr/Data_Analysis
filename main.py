'''
 @authors: Nataliia Tytovets  
 @date:     09-May-2024
 @project:  teamwork
 @description:  main app
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import easygui as eg
import ds_salaries
#import incomes

def login_procedure():
    """
    (None) -> None
    A kind of authorization in the application.
        login = login,
        password = password
    """
    while True:
        try: 
            fieldValues = eg.multpasswordbox(msg="Enter login and password",
                                             title="Authorization",
                                             fields=["Login", "Password"])
            USERNAME = fieldValues[0]
            PASSWORD = fieldValues[1]
        except: 
            login_procedure()
            exit(0)
            
        if USERNAME.lower() == "login" and PASSWORD.lower() == "password":
            eg.msgbox("Вход выполнен!",
                      image='images/yes.jpg')
            break
        else:
            eg.msgbox("Неверный логин или пароль",
                      image='images/no.jpg')

def main():
    '''
    (None) -> None
    Create main menu for datasets using easygui
    '''
    menu = ["US Crude",
            "DS Salaries",
            "Ecommerce",
            "Obesity",
            "Online Foods",
            "Students",
            "US Incomes",
            "Quit"]
    #login_procedure()
    while True:
        pick= eg.indexbox(msg="Select dataset to analyse",
                          title="Data Analytics",
                          choices=menu, image="images/data_a.png")
        if pick == 0:
            crude_oil.main()
        elif pick == 1:
            ds_salaries.main()
        elif pick == 2:
            ecommerce.main()
        elif pick == 3:
            obesity.main()
        elif pick == 4:
            foods.main()
        elif pick == 5:
            students.main()
        elif pick == 6:
            incomes.main()
        elif pick == 7:
            eg.msgbox(msg="Leaving Data Analytics...",
                      title="Goodbye...",
                      image='images/mainBYE.jpg')
            break

# -- main body
if __name__ == "__main__":
    main()
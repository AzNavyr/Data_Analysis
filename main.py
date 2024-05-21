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
            if USERNAME.lower() == "login" and PASSWORD.lower() == "password":
                eg.msgbox("Entry success!!!",
                          image='images/yes.jpg')
                break
            else:
                eg.msgbox("Invalid login or password",
                          image='images/no.jpg')
        except:
            eg.msgbox("Invalid login or password",
                      image='images/no.jpg')
            exit(0)
    

def main():
    '''
    (None) -> None
    Create main menu for datasets using easygui
    '''
    menu = ["US Crude",
            "DS Salaries",
            "Online Foods",
            "Students",
            "US Incomes",
            "Quit"]
    while True:
        pick= eg.indexbox(msg="Select dataset to analyse",
                          title="Data Analytics",
                          choices=menu, image="images/data_a.png")
        if pick == 0:
            crude_oil.main()
        elif pick == 1:
            ds_salaries.main()
        elif pick == 2:
            onlinefoods.main()
        elif pick == 3:
            students.main()
        elif pick == 4:
            incomes.main()
        elif pick == 5:
            eg.msgbox(msg="Goodbye...",
                      title="Leaving Data Analytics...",
                      image="images/goodbye_main.jpg")
            break
        
login_procedure()

if __name__ == "__main__":
    main()
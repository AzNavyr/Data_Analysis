'''
 @authors: Nataliia Tytovets  
 @date:     09-May-2024
 @project:  teamwork
 @description:  main app
'''
import easygui as eg
from pylint.lint import Run
import ds_salaries
import income
import crude_oil
import students
import onlinefoods


def login_procedure():
    """
    (None) -> None
    A kind of authorization in the application.
        login = login,
        password = password
    """
    while True:
        try:
            field_values = eg.multpasswordbox(msg="Enter login and password",
                                             title="Authorization",
                                             fields=["Login", "Password"])
            username = field_values[0]
            password = field_values[1]
            if username.lower() == "login" and password.lower() == "password":
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
    login_procedure()
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
            income.main()
        elif pick == 5:
            eg.msgbox(msg="Goodbye...",
                      title="Leaving Data Analytics...",
                      image="images/goodbye_main.jpg")
            break

def lint_me():
    '''
    (None) -> None
    This function checks code for errors, using pylint module.
    '''
    print("Checking for lint errors...")
    Run(['helpers.py'])

if __name__ == "__main__":
    #lint_me()
    main()
    
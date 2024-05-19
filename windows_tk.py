'''
 @authors: Enver Osmanov
 @date:     17-May-2024
 @project:  teamwork
 @description:  tkinter windows
'''

import tkinter as tk
import ds_salaries as ds
from PIL import Image, ImageTk

CHOICE = ['View Salary by Job Type',
          'Top 3 IT specialists by continent',
          'Top 3 IT specialists by continent',
          'Exit']

def make_button(win, text, bd=5, bg='#a7dee8', action='green'):
    return tk.Button(win, text=text,
                      command=ds.avg_salary_by_type,
                      activebackground=action,
                      font=('Arial', 9, 'bold'),
                      bd=bd,
                      bg=bg)

def main_window(width=897, height=457, title="", lable_text=""):
    """
    (None) -> None
    """
    win = tk.Tk()
    win.title(title)
    pic = tk.PhotoImage(file="images/icon.png")
    win.iconphoto(False, pic)
    win.geometry(f'{width}x{height}+600+300')
    win.resizable(False,False)
    pic_label = tk.PhotoImage(file="images/DS-image_other.png")
    # widget Labels
    lable_text = tk.Label(win,
                       text=lable_text,
                       anchor=tk.CENTER,
                       justify=tk.CENTER,
                       font=('Arial', 20, 'bold')).grid(column=0, row=0,
                                                        columnspan=20,
                                                        padx=12,
                                                        pady=12)
    lable_pic = tk.Label(win,
                       image=pic_label).grid(column=0, row=2,
                                             columnspan=20,
                                             padx=150,
                                             pady=7)
    #widget Buttons
    btn_1 = make_button(win, CHOICE[0]).grid(row=8,
                                        column=0,
                                        stick="wnes",
                                        padx=25,
                                        pady=5)
    
    btn_2 = make_button(win, CHOICE[1]).grid(row=8,
                                        column=2,
                                        stick="wnes",
                                        padx=25,
                                        pady=5)
    
    btn_3 = make_button(win, CHOICE[2]).grid(row=8,
                                            column=3,
                                            stick="wnes",
                                            padx=25,
                                            pady=5)
    
    btn_4 = make_button(win, CHOICE[3], action='red').grid(row=8,
                                                           column=4,
                                                           stick="wnes",
                                                           padx=25,
                                                           pady=5) 
    
    #cal = tk.Entry()
    #cal.grid(row=0, column=0)
    #btn_1.grid(row=4,column=3)
    #btn_2.grid(row=70,column=1)
    #btn_3.grid(row=70,column=2)
    #btn_4.grid(row=70,column=3)
    #win.grid_columnconfigure(1, weight=1)
    
    win.mainloop()


if __name__ == "__main__":
    main_window(title="Select box",lable_text="Data scientice salary")
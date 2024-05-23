'''
 @authors: Enver Osmanov
 @date:     17-May-2024
 @project:  teamwork
 @description:  tkinter windows
'''

import tkinter as tk
import ds_salaries as ds
import main
import webbrowser
import os

def make_button(win, text, command, bd=5, bg='#a7dee8', action='green'):
    return tk.Button(win, text=text,
                      command=lambda: command(),
                      activebackground=action,
                      font=('Arial', 9, 'bold'),
                      bd=bd,
                      bg=bg)

def close_win():
    """
    (None) -> None
    Func just close the window
    """
    os._exit(0)

def main_window(CHOICE, width=897, height=457, title="", lable_text=""):
    """
    (None) -> None
    """
    win = tk.Tk()
    win.title(title)
    win.configure(bg="#8BF6F2")
    pic = tk.PhotoImage(file="images/icon.png")
    win.iconphoto(False, pic)
    win.geometry(f'{width}x{height}+600+300')
    #win.resizable(False,False)
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
    btn_1 = make_button(win, CHOICE[0], command=ds.avg_salary_by_type).grid(row=20,
                                                                            column=0,
                                                                            stick="wnes",
                                                                            padx=25,
                                                                            pady=5)
    
    btn_2 = make_button(win, CHOICE[1], command=ds.top_jobs_by_continent).grid(row=20,
                                                                                  column=2,
                                                                                  stick="wnes",
                                                                                  padx=25,
                                                                                  pady=5)
    
    btn_3 = make_button(win, CHOICE[2], command=ds.top_5_by_national_composition).grid(row=20,
                                                                  column=3,
                                                                  stick="wnes",
                                                                  padx=25,
                                                                  pady=5)
    
    btn_4 = make_button(win, CHOICE[3], command=close_win, action='red').grid(row=20,
                                                                           column=5,
                                                                           stick="wnes",
                                                                           padx=25,
                                                                           pady=5)
    
#     btn_5 = make_button(win, text="Open Flowchart", command=open_flowchart_url).grid(row=8,
#                                                                            column=4,
#                                                                            stick="wnes",
#                                                                            padx=25,
#                                                                            pady=5)
    win.mainloop()

def open_flowchart_url():
    url = "https://app.diagrams.net/#G1_lWHB0DNhZ9E4qiBRdEYsZPMpm5hZf5G#%7B%22pageId%22%3A%22ZMWebayZMQBc8PB5ZtUZ%22%7D"
    webbrowser.open_new(url)

if __name__ == "__main__":
    pass
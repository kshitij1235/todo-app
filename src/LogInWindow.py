"""
Login window for the application
"""

import tkinter as tk
from application_lib import titlebar, rgbtohex,refresh_temp,check_username_and_password,get_tasks
import customtkinter
from RegisterWindow import Regsiter_window
from Todowindow import Todo_window

class LoginWindow:
    def __init__(self, master):
        super().__init__()

        # setting up the basic config for the application 
        # window 
        self.img = tk.PhotoImage(file='src/content/Login.png')
        self.close_icon = tk.PhotoImage(file='src/content/close.png')
        master.geometry('720x520')
        master.configure(bg=rgbtohex(43, 46, 40))
        master.overrideredirect(True)
        master.attributes("-topmost", True)
        titlebar(master, self.close_icon)

        label1 = tk.Label(master,
                        image=self.img,
                        borderwidth=0, 
                        highlightthickness=0)

        label1.pack()

        entry = customtkinter.CTkEntry(master=master,
                                       width=200,
                                       placeholder_text="Username")
        entry.place(x=270, y=240)

        entry2 = customtkinter.CTkEntry(master=master,
                                        width=200,
                                        placeholder_text="Password",
                                        show="*")
        entry2.place(x=270, y=290)
        check_1 = tk.IntVar()
        check_box_1 = customtkinter.CTkCheckBox(master=master,
                                               text="Keep me signed in",
                                               width=15,
                                               height=15,
                                               variable=check_1)
        check_box_1.place(x=270, y=330)
        
        # self.radio_button_1.select()


        button_2 = customtkinter.CTkButton(master=master,
                                          text="Login now",
                                          width=200,
                                          fg_color=rgbtohex(63, 139, 254),
                                          command=lambda username=entry,password=entry2,args=check_1,warning_=master,arg2=master:submit(username,password,args,warning_,arg2)
                                          )
        button_2.place(x=270, y=360)

        register = tk.Label(master,
                           text="Register", 
                           bg=rgbtohex(34, 36, 40), 
                           fg="white", 
                           borderwidth=0)

        register.place(x=295, y=424)
        register.bind("<Button-1>", lambda event , arg=master : open_register(event,arg))

def open_register(e,root):
    """
    switch the regsiter screen
    """
    root.destroy()
    Regsiter_window(tk.Tk())


def submit(username,password,a,warning,master):
    """
    submit and start the todo app with
    login
    """
    user=str(username.get())
    pass_=str(password.get())
    if check_username_and_password(user,pass_):
        if a.get()==1:
            refresh_temp(user,pass_)
        master.destroy()
        data=get_tasks(user)
        Todo_window(tk.Tk(),user,data)
    else:
        warning_label = tk.Label(warning,
                        text="*/username or password incorrect/*",
                        bg=rgbtohex(34, 36, 40),
                        fg="red",
                        font=("",9,'italic'))
        warning_label.place(x=270, y=400)



def Login_window(root):
    app=LoginWindow(root)
    root.mainloop()

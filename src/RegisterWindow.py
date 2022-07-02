"""
sign up page for the application
"""

from tkinter import *
import tkinter as tk
import tkinter
from application_lib import titlebar, rgbtohex,add_users,check_for_user
import customtkinter


class LoginWindow:
    def __init__(self, master):
        super().__init__()

        # settting up the basic settings of the applications 
        
        self.img = tk.PhotoImage(file='src/content/Register.png')
        self.close_icon = tk.PhotoImage(file='src/content/close.png')
        master.geometry('720x520')
        master.configure(bg=rgbtohex(43, 46, 40))
        master.overrideredirect(True)
        titlebar(master, self.close_icon)

        label1 = tk.Label(master, image=self.img,
                          borderwidth=0, highlightthickness=0)
        label1.pack()

        # =====username password entry=====

        username = customtkinter.CTkEntry(master=master,
                                       width=200,
                                       placeholder_text="Username")
        username.place(x=270, y=240)

        password = customtkinter.CTkEntry(master=master,
                                        width=200,
                                        placeholder_text="Password",
                                        show="*")
        password.place(x=270, y=300)

        button_2 = customtkinter.CTkButton(master=master,
                                            text="Register now",
                                            width=200,
                                            fg_color=rgbtohex(63, 139, 254),
                                            command = lambda user=username,pass_=password: register_users(user,pass_)
                                           )
        button_2.place(x=270, y=360)

        register = tk.Label(master, text="Login", bg=rgbtohex(
            34, 36, 40), fg="white", borderwidth=0)

        register.place(x=300, y=424)
        register.bind("<Button-1>", lambda event,args=master:open_login(event,args))


def open_login(e,master):
    """
    Login window
    """
    from LogInWindow import Login_window
    
    # switiching to the login window 
    master.destroy()
    Login_window(tkinter.Tk())

def Regsiter_window(root):
    """
    start the register window
    """
    app=LoginWindow(root)
    root.mainloop()

def register_users(username,password):
    """
    resiter the user in the 
    database
    """
    user=username.get()
    pass_=password.get()
    
    # get username and pass 
    # and register in the database(todousers)
    
    if not check_for_user('todousers',user):
        add_users('todousers',user,pass_)
        

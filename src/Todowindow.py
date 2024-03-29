"""
This app window is the main application file

"""
import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import customtkinter
from application_lib import rgbtohex,regular_quitter
from application_lib import render_todo,titlebar
from application_lib import add_task,refresh_tasks

global frames

frames = []

class TodoApp:
    def __init__(self, master,username,data):
        super().__init__()
        # initalize the applicatin settings s
        self.user = tkinter.PhotoImage(file='src/content/user.png')
        master.title(f"todo : {username}")
        master.geometry("780x520") 
        master.protocol("WM_DELETE_WINDOW",lambda args=master:regular_quitter(args))
        master.config(bg=rgbtohex(33,35,37))

        # # ============ create two frames ============
        # configure grid layout (2x1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        frame_left = customtkinter.CTkFrame(master=master,
                                                 width=180,
                                                 corner_radius=0)
        frame_left.grid(row=0, column=0, sticky="nswe")

        v = Scrollbar(master)
        v.grid(row=0, column=1, sticky='nse')

        frame_right = customtkinter.CTkFrame(master)
        frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    


        # # ============ frame_left ============
        frame_left.grid_rowconfigure(0, minsize=10)
        frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        frame_left.grid_rowconfigure(8, minsize=20)
        frame_left.grid_rowconfigure(11, minsize=10)

        label_1 = customtkinter.CTkLabel(master=frame_left,
                                              image=self.user,text=""
                                              )
        label_1.grid(row=1, column=0, pady=10, padx=10)

        label_1 = customtkinter.CTkLabel(master=frame_left,
                                              text=username)  # font name and size in px
        label_1.grid(row=2, column=0, pady=10, padx=10)

        button_2 = customtkinter.CTkButton(master=frame_left,
                                                text="Logout",
                                                fg_color=("gray75", "gray30"),
                                                command=lambda arg=master :logout_todo(arg)
                                                )
        button_2.grid(row=3, column=0, pady=10, padx=20)

        switch_2 = customtkinter.CTkSwitch(master=frame_left,
                                                text="Dark Mode",
                                                )
        switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        entry = customtkinter.CTkEntry(master=master,
                                       width=450)
        entry.grid(row=10, column=1, pady=10, padx=20, sticky="w")


        frames=render_todo(frame_right,data,username)

        button_2 = customtkinter.CTkButton(master=master,
                                          text="Add",
                                          width=100,
                                          fg_color=rgbtohex(63, 139, 254),
                                          command=lambda Username=username,
                                          Task_text_box=entry,
                                          Frame_right=frame_right,
                                          new_data=data,
                                          Previous_frames=frames:add_task(Username,Task_text_box,Frame_right,new_data,Previous_frames)
                                          )
        button_2.grid(row=10, column=1, pady=10, padx=15, sticky="e")


        frames = refresh_tasks(frames,frame_right=frame_right,data=data,username=username)

        switch_2.select()
        
        # switch between light and darkmode
        import threading
        t1=threading.Thread(target=lambda switch=switch_2 ,master = master: checks(switch,master),daemon=True)
        t1.start()

        master.protocol("WM_DELETE_WINDOW",lambda app=master: regular_quitter(app))

def checks(switch_2,master):
    from time import sleep
    while True:    
        change_mode(switch_2,master)
        sleep(1)

def change_mode(switch_2,master):
    """
    Light mode and dark mode
    """
    if switch_2.get() == 1:
        customtkinter.set_appearance_mode("dark")
    else:
        customtkinter.set_appearance_mode("light")
        master.config(bg=rgbtohex(120, 120, 120))

def Todo_window(root,username,data):
    """
    runs the todo window
    """
    app = TodoApp(root,username,data)
    root.mainloop()


def logout_todo(master):
    """
    log out from the current account 
    """
    
    import tkinter as tk
    from application_lib.database import refresh_temp
    from LogInWindow import Login_window

    # make changes in the recent login txt file 
    # and destroy the application 
    refresh_temp(None, None)
    master.destroy()
    Login_window(tk.Tk())

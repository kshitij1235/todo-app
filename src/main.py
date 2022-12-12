"""
main file that manage 
the whole application
"""
import tkinter as tk
from LogInWindow import Login_window 
from json_txt import extract_values,load_txt
from Todowindow import Todo_window
from RegisterWindow import Regsiter_window
from application_lib.database import check_for_user,no_users,get_tasks

# get the recent rembered login 
Meta = extract_values(load_txt('recent_login.txt'))
username=Meta[0]
password=Meta[1]

# if no user exists then register 
if not no_users('todousers'):
    Regsiter_window(tk.Tk())

# is no one is rembered in recent than let them log in
elif username=='None' and password=='None':
    Login_window(tk.Tk())

# is user is rembered then launch the app 
elif check_for_user('todousers', username):
    data=get_tasks(username)
    Todo_window(tk.Tk(),username,data)

# if exception occurs then too launch the login screen 
else:
    Login_window(tk.Tk())







		

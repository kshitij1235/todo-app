from boxdb import *
from boxdb.support import get_elements
from application_lib.todo_handler import render_todo, render_todo,render_specific_todo
from tkinter import END
from application_lib.setting import *

def add_users(table_name,username,password):
    add_row(database_name,table_name,[username,password])
    create_table(database_name,{'name':username})
    create_column(database_name,username,['task'],
                  primary_key=True,
                  data_type="str")
    create_column(database_name,username,['data','status'],data_type="str")

def refresh_temp(username,password):
    from json_txt import edit_data
    edit_data("recent_login.txt",'username',username)
    edit_data("recent_login.txt",'password',password)

def check_for_user(table_name,username):return chech_rows(database_name,
                                                        table_name,
                                                        'username',
                                                        username)

def no_users(table_name):return empty_table(database_name,table_name)


def check_username_and_password(username,password):
    return specific_auth(database_name,
                        user_table,
                        ["username","password"],
                        [username,password])

def remove_task(table_name,data):
    return remove_row(database_name,table_name,data)

def get_tasks(user):return get_elements(database_name,user,'task')

def add_task(user,task,frame_right,previous_tasks,frames):
    from application_lib import refresh_tasks
    from datetime import date

    # if len(task.get()) == 0 :
    
    #     print("wrong task")
    #     return
    
    # add data to database
    today = str(date.today())
    if add_row(database_name,user,[task.get(),today,"False"]):

        # create new sets of frame 
        frame_new=render_specific_todo(frame_right,task.get(),user,len(frames))
        frames.append(frame_new)
        
        # previous_tasks.append(task.get())
        # frames=render_todo(frame_right,previous_tasks,user)

    task.delete(0,END)

    
    refresh_tasks(frames,frame_right=frame_right,
                  data=previous_tasks,username=user)

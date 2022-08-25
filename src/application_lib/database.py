from boxdb import *
from boxdb.support import get_elements
from application_lib.todo_handler import render_todo, render_todo
def add_users(table_name,username,password):
    add_row(table_name,[username,password])
    create_project({'name':username})
    create_column(username,['task'],primary_key=True)
    create_column(username,['data','status'])

def refresh_temp(username,password):
    from json_txt import edit_data
    edit_data("recent_login.txt",'username',username)
    edit_data("recent_login.txt",'password',password)

def check_for_user(table_name,username):return chech_rows(table_name,'username',username)

def no_users(table_name):return empty_table(table_name)


def check_username_and_password(username,password):return auth_details('todousers',[username,password])

def remove_task(table_name,data):
    print(table_name,data)
    remove_row(table_name,"task",data)

def get_tasks(user):return get_elements(user,'task')

def add_task(user,task,frame_right,data):
    from datetime import date
    today = date.today()
    add_row(user,[task.get(),today,"False"])
    data.append(task.get())
    render_todo(frame_right,data,user)
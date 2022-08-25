from concurrent.futures import thread
import sys
import tkinter as tk
from application_lib.database import remove_task
from application_lib.todo_handler import render_todo

def quitter(e, master):
    master.destroy()
    sys.exit()

def regular_quitter(master,threading):
    master.destroy()
    sys.exit("quitting")


def button_event(button__,frames,data,frame_ava,user):
    if button__ in frames:
        target=data[frames.index(button__)]
        print(target)
        remove_task(user,target)
        button__.destroy()

    data.remove(data[frames.index(button__)])
    frames.remove(button__)
    if data == []:
        from application_lib import rgbtohex
        label_info_1 = tk.Label(master=frame_ava,
                            text="TODO is Empty",
                            font=("Roboto",20,"bold"),
                            bg=rgbtohex(42, 45,46),
                            fg="White"
                            )
        label_info_1.grid(
            column=1, row=3, sticky="nw", padx=0, pady=0)

    return data


def refresh_tasks(frames,
frame_right,
data,
username,
new_value):

    for i in frames:
        i.destroy()
        
    if new_value !="":
        data.append(new_value)

    render_todo(frame_right,
    data,
    username)
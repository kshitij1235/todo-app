from concurrent.futures import thread
import sys
import tkinter as tk
from application_lib.database import remove_task
from application_lib.todo_handler import render_todo

def quitter(e, master):
    master.destroy()
    sys.exit()

def regular_quitter(master):
    master.destroy()
    sys.exit("quitting")

#FIXME cannot get the rigth values

def button_event(button__,frames,data,frame_ava,user):
    
    if isinstance(data,str):
        if button__ in frames:
            if remove_task(user,data): 
                button__.destroy()  
                frames.remove(button__)

    
    if button__ in frames:
        target=data[frames.index(button__)]
        if remove_task(user,target): 
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
username):
    cleaned = [item for item in frames if not isinstance(item,list)]
    for i in cleaned:
        i.destroy()
    
    render_todo(frame_right,
    data,
    username)
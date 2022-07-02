
import tkinter as tk
from application_lib.app_movement import move_app
from application_lib.color_manager import rgbtohex
from application_lib.app_handler import quitter

def titlebar(master,close_icon):
    title_bar = tk.Frame(master, background="grey", relief="raised",
                                 bd=0, bg=rgbtohex(r=53, b=50, g=50))
    title_bar.pack(expand=1,fill=tk.X)
    title_bar.bind("<B1-Motion>", lambda event, arg=master:move_app(event, arg))
    app_name = tk.Label(title_bar, text="Login",
                        bg=rgbtohex(r=53,b=50,g=50), foreground="white")
    app_name.pack(side=tk.LEFT,pady=2,padx=5)
    close = tk.Label(title_bar, image=close_icon,
                     bg=rgbtohex(r=53, b=50, g=50))
    close.pack(side=tk.RIGHT)
    close.bind("<Button-1>",lambda event,arg=master:quitter(event,arg))   
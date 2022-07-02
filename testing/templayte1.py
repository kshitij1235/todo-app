import tkinter as tk
import customtkinter


class Music:
    def holy(master):

        box = []

        img = tk.PhotoImage(file='src/content/Login.png')



        label1 = tk.Label(master,
                          image=img,
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
                                           )
        button_2.place(x=270, y=360)

        register = tk.Label(master,
                            text="Register",
                            fg="white",
                            borderwidth=0)

        register.place(x=295, y=424)

        box.append(label1)
        box.append(entry)
        box.append(entry2)
        box.append(check_box_1)
        box.append(button_2)
        print(box)
        return box


def grab_music(master):
    return Music.holy(master=master)

import customtkinter

def render_todo(frame_right,data,username):
    from application_lib.app_handler import button_event
    frames=[]
    for i in range(len(data)):
        frame_info = customtkinter.CTkFrame(master=frame_right, height=10)
        frames.append(frame_info)

        frame_info.grid(row=i, column=0, columnspan=2,
                        rowspan=1, pady=5, padx=2, sticky="nsew")
        label_info_1 = customtkinter.CTkLabel(master=frame_info,
                                              text=data[i],
                                              )
        label_info_1.grid(
            column=0, row=0, sticky="nw", padx=10, pady=10)

        button_3 = customtkinter.CTkButton(master=frame_info,
                                           text="Delete",
                                           fg_color=("gray30"),
                                           command=lambda args=frame_info,arg2=frames,arg3=data,arg5=frame_right ,arg6=username: button_event(args,arg2,arg3,frame_ava=arg5,user=arg6))
        button_3.grid(row=0, column=10, pady=15, padx=10)
    return frames




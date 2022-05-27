from dataclasses import dataclass
from tkinter import *


@dataclass
class CallMeRequest:
    sender: str


def call_me_handler(request: CallMeRequest):
    win = Tk()

    var = f"{request.sender} Cię woła!"

    win.config(bg="#EB3A53")

    #textvariable - zmienna do tekstu
    label= Label(win, text = var, font=('Roman',70), justify=CENTER, background="#EB3A53", foreground='#2FEBC0')
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    submit_button = Button(win, text = " Japaelo ", font=('Roman',40), justify=CENTER, background="#8FEB46", foreground='#189E80', command=win.destroy)
    submit_button.place(relx=0.5, rely=0.7, anchor=CENTER)
    submit_button.config(cursor="dot")

    # Create a fullscreen window
    win.attributes('-fullscreen', True)

    win.mainloop()

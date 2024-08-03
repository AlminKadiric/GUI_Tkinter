from tkinter import *
from tkinter import messagebox
 
def confirm_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
 
window = Tk()
Label = Label( window, text="Click here")
Label.pack()
window.protocol("WM_DELETE_WINDOW", confirm_exit) 
window.mainloop()
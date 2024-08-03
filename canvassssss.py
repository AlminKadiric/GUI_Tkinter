from tkinter import *

window = Tk()
window.title("Canvas")
tk_canvas = Canvas(window,width=300,height=300)
tk_canvas.create_line(10,20,200,10)
tk_canvas.pack()
window.mainloop()
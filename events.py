from tkinter import *
def mouse_scroll(event):
    print("Mouse event at x={}, y={}".format(event.x, event.y))
    print("Event source widget: {}".format(event.widget))
    print("Event type: {}".format(event.type))
 
window = Tk()
label = Label(window, text="Click here")
label.pack()
label.bind( "<MouseWheel>", mouse_scroll)
window.mainloop()

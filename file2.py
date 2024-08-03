import tkinter as tk
  
win = tk.Tk()
win.minsize(300, 100)
 
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=2)
  
l1=tk.Label(win,text = 'label1', bg = 'green')
l1.grid(column=0,row=0)
l2=tk.Label(win,text = 'label2',bg = 'red')
l2.grid(column=0,row=1)
win.mainloop()
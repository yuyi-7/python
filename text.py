from tkinter import *

def func(event):
    xin = Tk()
    xin.wm_title('Message')
    t = e.get()
    g = 'Hello,%s' % t
    w1 = Label(xin, text = g)
    w1.pack()
    xin.mainloop()
root = Tk()
root.wm_title('Hello World')
e = Entry(root)
e.pack()
b1 = Button(root, text = 'Hello')
b1.bind('<Button-1>', func)
b1.pack()
root.mainloop()
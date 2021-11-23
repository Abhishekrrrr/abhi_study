from tkinter import *
root=Tk()
def fun():
    print("clicked")
Button(root,text="ok",command=fun).pack()
root.mainloop()
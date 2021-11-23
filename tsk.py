from tkinter import *
root=Tk()
def fun1():
    print("file clicked")

def fun2():
        print("new project clicked")


def fun3():
    print("new clicked")


def fun4():
    print("new starch clicked")


def fun5():
    print("new 3 clicked")


def fun6():
    print("undo")


def fun7():
    print("redo")


def fun8():
    print("cut clicked")


def fun8():
    print("class clicked")


def fun9():
    print("file clicked")


def fun10():
    print("symbol clicked")


def fun11():
    print("column clicked")


def fun12():
    print("next clicked")


mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu,command=fun1)
submenu.add_command(label="new projcet",command=fun2)
submenu.add_command(label="new",command=fun3)
submenu.add_separator()
submenu.add_command(label="new scartch file",command=fun3)
submenu.add_command(label="open",command=fun4)
submenu.add_command(label="save as",command=fun5)
submenu.add_command(label="exit",command=root.quit)

edit = Menu(mymenu)
mymenu.add_cascade(label="edit",menu=edit)
edit.add_command(label="undo",command=fun6)
edit.add_command(label="redo",command=fun7)
edit.add_separator()
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="paste")

navigate = Menu(mymenu)
mymenu.add_cascade(label="navigate",menu=navigate)
navigate.add_command(label="class",command=fun8)
navigate.add_command(label="file",command=fun9)
navigate.add_separator()
navigate.add_command(label="symbol",command=fun10)
navigate.add_command(label="column",command=fun11)
navigate.add_command(label="next line",command=fun12)

root.mainloop()


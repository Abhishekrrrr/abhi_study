import parser
from tkinter import *
root=Tk()
root.title("Calculator")
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
#GET user info
i=0
def get_vari(num):
    global i
    display.insert(i,num)
    i+=1


def clear_all():
    display.delete(0,END)

def undo():
    entir_str=display.get()
    if len(entir_str):
        new_str=entir_str[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"error")
def get_ops(opr):
    global i
    length=len(opr)
    display.insert(i,opr)
    i+=length
def cal():
    entir_str=display.get()
    try:
        a=parser.expr(entir_str).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except:
        clear_all()
        display.insert(0,"error")




#addbutton
Button(root,text="1",command=lambda :get_vari(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :get_vari(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :get_vari(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda :get_vari(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_vari(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_vari(6)).grid(row=3,column=2)
Button(root,text="7",command=lambda :get_vari(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :get_vari(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :get_vari(9)).grid(row=4,column=2)
Button(root,text="0",command=lambda :get_vari(0)).grid(row=5,column=0)
Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=1)
Button(root,text="=",command=lambda :cal()).grid(row=5,column=2)
Button(root,text="->",command=lambda :undo()).grid(row=2,column=3)
Button(root,text="+",command=lambda :get_ops('+')).grid(row=3,column=3)
Button(root,text="-",command=lambda :get_ops('_')).grid(row=4,column=3)
Button(root,text="*",command=lambda :get_ops('*3.14')).grid(row=5,column=3)
Button(root,text="/",command=lambda :get_ops('/')).grid(row=2,column=4)
Button(root,text="PI",command=lambda :get_ops('PI')).grid(row=3,column=4)
Button(root,text="%",command=lambda :get_ops('%')).grid(row=4,column=4)
Button(root,text="(",command=lambda :get_ops('(')).grid(row=5,column=4)
Button(root,text=")",command=lambda :get_ops(')')).grid(row=2,column=5)
Button(root,text="EXP",command=lambda :get_ops("**")).grid(row=3,column=5)
Button(root,text="X!").grid(row=4,column=5)
Button(root,text="^2",command=lambda :get_ops('**2')).grid(row=5,column=5)
root.mainloop()
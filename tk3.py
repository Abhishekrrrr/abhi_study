from tkinter import*
root=Tk()
l1=Label(root,text="user name")
l2=Label(root,text="mobile number")
l3=Label(root,text="email")
l4=Label(root,text="password")
l5=Label(root,text="password again")

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
l4.grid(row=3,column=0)
l5.grid(row=4,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
e4.grid(row=3,column=1)
e5.grid(row=4,column=1)



Button(root,text="login").grid(row=5,column=0)
Button(root,text="cancel").grid(row=5,column=1)

root.mainloop()
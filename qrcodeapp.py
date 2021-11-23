from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root=Tk()
def qrr():
    linkname=name_en.get()
    link=linen.get()
    file_name=linkname + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    if len(linkname.get()) != 0:
        global qr, img
        qr = pyqrcode.create(linkname.get())
        img = BitmapImage(data=qr.xbm(scale=8))







canvas=Canvas(root,width=600,height=600)
canvas.pack()
aa=Label(root,text="QRCODE GENATARIOR",fg="red",font=('Arial',30))
canvas.create_window(200,50,window=aa)
namelb=Label(root,text="LINK NAME")
linklb=Label(root,text="LINK")

canvas.create_window(200,100,window=namelb)
canvas.create_window(200,150,window=linklb)
name_en=Entry(root)
linen=Entry(root)


canvas.create_window(200,130,window=name_en)
canvas.create_window(200,180,window=linen)

bt=Button(text="QRCODE",command=qrr)
canvas.create_window(200,210,window=bt)



root.mainloop()


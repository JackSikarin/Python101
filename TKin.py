from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI=Tk()#หน้าจอหลัก
GUI.title('โปรแกรมบันทึกการกิน')#ชื่อโปรแกรม
GUI.geometry('450x550')#ขนาดหน้าจอ

def But1():
    text= 'กินบ๊ะกุดเต๋'
    messagebox.showinfo('มื้อเข้า',text)

FB1=Frame(GUI)#กรอบย้ายได้
FB1.place(x=100,y=50)
B1=ttk.Button(FB1,text='ตอนเช้ากินอะไร',command=But1)
B1.pack(ipadx=20,ipady=20)


def But2():
    text= 'กินข้าวหมูเกาหลี'
    messagebox.showinfo('มื้อเที่ยง',text)

FB2=Frame(GUI)
FB2.place(x=100,y=150)
B2=ttk.Button(FB2,text='ตอนเที่ยงกินอะไร',command=But2)
B2.pack(ipadx=20,ipady=20)


def But3():
    text= 'กินบุฟเฟ่เนื้อย่าง'
    messagebox.showinfo('มื้อเย็น',text)

FB3=Frame(GUI)
FB3.place(x=100,y=250)
B3=ttk.Button(FB3,text='ตอนเย็นกินอะไร',command=But3)
B3.pack(ipadx=20,ipady=20)


def But4():
    text= 'อย่างงี้ไม่อ้วนไหวเหรอ'
    messagebox.showwarning('ยังจะแดกอีกเหรอ',text)

FB4=Frame(GUI)
FB4.place(x=100,y=350)
B4=ttk.Button(FB4,text='ก่อนนอนกินอะไร',command=But4)
B4.pack(ipadx=20,ipady=20)


GUI.mainloop()


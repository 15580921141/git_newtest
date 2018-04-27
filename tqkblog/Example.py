#coding:utf-8
# from tkinter import *
#
# window=Tk()
# window.title('hehe')
# def click():
# 	print('ww')
# Button(window, text="设置command事件调用命令", fg="blue",bd=2,width=28,command=click).pack()
# window.mainloop()

from tkinter import *
import tkinter.messagebox

# root = Tk()
# root.title("Button Test")
# def callback():
#     # tkinter.messagebox.showinfo("Python command","人生苦短、我用Python")
#     tkinter.messagebox.askokcancel('名字','python')
# Button(root, text="设置command事件调用命令", fg="blue",bd=2,width=28,command=callback).pack()
# root.mainloop()

root=Tk()
root.title('输入框窗口:')
root.geometry('300x300')
title1=Label(root,text='窗口一：')
title1.pack()
xls_text=StringVar()
xls_text.set('')
xls=Entry(root,textvariable=xls_text)
xls.pack()
def Run():
	x=xls_text.get()
	tkinter.messagebox.showinfo('Click',x)

def answer():
    tkinter.messagebox.showerror("Answer", "Sorry, no answer available")

def callback():
    if tkinter.messagebox.askyesno('Verify', 'Really quit?'):
	    quit()
        # tkinter.messagebox.showwarning('Yes', 'Not yet implemented')

    else:
        tkinter.messagebox.showinfo('No', 'Quit has been cancelled')

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
Button(root,text='Run',command=Run).pack()
mainloop()
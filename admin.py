from tkinter import messagebox
from tkinter import*
import mysql.connector

root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='black')


lbl_password = Label(root,  bg='black', fg='green', text='Administrator Login Page')
lbl_password.place(x=50, y=50, width=300)

lbl_password = Label(root,  bg='black', fg='white', text='Enter Password')
lbl_password.place(x=150, y=100)

password = Entry(root, width=45)
password.place(x=140, y=150, width=120)

reg_btn = Button(root, text='Login', bg='green', fg='white', command='')
reg_btn.place(x=160, y=200, width=80)

root.mainloop()



from tkinter import messagebox
from tkinter import*
import mysql.connector

root = Tk()
root.title('Lifechoices Online')
root.geometry('600x500')
root.configure(bg='black')

lbl_register = Label(root,  bg='black', fg='green', text='Register',)
lbl_register.place(x=280, y=50)

lbl_fullname = Label(root,  bg='black', fg='white', text='Full Name',)
lbl_fullname.place(x=200, y=100)

fullname = Entry(root, width=45)
fullname.place(x=300, y=100, width=120)

lbl_id = Label(root,  bg='black', fg='white', text='ID Number',)
lbl_id.place(x=200, y=140)

id = Entry(root, width=45)
id.place(x=300, y=140, width=120)

lbl_password = Label(root,  bg='black', fg='white', text='Password',)
lbl_password.place(x=200, y=180)

password = Entry(root, width=45)
password.place(x=300, y=180, width=120)

lbl_username = Label(root,  bg='black', fg='white', text='Username',)
lbl_username.place(x=200, y=220)

username = Entry(root, width=45)
username.place(x=300, y=220, width=120)

reg_btn = Button(root, text='Submit', bg='green', fg='white', command='')
reg_btn.place(x=280, y=300, width=80)

root.mainloop()





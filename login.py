from tkinter import messagebox
from tkinter import*
import mysql.connector

root = Tk()
root.title('Lifechoices Online')
root.geometry('600x600')  
root.configure(bg='black')
photo = PhotoImage(file="logo.png")
w = Label(root, image=photo, width=200, height=150)
w.pack()

lbl_password = Label(root,  bg='black', fg='white', text='Enter Password',)
lbl_password.place(x=200, y=300)

password = Entry(root, width=45)
password.place(x=300, y=300, width=100)

lbl_username = Label(root, bg='black', fg='white', text='Enter Username',)
lbl_username.place(x=200, y=200)

username = Entry(root, width=45)
username.place(x=300, y=200, width=100)

login_btn = Button(root, text='Login', bg='green', fg='white', command='')
login_btn.place(x=250, y=400, width=55)

reg_btn = Button(root, text='Register', bg='green', fg='white', command='')
reg_btn.place(x=320, y=400, width=55)

admin_btn = Button(root, text='Admin', bg='white', fg='black', command='')
admin_btn.place(x=250, y=450, width=125)

root.mainloop()

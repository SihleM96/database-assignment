from tkinter import messagebox
from tkinter import *
import mysql.connector
import pymysql.cursors
import datetime
import os
import time

# Connect Database
mydb = mysql.connector.connect(host="127.0.0.1",
                                user="lifechoices",
                                password="@Lifechoices1234",
                                database="lifechoicesonline", auth_plugin="mysql_native_password")
my_cursor = mydb.cursor()


def verify():
    fullname1 = fullname.get()
    id1 = id_no.get()
    password1 = password.get()
    username1 = username.get()

    sql = "INSERT INTO users VALUES (%s, %s,%s, %s)"
    val = [id1, fullname1,username1, password1]
    my_cursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("REGISTRATION MESSAGE", "USER REGISTERED SUCCESSFULLY")

# listbox function


def get_all():

    my_cursor.execute("Select * from users")
    for i in my_cursor:
     listbox.insert(END, i)


def clear_all():

    listbox.delete(0, END)

# Interface


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x600')
root.configure(bg='grey8')

lbl_register = Label(root, bg='grey8', fg='green yellow', text='Register', )
lbl_register.place(x=280, y=50)

lbl_id = Label(root, bg='grey8', fg='white', text='ID Number')
lbl_id.place(x=200, y=100)

id_no = Entry(root, width=45)
id_no.place(x=300, y=100, width=120)

lbl_fullname = Label(root, bg='grey8', fg='white', text='Full Name', )
lbl_fullname.place(x=200, y=140)

fullname = Entry(root, width=45)
fullname.place(x=300, y=140, width=120)

lbl_password = Label(root, bg='grey8', fg='white', text='Password', )
lbl_password.place(x=200, y=220)

lbl_username = Label(root, bg='grey8', fg='white', text='Username', )
lbl_username.place(x=200, y=180)

username = Entry(root, width=45)
username.place(x=300, y=180, width=120)

password = Entry(root, width=45)
password.place(x=300, y=220, width=120)

log_btn = Button(root, text='Submit', bg='green yellow', fg='grey8', command=verify)
log_btn.place(x=280, y=260, width=80)

listbox = Listbox(root, width=40, height=10)
listbox.place(x=160, y=300)

# listbox button

getlist_btn = Button(root, text='View List', bg='green yellow', fg='grey8', command=get_all)
getlist_btn.place(x=220, y=500, width=80)

getlist_btn = Button(root, text='Clear List', bg='green yellow', fg='grey8', command=clear_all)
getlist_btn.place(x=340, y=500, width=80)


root.mainloop()




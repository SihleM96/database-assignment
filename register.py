from tkinter import messagebox
from tkinter import *
import mysql.connector
import pymysql.cursors
import datetime
import os
import time

# Connect Database
mydb= mysql.connector.connect(host="127.0.0.1",
                                      user="lifechoices",
                                      password="@Lifechoices1234",
                                      database="lifechoicesonline", auth_plugin="mysql_native_password")
my_cursor = mydb.cursor()


def insertdb():
    fullname1 = fullname.get()
    id1 = id_no.get()
    password1 = password.get()
    username1 = username.get()

    sql = "INSERT INTO users VALUES (%s, %s,%s, %s)"
    val =  [id1, fullname1,username1, password1]
    my_cursor.execute(sql, val)
    mydb.commit()
   # messagebox.showinfo("REGISTRATION MESSAGE" + str(my_cursor.rowcount, "was inserted"))
    messagebox.showinfo("REGISTRATION MESSAGE", "USER REGISTERED SUCCESSFULLY")

# Interface


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x500')
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



reg_btn = Button(root, text='Submit', bg='green yellow', fg='grey8', command=insertdb)
reg_btn.place(x=280, y=300, width=80)

root.mainloop()

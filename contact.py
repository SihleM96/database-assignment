from tkinter import messagebox
from tkinter import*
import mysql.connector


# Connect Database

dtb_connect = mysql.connector.connect(host="127.0.0.1",
                                      user="lifechoices",
                                      password="@Lifechoices1234",
                                      database="lifechoicesonline")


my_cursor = dtb_connect.cursor()
#
#sql = "INSERT INTO users VALUES (%s,%s,%s,%s,)"
#dtb_connect .commit()
#


def sub():
    messagebox.showinfo("LOG MESSAGE", "Signed In, Enjoy your day!")
    root.destroy()


def log_out():
    messagebox.showinfo("LOG MESSAGE", "Signed Out")
    root.withdraw()


# Interface

root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='grey8')

lbl_password = Label(root,  bg='grey8', fg='green yellow', text='Enter Contact',)
lbl_password.place(x=150, y=100)

password = Entry(root, width=45)
password.place(x=140, y=180, width=120)

reg_btn = Button(root, text='Sign In', bg='green yellow', fg='grey8', command=sub)
reg_btn.place(x=100, y=240, width=80)

logout_btn = Button(root, text='Sign Out', bg='green yellow', fg='grey8', command=log_out)
logout_btn.place(x=220, y=240, width=80)

root.mainloop()


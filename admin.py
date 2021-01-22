from tkinter import messagebox
from tkinter import*
import mysql.connector


# Connect Database

dtb_connect = mysql.connector.connect(host="127.0.0.1",
                                      user="lifechoices",
                                      password="@Lifechoices1234",
                                      database="lifechoicesonline")


my_cursor = dtb_connect.cursor()
sql = "INSERT INTO users VALUES (%s, curtime())"
dtb_connect .commit()

# Interface

root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='black')

lbl_password = Label(root,  bg='black', fg='green yellow', text='Administrator Login Page')
lbl_password.place(x=50, y=50, width=300)

lbl_password = Label(root,  bg='black', fg='white', text='Enter Password')
lbl_password.place(x=150, y=100)

password = Entry(root, width=45)
password.place(x=140, y=150, width=120)

reg_btn = Button(root, text='Login', bg='green yellow', fg='grey8', command='')
reg_btn.place(x=160, y=200, width=80)

root.mainloop()



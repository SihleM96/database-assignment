from tkinter import messagebox
from tkinter import *
import mysql.connector

# Connect Database
mydb = mysql.connector.connect(host="127.0.0.1",
                               user="lifechoices",
                               password="@Lifechoices1234",
                               database="lifechoicesonline",
                               auth_plugin="mysql_native_password")
mycursor = mydb.cursor()


# creating function

def verify():
    users = user_entry.get()
    passs = pass_entry.get()
    sql = "select * from users where username = %s and password = %s"
    mycursor.execute(sql, [users, passs])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo("LOG MESSAGE", "You have successfully logged")
    import contact
    root.destroy()


# if login details are incorrect
def failed():
    messagebox.showinfo("LOG MESSAGE", "Error, try again")
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


# Interface


root = Tk()
root.title('Lifechoices Online')
root.geometry('600x400')
root.configure(bg='grey9')
photo = PhotoImage(file="logo.png")
w = Label(root, image=photo, width=220, height=150)
w.pack()

lbl_id = Label(root, bg='grey9', fg='green yellow', text='Enter Username', )
lbl_id.place(x=180, y=200)

user_entry = Entry(root, width=45)
user_entry.place(x=300, y=200, width=120)

lbl_id = Label(root, bg='grey9', fg='green yellow', text='Enter Password', )
lbl_id.place(x=180, y=250)

pass_entry = Entry(root, width=45)
pass_entry.place(x=300, y=250, width=120)

login_btn = Button(root, text='Login', bg='green yellow', fg='grey8', command=verify)
login_btn.place(x=200, y=300, width=80)

adm_btn = Button(root, text='Admin', bg='green yellow', fg='grey8', command='')
adm_btn.place(x=320, y=300, width=80)

root.mainloop()

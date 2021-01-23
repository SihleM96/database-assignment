from tkinter import messagebox
from tkinter import*
import mysql.connector


# Connect Database

mydb = mysql.connector.connect(host="127.0.0.1",
                                      user="lifechoices",
                                      password="@Lifechoices1234",
                                      database="lifechoicesonline")


mycursor = mydb.cursor()


# Function

def verify():
    passwrd = password.get()
    sql = "select * from admin where password = %s"
    mycursor.execute(sql, [passwrd])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def logged():
    messagebox.showinfo("LOG MESSAGE", "You have successfully logged in")
    import register
    root.destroy()


# if login details are incorrect

def failed():
    messagebox.showinfo("LOG MESSAGE", "Error, try again")
    password.delete(0, END)

# datetime function


# Interface

root = Tk()
root.title('Lifechoices Online')
root.geometry('400x400')
root.configure(bg='grey8')

lbl_password = Label(root,  bg='grey8', fg='green yellow', text='Administrator Login Page')
lbl_password.place(x=50, y=50, width=300)

lbl_password = Label(root,  bg='grey8', fg='white', text='Enter Password')
lbl_password.place(x=150, y=100)

password = Entry(root, width=45)
password.place(x=140, y=150, width=120)

log_btn = Button(root, text='Login', bg='green yellow', fg='grey8', command=verify)
log_btn.place(x=160, y=200, width=80)


root.mainloop()




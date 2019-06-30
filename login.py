from tkinter import *

#possible tables: recruiter, candidate, admin
def check_login():
    name,password,admin,recruiter,candidate='UNSET'
    if name in admin and password:
        login_admin()
    if name in recruiter and password:
        login_recruiter()
    elif name in candidate and password:
        login_candidate()

def login_admin():
    pass

def login_recruiter():
    pass

def login_candidate():
    pass
def test():
    print('works')


root = Tk()
root.title('Database GUI')
#root.winfo_toplevel().title('Database GUI')


name_label = Label(root, text='Name')
name_label.grid(row=1, sticky=W)
password_label = Label(root, text='Password')
password_label.grid(row=2, sticky=W)
welcome_label = Label(root, text='Please login')
welcome_label.grid(row=0, columnspan=2)

input_name = StringVar()
name_entry = Entry(root, textvariable=input_name, width=15)
name_entry.grid(row=1, column=1, sticky=W)

input_password = StringVar()
password_entry = Entry(root, textvariable=input_password, show='*', width=15)
password_entry.grid(row=2, column=1, sticky=W)


def toggle_password():
    if show_password.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


def off():
    password_entry.config(show='*')


show_password = BooleanVar()
show_password_checkbox = Checkbutton(root, text='Show password', variable=show_password, command=toggle_password)
show_password_checkbox.grid(row=3, column=1)


def show():
    """Works"""
    p = input_password.get()
    print(p)


login_button = Button(root, text='Login', command=show)
login_button.grid(row=4, columnspan=2)

root.mainloop()

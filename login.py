from tkinter import *
import mysqlFunctions


class AdminWindow:
    #TODO make a new window or configure the current one?
    def __init__(self, master):
        self.master = master
        master.title("Admin")


class RecruiterWindow:
    def __init__(self, master):
        self.master = master
        master.title("Recruiter")



class CandidateWindow:
    def __init__(self, master):
        self.master = master
        master.title("Candidate")


def test():
    print('works')


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Database GUI")
        self.type_of_user = None
        self.create_widgets()
        root.resizable(False, False)

    def create_widgets(self):
        self.left_space = Label(self.master)
        self.left_space.grid(padx=10)
        self.right_space = Label(self.master)
        self.right_space.grid(column=3, padx=30)

        self.welcome_label = Label(self.master, text='Please login')
        self.welcome_label.grid(row=0, column=2, sticky=N)

        self.username_label = Label(self.master, text='Username')
        self.username_label.grid(row=2, column=1, sticky=E)
        self.password_label = Label(self.master, text='Password')
        self.password_label.grid(row=3, column=1, sticky=E)

        self.input_username = StringVar()
        self.username_entry = Entry(self.master, textvariable=self.input_username, width=20)
        self.username_entry.grid(row=2, column=2, sticky=E)


        self.input_password = StringVar()
        # Password entry automatically hides what is typed
        self.password_entry = Entry(self.master, textvariable=self.input_password, show='*', width=20)
        self.password_entry.grid(row=3, column=2, sticky=E)
        # Pressing Enter in the password entry calls login
        self.password_entry.bind('<Return>', self.check_login)

        self.show_password = BooleanVar()
        self.show_password_checkbox = Checkbutton(self.master, text='Show password',
                                                  variable=self.show_password,
                                                  command=self.toggle_password)
        self.show_password_checkbox.grid(row=4, column=2, sticky=E)

        self.login_button = Button(self.master, text='Login', command=self.check_login)
        self.login_button.grid(row=6, column=2, sticky=N + E + W + S)
        self.login_button.bind()

    def toggle_password(self):
        if self.show_password.get():
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def check_login(self, event=None):
        """ Calls mysqlFunctions.login and opens the appropriate window depending on the type of user that
            logged in. If the password if wrong it makes a new label and tells the user
        """
        self.type_of_user = mysqlFunctions.login(self.input_username.get(), self.input_password.get())
        if self.type_of_user == 'recruiter':
            root2 = Toplevel(self.master)
            recruiter = RecruiterWindow(root2)

        elif self.type_of_user == 'candidate':
            pass
            # candidate_window()
        elif self.type_of_user == 'admin':
            pass
            # admin_window()
        else:
            self.wrong_password = Label(self.master, text='Wrong password or username', fg='red')
            self.wrong_password.grid(row=1, column=1, columnspan=3, sticky=N)

    print(mysqlFunctions.login('msmith', 'we3wd'))


root = Tk()
app = LoginWindow(root)
root.mainloop()

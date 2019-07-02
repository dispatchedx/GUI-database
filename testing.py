from tkinter import *
import mysqlFunctions

class AdminWindow:
    # TODO make a new window or configure the current one?
    def __init__(self, master):
        self.master = master
        master.title("Admin control panel")
        master.geometry("500x500")
        self.create_widgets()
        self.grid_widgets()

    def create_widgets(self):
        self.upper_left_space = Label(self.master)
        self.register_candidate_button = Button(self.master, text='register a candidate',
                                                command=self.register_candidate)
        self.register_recruiter_button = Button(self.master, text='register a recruiter',
                                                command=self.register_recruiter)


    def grid_widgets(self):
        self.upper_left_space.grid(padx=10, pady=0)
        self.register_candidate_button.grid(row=2, column=3, sticky=NSEW, ipadx=20, pady=5)
        self.register_recruiter_button.grid(row=4, column=3, sticky=NSEW, pady=5)

    def register_base(self):
        # TODO registration date no need for this it should be automatic
        # TODO username=12 length, password=10, name=25, surname=35, email=30, firm/AFM=9, exp_years=TINYINT,
        # TODO sistatikes=35, certificates=35
        # Input variables
        self.input_username = StringVar()
        self.input_password = StringVar()
        self.input_name = StringVar()
        self.input_surname = StringVar()
        self.input_email = StringVar()
        # Labels
        self.username = Label(self.master, text='Username')
        self.password = Label(self.master, text='Password')
        self.name = Label(self.master, text='Name')
        self.surname = Label(self.master, text='Surname')
        self.email = Label(self.master, text='Email')
        # Entry text boxes
        self.username_entry = Entry(self.master, textvariable=self.input_username)
        self.password_entry = Entry(self.master, textvariable=self.input_password)
        self.name_entry = Entry(self.master, textvariable=self.input_name)
        self.surname_entry = Entry(self.master, textvariable=self.input_surname)
        self.email_entry = Entry(self.master, textvariable=self.input_email)
        # Grid the labels
        self.username.grid(row=2, column=5, padx=10, sticky=E)
        self.password.grid(row=3, column=5, padx=10, sticky=E)
        self.name.grid(row=4, column=5, padx=10, sticky=E)
        self.surname.grid(row=5, column=5, padx=10, sticky=E)
        self.email.grid(row=6, column=5, padx=10, sticky=E)
        # Grid the entry text boxes
        self.username_entry.grid(row=2, column=6, sticky=W)
        self.password_entry.grid(row=3, column=6, sticky=W)
        self.name_entry.grid(row=4, column=6, sticky=W)
        self.surname_entry.grid(row=5, column=6, sticky=W)
        self.email_entry.grid(row=6, column=6, pady=10, sticky=W)

    def submit(self):
        self.info_list = []
        for var in self.variables:
            self.info_list.append(var.get())
        mysqlFunctions.register(self.info_list)
    def register_candidate(self):
        self.register_base()
        self.exp_years = Label(self.master, text='Years of experience')
        self.firm = Label(self.master, text='AFM')
        self.input_exp_years = IntVar()
        self.exp_years_entry = Entry(self.master, textvariable=self.input_exp_years)
        self.input_firm = StringVar()
        self.firm_entry = Entry(self.master, textvariable=self.input_firm)

        self.exp_years.grid(row=7, column=5, padx=10, sticky=E)
        self.firm.grid(row=8, column=5, padx=10, sticky=E)
        self.exp_years_entry.grid(row=7, column=6, sticky=W)
        self.firm_entry.grid(row=8, column=6, pady=10, sticky=W)

        self.submit_button = Button(self.master, text='submit', command=self.submit)
        self.submit_button.grid(row=9, column=6)

        self.variables=[self.input_username,
                        self.input_password,
                        self.input_name,
                        self.input_surname,
                        self.input_email,
                        self.input_exp_years,
                        self.input_firm
                        ]

    def register_recruiter(self):
        self.register_base()

        self.variables = [self.input_username,
                          self.input_password,
                          self.input_name,
                          self.input_surname,
                          self.input_email,
                          #self.input_sistatikes,
                          #self.input_certificates,
                          ]


root = Tk()
window = AdminWindow(root)
root.mainloop()

from tkinter import *
import mysqlFunctions
import datetime
from tkinter import messagebox
from tkinter import ttk


class AdminWindow(mysqlFunctions.Common):
    # TODO make a new window or configure the current one?
    def __init__(self, master):
        mysqlFunctions.Common.__init__(self)
        self.master = master
        master.title("Admin control panel")
        master.geometry("500x500")
        self.create_widgets()
        self.grid_widgets()

    def create_widgets(self):
        self.upper_left_space = Label(self.master)
        self.register_candidate_button = Button(self.master, text='Register a candidate',
                                                command=self.register_candidate)
        self.register_recruiter_button = Button(self.master, text='Register a recruiter',
                                                command=self.register_recruiter)
        self.add_antikeim_button = Button(self.master, text='Add antikeim',
                                          command=self.add_antikeim)
        self.add_business_areas_button = Button(self.master, text='Add business areas',
                                                command=self.add_business_areas)
        self.change_history_button = Button(self.master, text='Change history', command=self.change_history)

    def grid_widgets(self):
        self.upper_left_space.grid(padx=10, pady=0)
        self.register_candidate_button.grid(row=2, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)
        self.register_recruiter_button.grid(row=3, column=3, sticky=NSEW, ipady=2)
        self.add_antikeim_button.grid(row=4, column=3, sticky=NSEW, ipady=2, pady=5)
        self.add_business_areas_button.grid(row=5, column=3, sticky=NSEW, ipady=2)
        self.change_history_button.grid(row=6, column=3, sticky=NSEW, ipady=2, pady=5)

    def add_antikeim(self):

        self.destroyer()
        # Variables
        self.input_title = StringVar()

        # Labels
        self.title = Label(self.master, text='    Title')
        self.description = Label(self.master, text='Description')
        self.belongs = Label(self.master, text='Belongs to')

        # Entries and List boxes
        self.title_entry = Entry(self.master, textvariable=self.input_title)
        self.description_combobox = ttk.Combobox(self.master, state="readonly", values=['Level one element',
                                                                                        'Level two element'])
        self.values_belongs = mysqlFunctions.fetch_belongs()
        belongs_list = []
        # Adding values by iterating belongs_list
        self.belongs_combobox = ttk.Combobox(self.master, state="readonly", values=[value for value in belongs_list])
        # Grid
        self.title.grid(row=2, column=5, padx=10, sticky=E)
        self.title_entry.grid(row=2, column=6, ipady=1, sticky=E+W)
        self.description.grid(row=3, column=5, padx=10, sticky=E)
        self.description_combobox.grid(row=3, column=6)
        self.belongs.grid(row=4, column=5, padx=10, sticky=E)
        self.belongs_combobox.grid(row=4, column=6)
        self.submit_button = Button(self.master, text='Submit',
                                    command=lambda: self.submit('antikeim', self.title_entry.get()))
        self.submit_button.grid(row=5, column=6, sticky=NSEW)

        self.variables = [self.title_entry,
                          self.description_combobox,
                          self.belongs_combobox]

        self.removable_widgets = [self.submit_button,
                                  self.title,
                                  self.title_entry,
                                  self.description,
                                  self.belongs,
                                  self.belongs_combobox,
                                  self.description_combobox]

    def add_business_areas(self):
        # TODO implement this but need mysql part
        self.destroyer()

    def change_history(self):
        # TODO implement this but need mysql part
        self.destroyer()
        self.change_h_for_table = Label(self.master, text='Show history for table')
        self.change_h_for_table.grid(row=2, column=5)
        self.change_h_for_table_combobox = ttk.Combobox(self.master, state='readonly',
                                                        values=['candidate',
                                                                'recruiter',
                                                                'user',
                                                                'etaireia',
                                                                'job'])
        self.change_h_for_table_combobox.grid(row=2, column=6)
        self.change_h_for_user = Label(self.master, text='Show history for user')
        self.change_h_for_user.grid(row=3, column=5)
        users = mysqlFunctions.fetch_users()
        self.change_h_for_user_combobox = ttk.Combobox(self.master, state='readonly', values=[user for user in users])
        self.change_h_for_user_combobox.grid(row=3, column=6)

        self.removable_widgets = [self.change_h_for_user,
                                  self.change_h_for_user_combobox,
                                  self.change_h_for_table,
                                  self.change_h_for_table_combobox]

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

        # Grid labels
        self.username.grid(row=2, column=5, padx=10, sticky=E)
        self.password.grid(row=3, column=5, padx=10, sticky=E)
        self.name.grid(row=4, column=5, padx=10, sticky=E)
        self.surname.grid(row=5, column=5, padx=10, sticky=E)
        self.email.grid(row=6, column=5, padx=10, sticky=E)

        # Grid entry text boxes
        self.username_entry.grid(row=2, column=6, sticky=W)
        self.password_entry.grid(row=3, column=6, sticky=W)
        self.name_entry.grid(row=4, column=6, sticky=W)
        self.surname_entry.grid(row=5, column=6, sticky=W)
        self.email_entry.grid(row=6, column=6, pady=10, sticky=W)

        self.removable_widgets = [self.username, self.username_entry, self.password, self.password_entry, self.name,
                                  self.name_entry, self.surname, self.surname_entry, self.email, self.email_entry]

    def submit(self, table_name, primary_key):
        # TODO maybe reg_date is automatic
        #self.table_name = table_name
        self.info_list = []
        for var in self.variables:
            self.info_list.append(var.get())
        self.current_datetime = datetime.datetime.now()
        if table_name == 'recruiter' or table_name == 'candidate':
            self.info_list.insert(4, self.current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
            result = mysqlFunctions.register(self.info_list, table_name)
        elif table_name == 'antikeim':
            result = mysqlFunctions.register(self.info_list, table_name)
        else:
            result = 'Error: no table %s exists' % table_name
        if result == 'Success':
            self.destroyer()
            messagebox.showinfo("Success", f'Registration of {primary_key} was a success')
        else:
            messagebox.showerror("Error", result)


    def register_recruiter(self):
        self.destroyer()
        # TODO make firm a listbox
        self.register_base()
        self.input_firm = StringVar()
        self.input_exp_years = IntVar()
        self.exp_years = Label(self.master, text='Years of experience')
        self.exp_years_entry = Entry(self.master, textvariable=self.input_exp_years)
        self.firm = Label(self.master, text='AFM')
        self.firm_entry = Entry(self.master, textvariable=self.input_firm)
        self.firm.grid(row=8, column=5, padx=10, sticky=E)
        self.firm_entry.grid(row=8, column=6, pady=10, sticky=W)
        self.exp_years.grid(row=7, column=5, padx=10, sticky=E)
        self.exp_years_entry.grid(row=7, column=6, sticky=W)

        self.submit_button = Button(self.master, text='register',
                                    command=lambda: self.submit('recruiter', self.input_username.get()))
        self.submit_button.grid(row=9, column=6, sticky=NSEW)

        self.variables = [self.input_username,
                          self.input_password,
                          self.input_name,
                          self.input_surname,
                          self.input_email,
                          self.input_exp_years,
                          self.input_firm
                          ]
        self.removable_widgets.extend([self.exp_years,
                                       self.exp_years_entry,
                                       self.firm,
                                       self.firm_entry,
                                       self.submit_button
                                       ])

    def register_candidate(self):
        self.destroyer()
        self.register_base()
        # Variables
        self.input_bio = StringVar()
        self.input_sistatikes = StringVar()
        self.input_certificates = StringVar()

        # Labels
        self.sistatikes = Label(self.master, text='Sistatikes')
        # Note: space is added here to make add space to the whole column to match Recruiter registration
        self.certificates = Label(self.master, text='              Certificates')
        self.bio = Label(self.master, text='Biography')

        # Entry text boxes
        self.certificates_entry = Entry(self.master, textvariable=self.input_certificates)
        self.sistatikes_entry = Entry(self.master, textvariable=self.input_sistatikes)
        # TODO make this TEXT instead of Entry
        self.bio_entry = Entry(self.master, textvariable=self.input_bio)

        # Grid Labels
        self.certificates.grid(row=7, column=5, padx=10, sticky=E)
        self.sistatikes.grid(row=8, column=5, padx=10, sticky=E)
        self.bio.grid(row=9, column=5, ipadx=10, sticky=E)

        # Grid Entries
        self.certificates_entry.grid(row=7, column=6, sticky=W)
        self.sistatikes_entry.grid(row=8, column=6, pady=10, sticky=W)
        self.bio_entry.grid(row=9, column=6, sticky=W+E)

        self.submit_button = Button(self.master, text='register',
                                    command=lambda: self.submit('candidate',self.input_username.get()))
        self.submit_button.grid(row=10, pady=5, column=6, sticky=NSEW)

        self.variables = [self.input_username,
                          self.input_password,
                          self.input_name,
                          self.input_surname,
                          self.input_email,
                          self.input_bio,
                          self.input_sistatikes,
                          self.input_certificates
                          ]
        self.removable_widgets.extend([self.sistatikes,
                                       self.sistatikes_entry,
                                       self.certificates,
                                       self.certificates_entry,
                                       self.bio,
                                       self.bio_entry,
                                       self.submit_button
                                       ])


if __name__ == '__main__':
    root = Tk()
    app = AdminWindow(root)
    root.mainloop()

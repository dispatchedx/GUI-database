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





if __name__ == '__main__':
    root = Tk()
    app = AdminWindow(root)
    root.mainloop()

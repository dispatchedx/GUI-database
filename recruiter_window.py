import mysqlFunctions
from tkinter import *
from tkinter import messagebox

class RecruiterWindow(mysqlFunctions.Common):
    def __init__(self, master, stored_username):
        # Tables: etaireia (link=AFM) recruiter
        # TODO change liagourma to stored_username
        self.stored_username = 'msmith'#stored_username
        mysqlFunctions.Common.__init__(self)
        self.master = master
        master.title('Recruiter control panel')
        master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.upper_left_space = Label(self.master)
        self.upper_left_space.grid(padx=10, pady=0)
        # TODO cant edit AFM, should i maybe not show it at all?
        self.my_profile_button = Button(self.master, text='My profile', command=lambda: self.view_profile('recruiter'))
        self.my_profile_button.grid(row=2, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

        self.my_company_button = Button(self.master, text='My company', command=self.my_company)
        self.my_company_button.grid(row=3, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

        # TODO my_jobs, all_jobs, add_job ...
    def grid_widgets(self):
        pass

    def my_company(self):
        self.destroyer()
        # TODO maybe add sector as well?
        # Variables
        input_telephone = StringVar()
        input_street = StringVar()
        input_num = StringVar()
        input_city = StringVar()
        input_country = StringVar()
        input_sector = StringVar()

        # Labels
        afm = Label(self.master, text='AFM')
        doy = Label(self.master, text='DOY')
        name = Label(self.master, text='Name')
        telephone = Label(self.master, text='Telephone')
        street = Label(self.master, text='Street')
        street_number = Label(self.master, text='Street number')
        city = Label(self.master, text='City')
        country = Label(self.master, text='Country')
        # sector = Label(self.master, text='Sector')

        # Entry boxes
        afm_entry = Entry(self.master, textvariable=afm)
        doy_entry = Entry(self.master, textvariable=doy)
        name_entry = Entry(self.master, textvariable=name)
        telephone_entry = Entry(self.master, textvariable=telephone)
        street_entry = Entry(self.master, textvariable=street)
        street_number_entry = Entry(self.master, textvariable=street_number)
        city_entry = Entry(self.master, textvariable=city)
        country_entry = Entry(self.master, textvariable=country)
        # sector_entry = Entry(self.master, textvariable=sector)
        # sector_entry.insert(END,'0')

        # Grid labels
        afm.grid(row=2, column=5, padx=10, sticky=E)
        doy.grid(row=3, column=5, padx=10, sticky=E)
        name.grid(row=4, column=5, padx=10, sticky=E)
        telephone.grid(row=5, column=5, padx=10, sticky=E)
        street.grid(row=6, column=5, padx=10, sticky=E)
        street_number.grid(row=7, column=5, padx=10, sticky=E)
        city.grid(row=8, column=5, padx=10, sticky=E)
        country.grid(row=9, column=5, padx=10, sticky=E)
        # sector.grid(row=10, column=5, padx=10, sticky=E)

        # Grid Entries
        afm_entry.grid(row=2, column=6, sticky=W)
        doy_entry.grid(row=3, column=6, sticky=W)
        name_entry.grid(row=4, column=6, sticky=W)
        telephone_entry.grid(row=5, column=6, sticky=W)
        street_entry.grid(row=6, column=6, sticky=W)
        street_number_entry.grid(row=7, column=6, sticky=W)
        city_entry.grid(row=8, column=6, sticky=W)
        country_entry.grid(row=9, column=6, sticky=W)
        # sector_entry.grid(row=10, column=6, sticky=W)

        self.entry_widgets = [afm_entry,
                              doy_entry,
                              name_entry,
                              telephone_entry,
                              street_entry,
                              street_number_entry,
                              city_entry,
                              country_entry]
                              #sector_entry]
        info_list = mysqlFunctions.fetch_etaireia_info(self.stored_username)
        for widget, info in zip(self.entry_widgets, info_list):
            widget.insert(END, info)
        for widget in self.entry_widgets[:3]:
            widget.config(state='disabled')
        for widget in self.entry_widgets[3:]:
            widget.config(state='readonly')
        self.edit_button = Button(self.master, text='Edit info', command=self.edit_company)
        self.edit_button.grid(row=11, column=6, sticky=NSEW)

    def edit_company(self):
        for widget in self.entry_widgets[3:]:
            widget.config(state='normal')
        self.edit_button.config(text='Done editing', command=self.done_edit_company)

    def done_edit_company(self):
        """
        :var: info_list_updated: List of strings: contains the updated info in order: [telephone, street, street_number,
                                city, country]
        """
        for widget in self.entry_widgets[3:]:
                widget.config(state='readonly')
        self.edit_button.config(text='edit info', command=self.edit_company)
        info_list_updated = [entry.get() for entry in self.entry_widgets[3:]]
        afm = self.entry_widgets[0].get()
        result = mysqlFunctions.done_edit_etaireia(afm, info_list_updated)
        if result == 'Success':
            messagebox.showinfo("Success", f'Successfully updated all values.')
        else:
            messagebox.showerror("Error", result)

    def add_job(self):
        self.destroyer()
        pass

    def my_jobs(self):
        self.destroyer()
        pass

    def all_jobs(self):
        self.destroyer()
        pass


if __name__ == '__main__':
    root = Tk()
    app = RecruiterWindow(root, None)
    root.mainloop()

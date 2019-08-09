import mysqlFunctions
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class RecruiterWindow(mysqlFunctions.Common):
    def __init__(self, master, stored_username):
        # Tables: etaireia (link=AFM) recruiter
        # TODO change liagourma to stored_username
        self.stored_username = stored_username
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

        self.all_jobs_button = Button(self.master, text='All jobs', command=self.all_jobs)
        self.all_jobs_button.grid(row=4,column=3,sticky=NSEW,ipady=2,ipadx=20,pady=5)
        # TODO my_jobs, all_jobs, add_job ...

    def grid_widgets(self):
        pass

    def my_company(self):
        self.destroyer()
        self.master.geometry("500x500")
        # TODO maybe add sector as well?

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
        country_entry = Entry(self.master)
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

        self.removable_widgets.extend([afm,
                                       doy,
                                       name,
                                       telephone,
                                       street,
                                       street_number,
                                       city,
                                       country,
                                       afm_entry,
                                       doy_entry,
                                       name_entry,
                                       telephone_entry,
                                       street_entry,
                                       street_number_entry,
                                       city_entry,
                                       country_entry,
                                       self.edit_button])

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
        self.master.geometry("1000x500")
        tv = ttk.Treeview(self.master)
        # TODO maybe remove the other 3 username variables from scope
        tv['columns'] = ('salary', 'position', 'edra', 'recruiter', 'announce_date', 'submission_date')
        tv.heading("#0", text='Start date')
        tv.column('#0', anchor='center', width=100)
        tv.heading("salary", text='Salary')
        tv.column('salary', anchor='center', width=50)
        tv.heading("position", text='Position')
        tv.column('position', anchor='center', width=200)
        tv.heading("edra", text='Edra')
        tv.column('edra', anchor='center', width=100)
        tv.heading("recruiter", text='Recruiter')
        tv.column('recruiter', anchor='center', width=70)
        tv.heading("announce_date", text='Announce date')
        tv.column('announce_date', anchor='center', width=115)
        tv.heading("submission_date", text='Submission date')
        tv.column('submission_date', anchor='center', width=100)
        tv.grid(sticky=NSEW)
        tv.grid(sticky=NSEW)
        extra_space = Label(self.master)
        extra_space.grid(row=12, column=5, pady=50, padx=5)
        self.treeview = tv
        self.treeview.grid(row=2, column=6, rowspan=12)
        edit_job_button = Button(self.master, text='Edit job', command=self.edit_job)
        edit_job_button.grid(row=14, column=6, pady=10, ipadx=10, ipady=3)

        # Populate tree view with applications
        all_jobs = mysqlFunctions.fetch_all_jobs(self.stored_username)
        for arr in all_jobs:
            for job in arr:
                self.treeview.insert('', 'end', text=job[0], values=job[1:])

        self.removable_widgets.extend([self.treeview, edit_job_button])

    def edit_job(self):
        selected = self.treeview.selection()[0]
        print(self.treeview.item(selected)['values'])
        x = self.treeview.get_children()
        #for child in x:
            #print(child)


if __name__ == '__main__':
    root = Tk()
    app = RecruiterWindow(root, None)
    root.mainloop()

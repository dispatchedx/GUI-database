from tkinter import *
import mysqlFunctions
import datetime
from tkinter import messagebox
from tkinter import ttk
import admin_window



class CandidateWindow(admin_window.AdminWindow):
    def __init__(self, master, stored_username):
        self.stored_username = stored_username
        mysqlFunctions.Common.__init__(self)
        self.master = master
        master.title('Candidate control panel')
        master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        self.upper_left_space = Label(self.master)
        self.upper_left_space.grid(padx=10, pady=0)

        self.my_profile_button = Button(self.master, text='My profile', command=self.view_profile)
        self.my_profile_button.grid(row=2, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

        self.available_jobs = Button(self.master, text='Available jobs')
        self.available_jobs.grid(row=3, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

        self.my_application = Button(self.master, text='My applications')
        self.my_application.grid(row=4, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

    def view_profile(self):
        self.destroyer()
        self.register_candidate()
        self.submit_button.destroy()
        self.edit_button = Button(self.master, text='edit info', command=self.edit)
        self.edit_button.grid(row=10, column=6, sticky=NSEW)
        self.username_entry.insert(END, self.stored_username)
        self.username_entry.config(state='disabled')
        # TODO check if stored_username works
        self.info_list = mysqlFunctions.fetch_candidate_info(self.stored_username)
        entry_widgets = [widget for widget in self.removable_widgets if 'entry' in str(widget)]
        # Fill each entry with corresponding info
        for widget, info in zip(entry_widgets[1:], self.info_list):
                print(info)
                widget.insert(END, info)
                widget.config(state='readonly')
        self.removable_widgets.extend([self.edit_button,
                                       ])

    def edit(self):
        self.password_entry.config(state='normal')
        self.name_entry.config(state='normal')
        self.surname_entry.config(state='normal')
        self.email_entry.config(state='normal')
        self.certificates_entry.config(state='normal')
        self.sistatikes_entry.config(state='normal')
        self.bio_entry.config(state='normal')


    def available_jobs(self):
        self.destroyer()

    def applications(self):
        self.destroyer()

















if __name__ == '__main__':
    root = Tk()
    app = CandidateWindow(root)
    root.mainloop()

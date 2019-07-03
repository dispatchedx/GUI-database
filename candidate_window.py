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

        self.available_jobs = Button(self.master, text='Available jobs', command=self.available_jobs)
        self.available_jobs.grid(row=3, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

        self.my_application = Button(self.master, text='My applications', command=self.applications)
        self.my_application.grid(row=4, column=3, sticky=NSEW, ipady=2, ipadx=20, pady=5)

    def view_profile(self):
        self.destroyer()
        self.register_candidate()
        self.submit_button.destroy()
        self.edit_button = Button(self.master, text='edit info', command=self.edit)
        self.edit_button.grid(row=10, column=6, pady=5, sticky=NSEW)
        self.username_entry.insert(END, self.stored_username)
        self.username_entry.config(state='disabled')
        self.info_list = mysqlFunctions.fetch_candidate_info(self.stored_username)
        self.entry_widgets = [widget for widget in self.removable_widgets if 'entry' in str(widget)]
        self.removable_widgets.append(self.edit_button)
        # Fill each entry with corresponding info
        for widget, info in zip(self.entry_widgets[1:], self.info_list):
                widget.insert(END, info)
                widget.config(state='readonly')

    def done_edit(self):
        """
        :var: info_list_updated: List of strings: contains the updated info in order: [password, name, surname, email,
        certificates, sistatikes, bio]
        """
        for widget in self.entry_widgets[1:]:
                widget.config(state='readonly')
        self.edit_button.config(text='edit info', command=self.edit)
        self.info_list_updated = [entry.get() for entry in self.entry_widgets[1:]]
        mysqlFunctions.edit_info(self.stored_username, self.info_list_updated)

    def edit(self):
        """
         entry_widget[0] is username and we don't want to change it so we put everything else
         to normal state which means its editable

        """
        for widget in self.entry_widgets[1:]:
                widget.config(state='normal')
        self.edit_button.config(text='done editing', command=self.done_edit)

    def available_jobs(self):
        self.destroyer()

    def applications(self):
        self.destroyer()

















if __name__ == '__main__':
    root = Tk()
    app = CandidateWindow(root)
    root.mainloop()

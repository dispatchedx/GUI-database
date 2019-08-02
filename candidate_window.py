from tkinter import *
import mysqlFunctions
from tkinter import messagebox
from tkinter import ttk


class CandidateWindow(mysqlFunctions.Common):
    def __init__(self, master, stored_username):
        #TODO change liagourma to stored_username
        self.stored_username = 'cleogeo'#stored_username
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
        self.master.geometry("500x500")
        self.register_candidate()
        self.submit_button.destroy()
        self.edit_button = Button(self.master, text='edit info', command=self.edit)
        self.edit_button.grid(row=10, column=6, pady=5, sticky=NSEW)
        self.username_entry.insert(END, self.stored_username)
        self.username_entry.config(state='disabled')
        self.info_list = mysqlFunctions.fetch_candidate_info(self.stored_username)
        self.entry_widgets = [widget for widget in self.removable_widgets if 'entry' in str(widget)]
        self.removable_widgets.append(self.edit_button)
        # Fill each entry with corresponding info and make it readonly
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
        # TODO if return success
        result = mysqlFunctions.edit_info(self.stored_username, self.info_list_updated)
        if result == 'Success':
            messagebox.showinfo("Success", f'Successfully updated all values.')
        else:
            messagebox.showerror("Error", result)

    def edit(self):
        """
         :var: entry_widget[0]: is username and we don't want to change it so we put everything else
         to normal state which means its editable

        """
        for widget in self.entry_widgets[1:]:
                widget.config(state='normal')
        self.edit_button.config(text='done editing', command=self.done_edit)

    def available_jobs(self):
        self.destroyer()
        self.master.geometry("1000x500")
        tv = ttk.Treeview(self.master)
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

        extra_space = Label(self.master)
        extra_space.grid(row=12, column=5, pady=50, padx=5)

        self.treeview= tv
        self.treeview.grid(row=2, column=6, rowspan=12)

        available_jobs = mysqlFunctions.fetch_available_jobs()

        for job in available_jobs:
            self.treeview.insert('', 'end', text=job[0], values=job[1:])
        self.treeview.grid_rowconfigure(2, weight=0)

        self.apply_job_button = Button(self.master, text='Apply to job(s)')
        self.apply_job_button.grid(row=14, column=6, pady=10, ipadx=10, ipady=3)

        self.removable_widgets.extend([self.treeview, extra_space, self.apply_job_button])

    def select_item(self):
        current_item = self.treeview.focus()
        job_name = self.treeview.item(current_item)['text']
        return job_name

    def applications(self):
        def delete_my_application():
            selected_application = self.select_item()
            if selected_application == '':
                # If nothing is selected, show error
                messagebox.showerror("Error", 'You must select an application first')
                return -1

            result = mysqlFunctions.delete_my_application(self.stored_username, selected_application)
            if result == 'Success':
                messagebox.showinfo("Success", f'Application successfully deleted')

                # Delete item from tree view
                selected_item = self.treeview.selection()[0]
                self.treeview.delete(selected_item)
            else:
                messagebox.showerror("Error", result)

        self.destroyer()
        self.master.geometry("500x500")
        tv = ttk.Treeview(self.master)
        # TODO maybe remove the other 3 username variables from scope
        tv['columns'] = ('my_application_status')
        tv.heading("#0", text='Job name')
        tv.column("#0", anchor='center', width=150)
        tv.heading("my_application_status", text='Status')
        tv.column("0", anchor='center', width=150)
        tv.grid(sticky=NSEW)
        extra_space = Label(self.master)
        extra_space.grid(row=12, column=5, pady=50, padx=5)
        self.treeview = tv
        self.treeview.grid(row=2, column=6, rowspan=12)
        delete_application_button = Button(self.master, text='Delete application', command=delete_my_application)
        delete_application_button.grid(row=14, column=6, pady=10, ipadx=10, ipady=3)

        # Populate tree view with applications
        my_applications = mysqlFunctions.fetch_my_applications(self.stored_username)
        for var in my_applications:
            self.treeview.insert('', 'end', text=var[0], values=var[1:])

        self.removable_widgets.extend([self.treeview, delete_application_button])




# TODO check this


'''
def finish(self):
    self.master.destroy()
'''

if __name__ == '__main__':
    root = Tk()
    app = CandidateWindow(root, None)
    root.mainloop()

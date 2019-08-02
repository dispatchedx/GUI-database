import mysqlFunctions
from tkinter import *


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
        pass

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

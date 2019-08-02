import admin_window
import mysqlFunctions


class RecruiterWindow(mysqlFunctions.Common):
    def __init__(self, master, stored_username):
        # Tables: etaireia (link=AFM) recruiter
        # TODO change liagourma to stored_username
        self.stored_username = 'cleogeo'#stored_username
        mysqlFunctions.Common.__init__(self)
        self.master = master
        master.title('Recruiter control panel')
        master.geometry("500x500")
        self.create_widgets()

    def create_widgets(self):
        pass

    def grid_widgets(self):
        pass

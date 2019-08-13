import MySQLdb
from tkinter import *
from tkinter import messagebox

host = '127.128.0.1'
port = 3306
user = 'root'
password = 'root'
database = 'erecruit'
# TODO close connection
my_database = MySQLdb.connect(
    host=host,
    port=port,
    user=user,
    passwd=password,
    db=str(database)
)


class Common(object):
    """
    This class contains functions that are shared between the different control panels
    """
    def __init__(self):
        self.removable_widgets = []

    def destroyer(self):
        # TODO proper way is to put everything in a frame and delete the frame
        """
        Destroys every widget except the starting buttons.
        Calling this will essentially return you to the starting panel

        """

        try:
            for self.widget in self.removable_widgets:
                self.widget.destroy()
        except AttributeError:
            pass

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
        self.password_entry.config(show='*')
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
                                    command=lambda: self.submit('candidate', self.input_username.get()))
        self.submit_button.grid(row=10, pady=5, column=6, sticky=NSEW)

        self.variables = [self.input_username,
                          self.input_password,
                          self.input_name,
                          self.input_surname,
                          self.input_email,
                          self.input_bio,
                          self.input_certificates,
                          self.input_sistatikes
                          ]
        self.removable_widgets.extend([self.certificates,
                                       self.certificates_entry,
                                       self.sistatikes,
                                       self.sistatikes_entry,
                                       self.bio,
                                       self.bio_entry,
                                       self.submit_button
                                       ])

    def view_profile(self, type_of_user):
        self.destroyer()
        self.master.geometry("500x500")
        if type_of_user == 'recruiter':
            self.register_recruiter()
            self.info_list = fetch_recruiter_info(self.stored_username)
        elif type_of_user == 'candidate':
            self.register_candidate()
            self.info_list = fetch_candidate_info(self.stored_username)
        self.submit_button.destroy()
        self.edit_button = Button(self.master, text='Edit info', command=lambda: self.edit(type_of_user))
        self.edit_button.grid(row=10, column=6, pady=5, sticky=NSEW)
        self.username_entry.insert(END, self.stored_username)
        self.username_entry.config(state='disabled')
        self.entry_widgets = [widget for widget in self.removable_widgets if 'entry' in str(widget)]
        self.removable_widgets.append(self.edit_button)
        # Fill each entry with corresponding info and make it readonly
        for widget, info in zip(self.entry_widgets[1:], self.info_list):
                widget.insert(END, info)
                widget.config(state='readonly')
        # recruiter's AFM must not be editable
        if type_of_user == 'recruiter':
            self.entry_widgets[-1].config(state='disabled')

    def edit(self, type_of_user):
        """
         :var: entry_widget[0]: is username and we don't want to change it so we put everything else
         to normal state which means its editable

         :var: entry_widget[1]: is password field and we don't want to show it so we use config(show='*')

        """
        for widget in self.entry_widgets[1:]:
            widget.config(state='normal')
        # recruiter's AFM must not be editable
        if type_of_user == 'recruiter':
            self.entry_widgets[-1].config(state='disabled')
        self.entry_widgets[1].config(show='')
        # TODO maybe not, after done editing password remains visible
        self.edit_button.config(text='done editing', command=lambda: self.done_edit(type_of_user))

    def done_edit(self, type_of_user):
        """
        :var: info_list_updated: List of strings: contains the updated info in order: [password, name, surname, email,
        certificates, sistatikes, bio]
        """
        for widget in self.entry_widgets[1:]:
                widget.config(state='readonly')
        self.edit_button.config(text='Edit info', command=lambda: self.edit(type_of_user))
        self.info_list_updated = [entry.get() for entry in self.entry_widgets[1:]]
        result = edit_info(self.stored_username, self.info_list_updated, type_of_user)
        if result == 'Success':
            messagebox.showinfo("Success", f'Successfully updated all values.')
        else:
            messagebox.showerror("Error", result)


def delete_my_application(username, selected_application):

    cursor = my_database.cursor()
    try:
        #TODO trigger for submission date checking
        cursor.execute(""" DELETE FROM t1 USING applies t1 INNER JOIN job t2 ON (t1.job_id=t2.id) WHERE
                        cand_usrname=%s and position=%s """, (username, selected_application))
        my_database.commit()
        return 'Success'
    except MySQLdb.Error as e:
        my_database.rollback()
        return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
    finally:
        cursor.close()


def fetch_job_applications(job_name):
    cursor = my_database.cursor()

    try:
        cursor.execute(""" SELECT COUNT(*) FROM applies,job WHERE applies.job_id=job.id
                            and job.position=%s;""", [job_name])
        result = cursor.fetchone()
        applications = list(result)
        return applications
    finally:
        cursor.close()


def fetch_my_applications(username):
    cursor = my_database.cursor()
    # TODO need to select position + status
    try:
        cursor.execute("""SELECT position FROM applies INNER JOIN job ON job.id=applies.job_id 
                        WHERE applies.cand_usrname=%s """, ([username]))
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()


def fetch_available_jobs():

    cursor = my_database.cursor()

    try:
        #TODO change <= to >=
        cursor.execute("""SELECT start_date, salary, position, edra, recruiter, announce_date, submission_date
                        FROM job WHERE submission_date <= CURDATE();""")
        result = cursor.fetchall()
        return result

    finally:
        cursor.close()


def edit_info(username, info_list_updated, type_of_user):
    """
    :param username: Username
    :param: info_list_updated: List of strings: contains the updated info in order: [password, name, surname, email,
    certificates, sistatikes, bio]
    :return:
    """
    cursor = my_database.cursor()
    if type_of_user == 'candidate':
        try:
            cursor.execute("""UPDATE  user SET password=%s, name=%s, surname=%s, email=%s WHERE user.username=%s""",
                           (info_list_updated[0], info_list_updated[1], info_list_updated[2], info_list_updated[3],
                            username))
            cursor.execute("""UPDATE candidate SET  certificates=%s, sistatikes=%s, bio=%s WHERE candidate.username=%s""",
                           (info_list_updated[4], info_list_updated[5], info_list_updated[6], username))
            my_database.commit()
            return'Success'
        except MySQLdb.Error as e:
            my_database.rollback()
            return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
        finally:
            cursor.close()
    elif type_of_user == 'recruiter':
        try:
            cursor.execute("""UPDATE  user SET password=%s, name=%s, surname=%s, email=%s WHERE user.username=%s""",
                           (info_list_updated[0], info_list_updated[1], info_list_updated[2], info_list_updated[3],
                            username))
            cursor.execute("""UPDATE recruiter SET exp_years=%s, firm=%s WHERE recruiter.username=%s""",
                           (info_list_updated[4], info_list_updated[5], username))
            my_database.commit()
            return 'Success'
        except MySQLdb.Error as e:
            my_database.rollback()
            return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
        finally:
            cursor.close()


def login(username, password):
    """
    :param username: input username
    :param password: input password
    :return: Α String containing the type_of_user of user. Can be either "candidate", "recruiter", "admin".
     If user doesnt exist returns "None"
    """
    # TODO is this how it should even work ? replace root with username, password

    my_database = MySQLdb.connect(
        host=host,
        port=port,
        user='root',
        passwd='root',
        db=str(database)
    )
    cursor = my_database.cursor()
    cursor.execute("""SELECT username, password FROM user 
    WHERE username = %s AND password = %s""", (username, password,))
    result = cursor.fetchone()

    try:
        if result is not None:
            if cursor.execute("""SELECT username FROM candidate WHERE username = %s""", (result[0],)):
                return 'candidate'
            elif cursor.execute("""SELECT username FROM recruiter WHERE username = %s""", (result[0],)):
                return 'recruiter'
            elif cursor.execute("""SELECT username FROM admin WHERE username = %s""", (result[0],)):
                return 'admin'
        else:
            return None
    finally:
        cursor.close()

def apply_to_jobs(candidate_username, job_name):
    cursor = my_database.cursor()
    try:
        cursor.execute("""INSERT INTO applies (cand_usrname, job_id)  SELECT %s, id FROM job WHERE job.position=%s""",
                           (candidate_username, job_name))
        my_database.commit()
        return 'Success'
    except MySQLdb.Error as e:
        my_database.rollback()
        return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
    finally:
        cursor.close()


def fetch_all_jobs():
    cursor = my_database.cursor()
    cursor.execute("""SELECT start_date, salary, position, edra, recruiter, announce_date, submission_date FROM job""")
    result = cursor.fetchall()
    all_jobs = list(result)
    cursor.close()
    return all_jobs


def fetch_my_jobs(recruiter_username):
    cursor = my_database.cursor()
    cursor.execute("""SELECT start_date, salary, position, edra, recruiter, announce_date, submission_date FROM job
                        WHERE job.recruiter=%s""", [recruiter_username])
    result = cursor.fetchall()
    my_jobs = list(result)
    cursor.close()
    return my_jobs


def fetch_business_areas():
    """
    :return: List of strings: all unique belongs_to in table sector
    """
    cursor = my_database.cursor()
    cursor.execute('SELECT distinct title FROM sector')
    result = cursor.fetchall()
    # There was a bug causing brackets to appear on some elements, this implementation fixes it
    values_list = list(result)
    values_list = [''.join(x) for x in values_list]
    cursor.close()
    return values_list


def fetch_belongs():
    """
    :return: List of strings: all unique belongs_to in table antikeim
    """
    cursor = my_database.cursor()
    cursor.execute('SELECT distinct title FROM antikeim')
    result = cursor.fetchall()
    # There was a bug causing brackets to appear on some elements, this implementation fixes it
    values_list = list(result)
    values_list = [''.join(x) for x in values_list]
    cursor.close()
    return values_list


def fetch_users():
    """
    :return: List of strings: all usernames in the database
    """
    cursor = my_database.cursor()
    cursor.execute('SELECT username from user')
    result = cursor.fetchall()
    # Convert tuple to list
    users_list = list(result)
    cursor.close()
    return users_list


def fetch_candidate_info(candidate_username):
    """
    :param candidate_username: String: Candidate's username to fetch info for
    :return: List of Strings: password, name, surname, email, certificates,
             sistatikes, biography for given candidate
    """
    cursor = my_database.cursor()
    cursor.execute("""SELECT password,name,surname,email,certificates,sistatikes,bio FROM candidate INNER JOIN 
                    user ON user.username=candidate.username WHERE user.username=%s""", [candidate_username])
    result = cursor.fetchone()
    # Convert tuple to list
    cursor.close()
    return list(result)


def fetch_recruiter_info(recruiter_username):

    cursor = my_database.cursor()
    cursor.execute("""SELECT password, name, surname, email, exp_years, firm FROM recruiter INNER JOIN 
                    user ON user.username=recruiter.username WHERE user.username=%s""", [recruiter_username])
    result = cursor.fetchone()
    info_list = list(result)
    cursor.close()
    return info_list


def fetch_etaireia_info(recruiter_username):
    cursor = my_database.cursor()
    cursor.execute("""select AFM, DOY, name, tel, street, num, city, country, sector from etaireia INNER JOIN
                    recruiter ON etaireia.AFM=recruiter.firm WHERE recruiter.username=%s""", [recruiter_username])

    result = cursor.fetchone()
    info_list = list(result)
    cursor.close()
    return info_list


def done_edit_etaireia(recruiter_afm, info_list):
    cursor = my_database.cursor()

    try:
        cursor.execute("""UPDATE etaireia SET tel=%s, street=%s, num=%s, city=%s, country=%s WHERE etaireia.AFM=%s""",
                       (info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], recruiter_afm))
        my_database.commit()
        return 'Success'
    except MySQLdb.Error as e:
        my_database.rollback()
        return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
    finally:
        cursor.close()


def register(info_list, table_name):

    for entry in info_list:
        if len(str(entry)) < 1:
            return 'Error: all fields are required'
    cursor = my_database.cursor()

    try:
        if table_name == 'recruiter' or table_name == 'candidate':
            cursor.execute("""INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s)""",
                           (info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5]))
        if table_name == 'recruiter':
            cursor.execute("""INSERT INTO recruiter (username, exp_years, firm) values (%s, %b, %s)""",
                           (info_list[0], info_list[6], info_list[7],))
        elif table_name == 'candidate':
            cursor.execute("""INSERT INTO candidate (username, bio, sistatikes, certificates) values
             (%s, %s, %s, %s)""", (info_list[0], info_list[6], info_list[7], info_list[8],))
        elif table_name == 'antikeim':
            if info_list[2] == 'None':
                info_list[2] = ''
            cursor.execute('INSERT INTO antikeim (Title, descr, belongs_to) VALUES (%s, %s, %s) ',
                           (info_list[0], info_list[1] + ', child of %s' % info_list[2], info_list[2]))
        elif table_name == 'business_areas':
            if info_list[2] == 'None':
                info_list[2] = ''
            cursor.execute("""INSERT INTO sector (title, description, belongs_to) VALUES (%s, %s, %s)""",
                           (info_list[0], info_list[1], info_list[2]))
        else:
            return f'Error: no table name {table_name} exits'
        my_database.commit()
        return 'Success'
    except MySQLdb.Error as e:
        my_database.rollback()
        return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
    finally:
        cursor.close()



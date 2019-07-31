import MySQLdb

host = '127.128.0.1'
port = 3306
user = 'root'
password = 'root'
database = 'erecruit'


my_database = MySQLdb.connect(
    host=host,
    port=port,
    user=user,
    passwd=password,
    db=str(database)
)


class Common(object):
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

def delete_my_application(username,selected_application):

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

def edit_info(username, info_list_updated):
    """
    :param username: Username
    :param: info_list_updated: List of strings: contains the updated info in order: [password, name, surname, email,
    certificates, sistatikes, bio]
    :return:
    """
    cursor = my_database.cursor()
    try:
        cursor.execute("""UPDATE  user SET password= %s, name=%s, surname=%s, email=%s WHERE user.username=%s""",
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


def login(username, password):
    """
    :param username: input username
    :param password: input password
    :return: Α String containing the type of user. Can be either "candidate", "recruiter", "admin".
     If user doesnt exist returns "None"
    """
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


def fetch_belongs():
    """

    :return: List of strings: all unique belongs_to in table antikeim
    """
    cursor = my_database.cursor()
    cursor.execute('SELECT distinct belongs_to FROM antikeim WHERE belongs_to IS NOT NULL;')
    result = cursor.fetchall()
    values_list = []
    # Convert tuple to list
    for val in result:
        values_list.append(''.join(val))
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
    users_list = []
    for var in result:
        users_list.append(''.join(var))
    cursor.close()
    return users_list


def fetch_candidate_info(candidate_username):
    """

    :param candidate_username: String: Candidate's username to fetch info for
    :return: List of Strings: password, name, surname, email, certificates,
             sistatikes, biography for given candidate
    """
    cursor = my_database.cursor()
    cursor.execute("""SELECT password,name,surname,email,certificates,sistatikes,bio FROM candidate 
    INNER JOIN user ON user.username=candidate.username WHERE user.username=%s""", [candidate_username])
    result = cursor.fetchone()
    # Convert tuple to list
    info_list = []
    for var in result:
        info_list.append(''.join(var))
    cursor.close()
    return info_list


''' # Useless function
def fetch_tables():
    cursor = my_database.cursor()
    cursor.execute('SHOW TABLES;')
    result = cursor.fetchall()
    # Convert tuple to list
    tables_list = []
    for var in result:
        tables_list.append(''.join(var))
    cursor.close()
    return tables_list
'''


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
            cursor.execute('INSERT INTO antikeim (Title, descr, belongs_to) VALUES (%s, %s, %s) ',
                           (info_list[0], info_list[1] + ', child of %s' % info_list[2], info_list[2]))
        else:
            return f'Error: no table name {table_name} exits'
        my_database.commit()
        return 'Success'
    except MySQLdb.Error as e:
        my_database.rollback()
        return 'MySQL Error [%d]: %s' % (e.args[0], e.args[1])
    finally:
        cursor.close()



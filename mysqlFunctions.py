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

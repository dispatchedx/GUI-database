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

def register(info_list):

    cursor = my_database.cursor()
    try:
        cursor.execute("""INSERT INTO `user` (username, `password`, `name`, surname, reg_date, email) values (%s, %s, %s, 
        %s, '1337-08-25 04:20:00', %s);""", (info_list[0], info_list[1], info_list[2], info_list[3], info_list[4],))
        cursor.execute("""INSERT INTO recruiter (username, exp_years, firm) values (%s, %b, %s);""",
                       (info_list[0], info_list[5], info_list[6],))
    finally:
        cursor.close()


cursor = my_database.cursor()
# TODO IT DOESNT INSTERT XD okay fixed needed to commit
try:

    cursor.execute('INSERT into user VALUES (%s,%s,%s,%s,%s,%s)',('username','password','name','surname',
                                                                  '1337-08-25 04:20:00', 'email'))

    my_database.commit()
    result = cursor.fetchone()
    print(result)
finally:
    cursor.close()

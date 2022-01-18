import mysql.connector
from mysql.connector import errorcode


class DBConnector(object):

    def __init__(self, user='root', password='ayari', database='ssi_db', host='localhost'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.dbconn = None

    # creates a new connection
    def create_connection(self):
        cnx = None
        try:
            cnx = mysql.connector.connect(user=self.user, password=self.password, database=self.database,
                                          host=self.host)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        return cnx

        # For explicitly opening database connection

    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self):
        self.dbconn.close()

from helpers.db_connector import DBConnector
import mysql.connector


class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = DBConnector().create_connection()
        return cls.connection

    @classmethod
    def execute_get_query(cls, query: str, values=None, many=False):
        """gets data from the database"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except mysql.connector.Error as err:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        if many:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        cursor.close()
        return result

    @classmethod
    def execute_insert_query(cls, query: str, values=None):
        """inserts/updates data in the database"""
        connection = cls.get_connection()
        try:
            cursor = connection.cursor()
        except mysql.connector.Error as err:
            connection = cls.get_connection(new=True)  # Create new connection
            cursor = connection.cursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        connection.commit()
        cursor.close()

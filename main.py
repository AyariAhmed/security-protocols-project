from helpers.db_connection import DBConnection

connection = DBConnection.get_connection()
print(DBConnection.execute_query("select * from users"))

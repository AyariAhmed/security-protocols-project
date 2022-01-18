from helpers.db_connection import DBConnection
from passlib.hash import sha512_crypt


def add_user(first_name: str, last_name: str, email: str, password: str):
    if find_user_by_email(email) is None:
        insert_query_template = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        values = (first_name, last_name, email, sha512_crypt.hash(password))
        DBConnection.execute_insert_query(insert_query_template, values)
        print(f'User {email} added to the Database!')
    else:
        raise Exception("This user already exists please try another user")


def find_user_by_email(email: str):
    get_query_template = "SELECT * FROM users where email = %s"
    values = (email,)
    return DBConnection.execute_get_query(get_query_template, values)


def find_all_users():
    get_query_template = "SELECT * FROM users"
    return DBConnection.execute_get_query(get_query_template, many=True)
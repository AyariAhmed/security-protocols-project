from helpers.db_connection import DBConnection
from auth.authentication import Auth
from auth.db_queries import find_all_users, find_user_by_email, add_user
from dotenv import dotenv_values

print(dotenv_values()['EMAIL'])
print(dotenv_values()['EMAIL_PASSWORD'])




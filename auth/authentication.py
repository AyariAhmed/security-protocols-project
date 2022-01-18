from helpers.db_connection import DBConnection
from auth.db_queries import add_user
import getpass
import re


def extract_names(email: str):
    """extracts the first_name and the last_name from the provided email"""
    first_name, lastname = email.split("@")[0].split(".")
    return first_name, lastname


class Auth:

    @staticmethod
    def registration():
        """
        Registers a user with valid email and password in the database
        Email and password constraints:
           . The user email should follow this regex: first_name.last_name@insat.ucar.tn.
           . The user password and password confirmation should match.
           . The length of the password should be strictly greater than 6 to increase security.
        """
        email_regex = r"\b[A-Za-z0-9]+\.[A-Za-z0-9]+@insat.ucar.tn\b"
        print('*Please enter your valid credentials')
        email = str(input("-Email: "))
        while not re.fullmatch(email_regex, email):
            print('Invalid email (should be <first_name>.<last_name>@insat.ucar.tn format)')
            email = str(input("-Email: "))
        password = None
        identical = False  # verification of user password and password confirmation
        while not identical:
            password = getpass.getpass('-Password: ')
            while not len(password) > 6:
                print('Invalid password (should be at least 6 characters long)')
                password = getpass.getpass('-Password: ')
            password_confirmation = getpass.getpass('-Password Confirmation: ')
            identical = password_confirmation == password
            if not identical:
                print('Password confirmation does\'t match the given password! Please try again.')
        first_name, last_name = extract_names(email)
        try:
            add_user(first_name, last_name, email, password)
        except Exception as exception:
            print(exception)
            Auth.registration()

    @staticmethod
    def login():
        print('*Please enter your valid credentials')
        email = None
        while not email:
            email = str(input("-Email: "))
        password = None
        while not password:
            password = getpass.getpass('-Password: ')

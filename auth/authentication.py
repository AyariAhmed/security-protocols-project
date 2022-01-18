from passlib.hash import sha512_crypt
from auth.db_queries import add_user, find_user_by_email
from helpers.mailing_service import send_email
import getpass
import re
import random
import string


def extract_names(email: str):
    """extracts the first_name and the last_name from the provided email"""
    first_name, lastname = email.split("@")[0].split(".")
    return first_name, lastname


def random_string_generator(length: int):
    """generates a random string with the given length"""
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(length))


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
        email = email.lower()
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
        remaining_attempts = 2
        verified = False
        while not verified and remaining_attempts > 0:
            remaining_attempts -= 1
            generated_string = random_string_generator(8)
            send_email(email, generated_string)
            print(f'A verification code has been sent your email: {email}')
            code = input(str('Please enter the received code: '))
            verified = code == generated_string
            if verified:
                print("Email Verified!")
            else:
                print('please check again the verification code')

        if not verified and remaining_attempts == 0:
            print("Please try registering with a valid email!")
            Auth.registration()
        else:
            try:
                add_user(first_name, last_name, email, password)
            except Exception as exception:
                print(exception)
                Auth.registration()

    @staticmethod
    def login():
        """Login with given credentials, after verifying the database and double factor authentication"""
        print('*Please enter your valid credentials')
        email = None
        while not email:
            email = str(input("-Email: "))
        password = None
        while not password:
            password = getpass.getpass('-Password: ')
        email = email.lower()
        retrieved_user = find_user_by_email(email)
        if retrieved_user and sha512_crypt.verify(password, retrieved_user[4]):
            remaining_attempts_double_auth = 2
            confirmed_double_auth = False
            while not confirmed_double_auth and remaining_attempts_double_auth > 0:
                remaining_attempts_double_auth -= 1
                generated_string = random_string_generator(8)
                send_email(email, generated_string)
                print(f'A verification code has been sent your email: {email}')
                code = input(str('Please enter the received code: '))
                confirmed_double_auth = code == generated_string
                if confirmed_double_auth:
                    print("*2 factor authentication succeeded")
                else:
                    print('please check again the verification code')
            if confirmed_double_auth:
                print('Logged in successfully')
            else:
                print('Please try again later')

        else:
            print('Please check your credentials (Invalid Credentials)')

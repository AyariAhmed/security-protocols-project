import yagmail
from dotenv import dotenv_values


def send_email(receiver_email: str, verification_code: str):
    config = dotenv_values('.env')
    email = config['EMAIL']
    password = config['EMAIL_PASSWORD']

    if not email or not password:
        print("Please check you have set the environment variables in the .env file")
        return

    yag = yagmail.SMTP(email, password)

    yag.send(receiver_email, 'Verification code', verification_code)
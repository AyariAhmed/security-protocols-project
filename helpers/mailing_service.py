import yagmail
from dotenv import dotenv_values


def send_email(receiver_email: str, verification_code: str):
    config = dotenv_values('.env')
    email = config['EMAIL']
    password = config['EMAIL_PASSWORD']

    yag = yagmail.SMTP(email, password)

    yag.send(receiver_email, 'Verification code', verification_code)
from mail import Mail
from getpass import getpass

sender_id = input("Sender ID: ")
sender_password = getpass(prompt="Sender Password: ")

mailing = Mail(sender_id, sender_password)

email_receiver = input("Receiver ID: ")
email_subject = input("Email Subject: ")
email_content = input("Enter text content to be mailed")

mailing.define_message(email_receiver, email_subject, email_content)

mailing.send_email()


import ssl, smtplib
from email.message import EmailMessage
from email_setup import my_password, my_email


smtp_port = 587
smtp_server = "smtp.gmail.com"

class EmailSend():
    def __init__(self, email_to, subject, body_text):
        self.email_to = email_to
        self.subject = subject
        self.body_text = body_text
        
        # email_to = email_to
        # subject = "Parking Receipt"
        # body_text = "This is a test of the new emailing system."
        # message = "Subject: {}\n\n{}".format(subject, body_text)
        email_from = my_email
        password = my_password

        simple_email_context = ssl.create_default_context()

        try:
            print("Connecting to the server...")
            parking_server = smtplib.SMTP(smtp_server, smtp_port)
            parking_server.starttls(context=simple_email_context)
            parking_server.login(email_from, password)
            print("Connected to server :)")

            print()
            print(f"Sending email from - {email_from}")
            parking_server.sendmail(email_from, email_to, body_text)
            print(f"Email sent to - {email_to}")

        except Exception as e:
            print(e)

        finally:
            parking_server.quit()



import datetime, ssl, smtplib 
from email.message import EmailMessage
from my_password import my_password
# app password = dzms iuxs xxzz iaew

# Format date and time for display in Terminal
today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%Y \n%X %p")
print(formatted_date)

# Get time as int from datetime.datetime
today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

if current_time.hour < 12:
    print("Goodmorning!")
elif 12 <= current_time.hour < 18:
    print("Good Afternoon!")
else:
    print("Good evenning!")

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "isaac.e.mellonie@gmail.com"
email_to = "isaac.e.mellonie@gmail.com"
subject = "Parking Receipt"
body_text = "This is a test of the new emailing system."
message = "Subject: {}\n\n{}".format(subject, body_text)

password = my_password

simple_email_context = ssl.create_default_context()
try:
    print("Connecting to the server...")
    parking_server = smtplib.SMTP(smtp_server, smtp_port)
    parking_server.starttls(context=simple_email_context)
    parking_server.login(email_from, password)
    print("Connected to server :)")

    print()
    print(f"Sending email to - {email_to}")
    parking_server.sendmail(email_from, email_to, message)
    print(f"Email sent to - {email_from}")

except Exception as e:
    print(e)

finally:
    parking_server.quit()

# email_sender = "isaac.e.mellonie@gmail.com"
# email_password = my_password

# email_receiver = "isaaceveans@gmail.com"

# subject = "Parking ticket application email test"
# body = """
# This is an initial test of the applications emailing system.
# """

# em = EmailMessage()
# em ["From"] = email_sender
# em["To"] = email_receiver
# em["subject"] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smpt.gmail.com", 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())




# try:
#     server_ssl = smtplib.SMTP_SSL("smtp.yahoo.com", 465)
#     server_ssl.ehlo() 
# except:
#     "Something went wrong"

# sender = "izeymelon@yahoo.com"
# receiver = "isaaceveans@gmail.com"
# subject = "Hey, this is the parking app!"
# body = "Hey there! Welcome aboard."


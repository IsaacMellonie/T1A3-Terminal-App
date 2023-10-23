import datetime, ssl, smtplib 
from email.message import EmailMessage
from email_setup import my_password, my_email
# app password = dzms iuxs xxzz iaew

# Format date and time for display in Terminal
today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%Y \n%-I:%M %p")
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

# smtp_port = 587
# smtp_server = "smtp.gmail.com"

# email_from = my_email
# email_to = "isaaceveans@gmail.com"
# subject = "Parking Receipt"
# body_text = "This is a test of the new emailing system."
# message = "Subject: {}\n\n{}".format(subject, body_text)

# password = my_password

# simple_email_context = ssl.create_default_context()

# try:
#     print("Connecting to the server...")
#     parking_server = smtplib.SMTP(smtp_server, smtp_port)
#     parking_server.starttls(context=simple_email_context)
#     parking_server.login(email_from, password)
#     print("Connected to server :)")

#     print()
#     print(f"Sending email from - {email_from}")
#     parking_server.sendmail(email_from, email_to, message)
#     print(f"Email sent to - {email_to}")

# except Exception as e:
#     print(e)

# finally:
#     parking_server.quit()



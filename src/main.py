import datetime, ssl, smtplib, time
from email.message import EmailMessage
from email_setup import my_password, my_email

# Format date and time for display in Terminal
today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%Y \n%-I:%M %p")
print(formatted_date)

# Get time as int from datetime.datetime
today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

if current_time.hour < 12:
    print("Good morning!")
elif 12 <= current_time.hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")

inloop_variable = int(0)
register_user = False
check_booking = False

while inloop_variable == 0 and 7 <= current_time.hour < 24:
    inloop_variable = int(input("""Welcome to the Parking Pal App.
    Press 1 to buy parking ticket.
    Press 2 to check current booking. 
        :..."""))
    if inloop_variable == 1: # go to registration set up
        register_user = True
    elif inloop_variable == 1: # go to check booking and email time remaining to self
        check_booking = True
    else:
        inloop_variable == 0 # error message 
        print("\nSorry, I don't recognise that input. Please try again.\n")
        time.sleep(2)
else:
    if register_user == False and check_booking == False and inloop_variable == 1:
        int(input("""\nService hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
    else:
        inloop_variable = 0

rego = []
while register_user == True:
    user_input = str(input("Car Registration: "))
    user_input = user_input.upper()
    rego.append(user_input)
    user_input = str(input("Please enter your password: "))
    rego.append(user_input)
    print(rego)



def email_system():
    smtp_port = 587
    smtp_server = "smtp.gmail.com"

    email_from = my_email
    email_to = "isaaceveans@gmail.com"
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
        print(f"Sending email from - {email_from}")
        parking_server.sendmail(email_from, email_to, message)
        print(f"Email sent to - {email_to}")

    except Exception as e:
        print(e)

    finally:
        parking_server.quit()



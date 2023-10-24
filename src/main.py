import datetime, ssl, smtplib, time, get_user_info
from email.message import EmailMessage
from email_setup import my_password, my_email
from email_system import email_send

# Format date and time for display in Terminal
today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%Y \n%-I:%M %p")
print(formatted_date)

# Get time as int from datetime.datetime
today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

def welcome():
    if current_time.hour < 12:
        print("Good morning!\n")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!\n")
    else:
        print("Good evening!\n")


# check user choice
register_user = False
check_booking = False
inloop_variable = 0

while inloop_variable == 0 and 7 <= current_time.hour < 24:
    inloop_variable = int(input("Welcome to the Parking Pal App\n\nPress 1 to register.\nPress 2 to signin.\nPress 3 to exit.\n"))
    if inloop_variable == 1: # go to registration set up
        register_user = True
        break
    elif inloop_variable == 2: # go to check booking and email time remaining to self
        check_booking = True
        email_to = str(input('Please enter your email address: '))
        email_send(email_to)
        break
    elif inloop_variable == 3: # exit the program
        print("\nBye!\n")
        break
    else:
        # error message 
        print("\nSorry, I don't recognise that input. Please try again.\n")
        time.sleep(1)
        inloop_variable == 0
else:
    if register_user == False and check_booking == False and inloop_variable == 0:
        int(input("""\nService hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
        # log_in()
    else:
        inloop_variable = 0



# check user choice
# register_user = False
# check_booking = False
# inloop_variable = 0

# while inloop_variable == 0 and 7 <= current_time.hour < 24:
#     inloop_variable = int(input("Welcome to the Parking Pal App\n\nPress 1 to buy a ticket.\nPress 2 to check booking.\nPress 3 to exit.\n"))
#     if inloop_variable == 1: # go to registration set up
#         register_user = True
#     elif inloop_variable == 2: # go to check booking and email time remaining to self
#         check_booking = True
#         email_to = str(input('Please enter your email address: '))
#         email_send(email_to)
#     elif inloop_variable == 3: # exit the program
#         print("\nBye!\n")
#         break
#     else:
#         # error message 
#         print("\nSorry, I don't recognise that input. Please try again.\n")
#         time.sleep(1)
#         inloop_variable == 0
# else:
#     if register_user == False and check_booking == False and inloop_variable == 0:
#         int(input("""\nService hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
#         # log_in()
#     else:
#         inloop_variable = 0



# register_user = False
# check_booking = False
# inloop_variable = 0
# user registration
if register_user == True:
    while inloop_variable == 1:
        new_user = get_user_info.CreateUser(input("Please enter your first name: "), 
                                            input("Please enter your last name: "), 
                                            input("Please enter your car registration number: "))
        user_response = int(input(f"Are these details correct?\n{new_user.__dict__}.\n 1 to continue. 2 to try again."))
        if user_response == 1:
            inloop_variable = 0
            print(f"Great! You're all set {new_user.first}") 
        else:
            inloop_variable = 1
            print("Ok, let's try that again.")
else:
    pass



# rego = []
# while register_user == True:
#     get_user_info.CreateUser()
#     user_input = str(input("Please enter your email address: "))
#     user_input = user_input.upper()
#     rego.append(user_input)
#     user_input = str(input("Please enter your password: "))
#     rego.append(user_input)
#     print(rego)

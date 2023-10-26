import datetime, ssl, smtplib, time, hashlib, email_system, get_user_info, purchase

# from get_user_info import CreateUser
from email.message import EmailMessage
from login_system import signup, login
from email_setup import my_password, my_email
# from email_system import EmailSend

today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%Y \n%-I:%M %p")

# Get time as int from datetime.datetime
today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

# Format date and time for display in Terminal
def time_date():
    print(formatted_date)

def welcome():
    if current_time.hour < 12:
        print("Good morning!\n")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!\n")
    else:
        print("Good evening!\n")

def login(email, pwd):
    with open("login_details.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and pwd == stored_pwd:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")

def register():
    i = 1
    while i == 1: #and register_user == True:
        email = input("Enter email address: ")
        password = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == password:
            with open("login_details.csv", "w") as f:
                    f.write(email + "\n" + password)
            f.close()
            print("You're now successfully registered.")
            new_user = get_user_info.CreateUser(email, 
                                                password,
                                                input("Please enter your first name: "), 
                                                input("Please enter your last name: "), 
                                                input("Please enter your car registration number: "))
            i = int(input(f"\nAre these details correct?\n{new_user.__dict__}.\n 1 to continue. 2 to try again."))
            if i == 1:
                with open("login_details.csv", "w") as f:
                    f.write(str(new_user.__dict__))
                    f.close()
                print(f"Thanks, {new_user.first}. Now you're ready to buy tickets.")
                break
                # purchase.payments()
            else:
                print("Ok, let's try that again.")
        else:
            print("\nPasswords don't match. Please start again.\n")
            time.sleep(1)

def open_menu():
    i = 0
    while i == 0 and 7 <= current_time.hour < 19:
        i = int(input("Welcome to the Parking Pal App\n\nPress 1 to register.\nPress 2 to signin.\nPress 3 if you forgot your password.\nPress 4 to exit.\n"))
        if i == 1: # register
            register()
            break
        elif i == 2: # signin
            break
        elif i == 3: # forgot password
            email_to = input('Please enter your email address: ')
            with open("login_details.txt", "r") as f: 
                stored_email, stored_pwd = f.read().split("\n")
            f.close()
            if email_to == stored_email:
                subject = "Forgot Password"
                body_text = (f"Hi, this is the Parking Pal App. Your Password is {stored_pwd}.")
                send = email_system.EmailSend(email_to, subject, body_text)
                print(f"Email has been sent to {email_to} with your password.")
                break
            else:
                print("Login failed. Try again. \n")
        elif i == 4: # exit the program
            print("\nBye!\n")
            break
        else:
            # error message 
            print("\nSorry, I don't recognise that input. Please try again.\n")
            time.sleep(1)
            inloop_variable == 0
    else:
        if i == 0:
            int(input("""\nService hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
            # log_in()
        else:
            inloop_variable = 0

time_date()
welcome()
open_menu()


import datetime, ssl, smtplib, time, hashlib, email_system, get_user_info, re, os, csv
from email.message import EmailMessage
from login_system import signup, login
from email_setup import my_password, my_email
from purchase import GetTime
from create_csv import create_csv

# Format date and time for display in Terminal
def time_date():
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")
    today_date = datetime.datetime.now()
    current_time = datetime.datetime.now()
    current_time.hour
    print(formatted_date)

# Display welcome menu upon opening the app
def welcome():
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("Good morning!\n")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!\n")
    else:
        print("Good evening!\n")

# Main menu that appears when opening the application
def open_menu():
    current_time = datetime.datetime.now()
    i = 0
    while i == 0 and 7 <= current_time.hour < 19:
        i = int(input("Welcome to the Parking Pal App\n\nPress 1 to register.\nPress 2 to signin.\nPress 3 if you forgot your password.\nPress 4 to exit.\n"))
        if i == 1: # register
            register()
        elif i == 2: # signin
            login()
        elif i == 3: # forgot password
            while True:
                email_to = input('Please enter your email address: ')
                with open("login_details.txt", "r") as f: 
                    stored_email, stored_pwd = f.read().split("\n")
                f.close()
                if email_to == stored_email:
                    i = 0
                    subject = "Forgot Password"
                    body_text = (f"Hi, this is the Parking Pal App. Your Password is {stored_pwd}.")
                    email_system.EmailSend(email_to, subject, body_text)
                    print(f"Email has been sent to {email_to} with your password.")
                    continue
                else:
                    a = int(input("That's not the email we have on record. 1 to try again, 2 to reregister 3 to return to main menu:...\n"))
                    while True:
                        try:
                            if a == 1:
                                print("Let's try again.")
                                break
                            elif a == 2:
                                register()
                            else:
                                intro()
                                break
                        except ValueError:
                            print("Numbers only, please.")
                        continue
                    else:
                        print("Thanks!")
                        time_date()
                        welcome()
                        open_menu()
        elif i == 4: # exit the program
            print("\nBye!\n")
            break
        else:
            # error message 
            print("\nSorry, I don't recognise that input. Please try again.\n")
            time.sleep(1)
            i == 0
    else: # Not in service at these hours
        if i == 0:
            int(input("""Service hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
        else:
            i == 0

# Function to buy tickets after the user has logged in. They'll have to enter a 16 digit credit card number and expiry date.
def get_ticket():
    valid_card = 0
    while valid_card == 0:
        try:
            cc = int(input("Please enter a fake 16 digit credit card number: "))
            if len(str(cc)) == 16:
                valid_card = 1
                continue
            else:
                print("Credit card must be 16 digits.")
        except ValueError:
            print("Numbers only, please.")
            continue
    time.sleep(0.5)
    print("You entered:", cc)
    valid_card = 1
    valid_month = 0
    while valid_month == 0:
        try:
            expiry_month = int(input("Please enter a 2 digit month (e.g. MM):"))
            if len(str(expiry_month)) == 2:
                valid_month = 1
                continue
            else:
                print("Must be 2 numbers long.")
        except ValueError:
            print("Numbers only, please.")
            continue
    time.sleep(0.5)
    print("You entered:", expiry_month)
    valid_month = 1
    valid_year = 0
    while valid_year == 0:
        try:
            expiry_year = int(input("Please enter a 2 digit year (e.g. YY):"))
            if len(str(expiry_year)) == 2:
                valid_year = 1
                continue
            else:
                print("Must be 2 numbers long.")
        except ValueError:
            print("Numbers only, please.")
            continue
    time.sleep(0.5)
    print("You entered:", expiry_year)
    print("Thank you. That looks good.")
    valid_year = 1
    valid_minutes = 0
    while valid_minutes == 0:
        try:
            minutes = int(input("Please enter the amount of minutes you'd like to purchase.\nMax purchase is 120 mins. Min purchase is 5 mins: "))
            if minutes >= 1:
                valid_minutes = 1
                continue
            else:
                print("Enter a number greater than 1.")
        except ValueError:
            print("Numbers only, please.")
            continue
    valid_minutes = 1
    details = get_user_info.CreateUser()
    receipt = GetTime(minutes)
    email_system.EmailSend("email", receipt,  details)
    time.sleep(3)
    intro()


def login():
    i = 1
    while i == 1:
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        with open("login_details.txt", "r") as f:
            stored_email, stored_pwd = f.read().split("\n")
            f.close()
        if email == stored_email and pwd == stored_pwd:
            print("Logged in Successfully!\nYou can now buy a ticket.")
            time.sleep(1)
            get_ticket() 
        else:
            i == 0
            answer = int(input("\nLogin failed! Try again?\n1 for yes 2 for no.\n:..."))
            if answer == 1:
                i == 1
            elif answer == 2:
                time_date()
                welcome()
                open_menu() 
            try:
                pass
            except Exception:
                print("Please enter a number value 1 or 2.")

def is_email_valid(email):
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def get_valid_email():
    while True:
        email = input("Enter email address: ")
        if is_email_valid(email):
            return email
        else:
            print("Not a valid email address. Try again.")

# Register the user email password and other details
def register():
    email = get_valid_email()
    password = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == password:
        with open("login_details.txt", "w") as f: # Save details as a list instead.
                f.write(email + "\n" + password)
        f.close()
        print("You're now successfully registered.")
        time.sleep(1)
    while True:
        new_user = get_user_info.CreateUser(email, 
                                            password,
                                            input("Please enter your first name: "), 
                                            input("Please enter your last name: "), 
                                            input("Please enter your car registration number: "))
        
        user_info = new_user.__dict__
        print("Here are your user details:\n")
        for key, value in user_info.items():
            print(f"{value}")
        i = int(input(f"\nAre these details correct?\n1 to continue.\n2 to try again: "))

        if i == 1:
            with open("login_details.csv", "w") as f:
                f.write(str(new_user.__dict__))
                f.close()
            print(f"Thanks, {new_user.first}. Now you're ready to buy tickets.")
            time.sleep(1)
            loggedin()
            return
        
        elif i == 2:
            print("Ok, let's try that again.")
            time.sleep(1)
            
        else:
            print("Sorry, I'm not sure what you meant.")
            pass
    else:
        print("\nPasswords don't match. Please try again.\n")
        time.sleep(1)

def loggedin():
    while True:
        # try:
            choice = int(input("To buy a ticket enter 1.\nTo log out enter 2."))
            if choice == 1:
                get_ticket()
            elif choice == 2:
                time_date()
                welcome()
                open_menu()
        # except ValueError:
        #     print("Invalid input. Please enter a valid number.")
        # except 

def intro():
    time_date()
    welcome()
    open_menu()

intro ()
# time_date()
# welcome()
# open_menu()


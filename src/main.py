import datetime
import time
import email_system
import get_user_info
import re
import csv
import os
from login_system import login
from purchase import GetTime


# Format date and time for display in a readable format. 
# This will also deisplay in a 12hr format instead of 24hr.
def time_date():
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")
    today_date = datetime.datetime.now()
    current_time = datetime.datetime.now()
    current_time.hour
    print(formatted_date)


# Find the current time and return the hour for
# comparison in conditional statements of my
# main.py file.
def get_current_time():
    current_time = datetime.datetime.now()
    return current_time


# Display welcome menu upon opening the application. 
# current_time.hour gets the current hour and uses that
# to make a comparison. Based on what time of day it is.
# If it's between 7pm and 7am the user won't be able to
# purchase any tickets 
def welcome():
    current_time = get_current_time()
    current_time.hour
    if current_time.hour < 12:
        print("Good morning!\n")
    elif 12 <= current_time.hour < 18:
        print("Good afternoon!\n")
    else:
        print("Good evening!\n")
    pass


# Main menu that appears when opening the application.
# Here the user is given 4 options. By entering the 
# corresponding number the user can navigate to a different 
# subsection. 1. Will navigate to a registration 
# section using the register function. 2. Will navigate
# to a signin section with the signin function.
# 3. Will navigate to a a forgot passord section.
# The user will have to enter a password that matches
# one that was created on signup. If the email doesn't
# match or there isn't a user created yet then you'll
# be prompted to create a new one.
def open_menu():
    current_time = get_current_time()
    i = 0
    while i == 0 and 7 <= current_time.hour < 19:
        try:
            time_date()
            welcome()
            i = int(input("""Welcome to the Parking Pal App\n
Press 1 to register.
Press 2 to sign in.
Press 3 if you forgot your password.
Press 4 to exit.\n:..."""))
            
            while i < 0:
                print("Please enter a positive number.")
                i = int(input("Enter 1 to register, or 2 to quit: "))
            
            if i == 1:  # register
                register()
            elif i == 2:  # sign in
                login()
            elif i == 3:  # forgot password
                while True:
                    email_to = input('Please enter your email address: ')
                    with open("login_details.txt", "r") as f:
                        stored_email, stored_pwd = f.read().split("\n")
                    f.close()
                    if email_to == stored_email:
                        i = 0
                        subject = "Forgot Password"
                        body_text = (f"""Hi, this is the Parking Pal App.
Your Password is {stored_pwd}.""")
                        email_system.EmailSend(email_to, subject, body_text)
                        print(f"""Email has been sent to
    {email_to} with your password.""")
                        intro()
                        break
                    else:
                        a = int(input("""That's not the email we have on record.
1 to try again, 2 to reregister 3 to return to main menu:...\n"""))
                        while a == 1 or 2:
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
                                ("Enter number 1, 2 or 3.")
            elif i == 4:  # exit the program
                print("\nBye!\n")
                exit()
            else:
                print("""\nSorry, I don't recognize that input.
Please try again.\n""")  # error message
                time.sleep(1)
        except ValueError:
            print("\nOnly numbers accepted.")
            i == 0
            time.sleep(0.5)
    else:
        while True:
            try:
                i = int(input("""Service is closed from 7:00pm to 7:00am.
Enter 1 to register. Enter 2 to quit.\n:..."""))
                if i == 1:
                    register()
                    print("Goodbye!")
                    exit()
                else:
                    print("Goodbye!")
                    exit()
            except ValueError:
                print("Must enter a number.")
            pass


# This login function handles the login process. Firstly, the user
# must input a valid email that matches the one stored locally.
# on login_details.txt. Next, the user must enter a password that
# matches the one stored locally. If both of them match login will 
# succeed. While the user does not meet these requirements, the code
# loops, giving them another opportunity to match the email and 
# passwor. Else they want to break out of the loop and return
# to the main menu. If the user can satisy the requirements,
# they'll pass to the next while loop.


# def login():
    while True:
        email = get_valid_email()
        pwd = input("Please enter your password:")

        try:
            with open("login_details.csv", "r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    stored_email = row["email"]
                    stored_pwd = row["password"]
                    
        except FileNotFoundError:
            print("Error: File 'login_details.csv' not found.")

        if email == stored_email and pwd == stored_pwd:
            print("Logged in Successfully!\nYou can now buy a ticket.")
            time.sleep(1)
            get_ticket()
            break  # Exit the loop on successful login
        else:
            answer = input("\nLogin failed! Try again? (1 for yes, 2 for no): ")
            try:
                answer = int(answer)
                if answer == 1:
                    continue  # Retry login
                elif answer == 2:
                    intro()
                    break  # Exit the loop on user's choice
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Please enter a number value (1 or 2).")
            pass


def login():
    stored_email = None
    stored_pwd = None
    
    while True:
        email = get_valid_email()
        pwd = input("Please enter your password:")

        try:
            with open("login_details.csv", "r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    if 'email' in row and 'password' in row:
                        stored_email = row['email']
                        stored_pwd = row['password']
                        break  # Only read the first row
        except FileNotFoundError:
            print("Error: File 'login_details.csv' not found.")
            return  # Exit the function
        email = email.strip()
        pwd = pwd.strip()
        stored_email = stored_email.strip()
        stored_pwd = stored_pwd.strip()
        if email == stored_email and pwd == stored_pwd:
            print("Logged in Successfully!\nYou can now buy a ticket.")
            time.sleep(1)
            get_ticket()
            break  # Exit the loop on successful login
        else:
            answer = input("\nLogin failed! Try again? (1 for yes, 2 for no): ")
            try:
                answer = int(answer)
                if answer == 1:
                    continue  # Retry login
                elif answer == 2:
                    intro()
                    break  # Exit the loop on the user's choice
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Please enter a number value (1 or 2).")


def get_ticket():
    valid_card = 0
    while valid_card == 0:
        try:
            cc = int(input("Please enter a 16 digit credit card number: "))
            if len(str(cc)) == 16:
                valid_card = 1
            else:
                print("Credit card must be 16 digits.")
        except ValueError:
            print("Numbers only, please.")
        pass

    time.sleep(0.5)
    print("You entered:", cc)
    valid_card = 1

    valid_month = 0
    while valid_month == 0:
        try:
            expiry_month = input("Please enter a 2-digit month (e.g., MM): ")
            
            if len(expiry_month) == 2 and expiry_month.isdigit():
                expiry_month = int(expiry_month)
                if 1 <= expiry_month <= 12:
                    valid_month = 1
                else:
                    print("Invalid input. Please enter a valid 2-digit month between 01 and 12.")
            else:
                print("Invalid input. Please enter a valid 2-digit month in the format '01' to '12'.")
        except ValueError:
            print("Numbers only, please.")
        pass
        
    time.sleep(0.5)
    print("You entered:", expiry_month)
    valid_month = 1

    valid_year = 0
    while valid_year == 0:
        try:
            expiry_year = int(input("Please enter a 2-digit year (e.g., YY): "))
            
            if len(str(expiry_year)) == 2 and 23 <= expiry_year <= 99:
                valid_year = 1
            else:
                print("Invalid input. Please enter a 2-digit year greater than or equal to 23.")
        except ValueError:
            print("Numbers only, please.")  

    time.sleep(0.5)
    print("You entered:", expiry_year)
    print("Thank you. That looks good.")
    valid_year = 1

    valid_minutes = 0
    while valid_minutes == 0:
        try:
            minutes = int(input("""Please enter the amount of
minutes you'd like to purchase.
Max purchase is 120 mins. Min purchase is 5 mins: """))
            if 5 <= minutes <= 120:  # Check for a valid range
                valid_minutes = 1
            else:
                print("Enter a number between 5 and 120.")
        except ValueError:
            print("Numbers only, please.")

    valid_minutes = 1
    GetTime(minutes)
    time.sleep(3)
    intro()

# Use Regular Expressions (re) module to check whether the
# email address is legitimate.
def is_email_valid(email):
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                        email))


# using the is_email_valid function first check the email, then it is
# passed to the get_valid_email function which will loop until a
# the email passes validation. 
def get_valid_email():
    while True:
        email = input("Enter email address: ")
        if is_email_valid(email):
            return email
        else:
            print("Not a valid email address. Try again.")
        pass


def validate_password(email):
    while True:
        password = input("Enter password: ")
        
        if 6 <= len(password) <= 12:
            conf_pwd = input("Confirm password: ")
            if conf_pwd == password:
                with open("login_details.txt", "w") as f:
                    f.write(email + "\n" + password + "\n")
                print("You're now successfully registered.")
                time.sleep(0.5)
                return password
            else:
                print("\nPasswords don't match. Please try again.\n")
                time.sleep(0.5)
        else:
            print("Password must be between 6 and 12 characters long.")


def create_csv():
    records_filename = "login_details_enhanced.csv"
    def create_records_csv(records_filename):
        if not os.path.exists(records_filename):
            with open(records_filename, 'w', newline="") as file:
                csvwriter = csv.writer(file)
                print("Creating a header row for the file")
                csvwriter.writerow([
                    "email",
                    "password", 
                    "first", 
                    "last", 
                    "rego", 
                    "ticket",
                ])
                print(f"Created a .CSV file to store employee data named {records_filename}")
        else:
            pass
    create_records_csv(records_filename)


def register():
    email = get_valid_email()
    password = validate_password(email)
    while True:
        new_user = get_user_info.CreateUser(email,
                                            password,
                                            input("Please enter first name: "),
                                            input("Please enter last name: "),
                                            input("Please enter registration number: "))
        user_info = new_user.__dict__
        print("Here are your user details:\n")
        for key, value in user_info.items():
            print(f"{value}")
        while True:
            try:
                i = int(input(f"""
Are these details correct?\n1 to continue.\n2 to try again: """))
                if i == 1:
                    with open("login_details.csv", "w") as f:
                        f.write(str(new_user.__dict__))
                        f.close()
                    print(f"Thanks, {new_user.first}.")
                    current_time = get_current_time()
                    if 7 <= current_time.hour < 19:
                        loggedin()
                    else:
                        intro()
                    break
                elif i == 2:
                    print("Ok, let's try that again.")
                    time.sleep(1)
                    break
                else:
                    print("Sorry, please enter either 1 to continue or 2 to try again.")
            except ValueError:
                print("Sorry, please enter either 1 to continue or 2 to try again.")


def loggedin():
    while True:
        try:
            choice = int(input("To buy tickets enter 1\nTo log out enter 2\n"))
            if choice == 1:
                get_ticket()
            elif choice == 2:
                intro()
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def intro():
    open_menu()


intro()

# if __name__ == "__main__":
#   intro()
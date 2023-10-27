import datetime, ssl, smtplib, time, hashlib, email_system, get_user_info, re
from email.message import EmailMessage
from login_system import signup, login
from email_setup import my_password, my_email
from purchase import GetTime

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
            break
        elif i == 2: # signin
            login()
            break
        elif i == 3: # forgot password
            email_to = input('Please enter your email address: ')
            with open("login_details.txt", "r") as f: 
                stored_email, stored_pwd = f.read().split("\n")
            f.close()
            if email_to == stored_email:
                subject = "Forgot Password"
                body_text = (f"Hi, this is the Parking Pal App. Your Password is {stored_pwd}.")
                email_system.EmailSend(email_to, subject, body_text)
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
            i == 0
    else:
        if i == 0:
            int(input("""Service hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
            # log_in()
        else:
            i == 0

# Function to buy tickets after the user has logged in. They'll have to enter a 16 digit credit card number and expiry date.
def get_ticket():
    while True:
            cc = input("Please enter a fake 16 digit credit card number: ")
            if len(cc) != 16:
                print("Credit card must be 16 digits. Try again?")
                choice = input("1 for yes, 2 for no: ")
                if choice == '2':
                    break
            try:
                cc = int(cc)
            except ValueError:
                print("Numbers only, please.")
                continue
            time.sleep(1)
            print("You entered:", cc)
            while True:
                    expiry_month = int(input("Please enter a 2 digit month (e.g. MM):"))
                    if type(expiry_month) == int and len(expiry_month) == 2:
                        expiry_year = int(input("Please enter a 2 digit year (e.g. YY):"))
                        if type(expiry_year) == int and len(expiry_year) == 2:
                            print("Thank you.")
                            minutes = int(input("Please enter the amount of minutes you'd like to purchase.\nMax is 120 mins. Min is 5 mins: "))
                            answer = int(input(f"Is this the corect amount of minutes? {minutes}\n1 for yes or 2 for no."))
                            if answer == 1:
                                print("You havea total of {minutes}")
                                GetTime(minutes)
                                # Get the user details from login_details.csv and send the receipt of purchase
                            else:
                                print("Ok, let's try again!")
                        try:
                            expiry_month = int
                        except ValueError:
                            print("Sorry, please enter numbers only in the correct format.")
                            continue
                    try:
                        expiry_month = int
                    except ValueError:
                        print("Sorry, please enter numbers only in the correct format.")
                        continue
                    else:
                        print("\nThank you. Have a great day!")
                        time_date()
                        welcome()
                        open_menu()
                    
    
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

def is_email_valid (email):
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
    while True:
        password = input("Enter password: ")
        conf_pwd = input("Confirm password: ")
        if conf_pwd == password:
            with open("login_details.csv", "w") as f:
                    f.write(email + "\n" + password)
            f.close()
            print("You're now successfully registered.")
            time.sleep(1)

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
                
            else:
                print("Sorry, I'm not sure what you meant.")
                pass
        else:
            print("\nPasswords don't match. Please try again.\n")
            time.sleep(1)



def loggedin():
    while True:
        try:
            choice = int(input("To purchase a parking ticket, please enter 1.\nTo log out, please enter 2."))
            if choice == 1:
                get_ticket()
            elif choice == 2:
                time_date()
                welcome()
                open_menu()
        except ValueError:
            print("Invalid input. Please enter a valid number.")

time_date()
welcome()
open_menu()


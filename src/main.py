import datetime, ssl, smtplib, time, hashlib, email_system, get_user_info

# from get_user_info import CreateUser
from email.message import EmailMessage
from login_system import signup, login
from email_setup import my_password, my_email
from purchase import GetTime


# Format date and time for display in Terminal
def time_date():
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")
    # Get time as int from datetime.datetime
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

def login():
    i = 1
    while i == 1:
        email = input("Enter email address: ")
        pwd = input("Enter password: ")
        with open("login_details.txt", "r") as f:
            stored_email, stored_pwd = f.read().split("\n")
            f.close()
        if email == stored_email and pwd == stored_pwd:
            print("Logged in Successfully!")
            time_date()
            welcome()
            open_menu()  
        else:
            i == 0
            answer = int(input("\nLogin failed! Try again?\n1 for yes 2 for no.\n:..."))
            if answer == 1:
                i == 1
            elif answer == 2:
                time_date()
                welcome()
                open_menu() 
            else:
                pass

def register():
    i = 0
    while i == 0: #and register_user == True:
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
            i = int(input(f"\nAre these details correct?\n{new_user.__dict__}.\n1 to continue. 2 to try again."))
            if i == 1:
                with open("login_details.csv", "w") as f:
                    f.write(str(new_user.__dict__))
                    f.close()
                print(f"Thanks, {new_user.first}. Now you're ready to buy tickets.")
                return
            while i == 2:
                print("Ok, let's try that again.")
                
            else:
                print("Sorry, I'm not sure what you meant.")
                pass
        else:
            print("\nPasswords don't match. Please start again.\n")
            time.sleep(1)

def get_ticket():
        while True:
            user_input = 1
            cc =  int(input("Please enter a fake 16 digit credit card number:"))
            print("You entered:", cc)
            if len(cc) != 16 or cc != type(int):
                user_input = input("Credit card must be 16 numbers. Try again? 1 for yes 2 for no.")
            elif ValueError:
                print("Numbers only, please.")
            else:
                print("Looks good")
                input("Please enter a fake expiry date e.g. MM/YY:")
                GetTime(round(int(input("Please enter the amount of minutes you'd like to purchase.\nMax is 120 mins.\nMin is 5 mins."))))
                print("\nThank you. Have a great day.")



#get_ticket()
time_date()
welcome()
open_menu()


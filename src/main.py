import datetime, ssl, smtplib, time, get_user_info, hashlib, email_system
from email.message import EmailMessage
from email_setup import my_password, my_email
# from email_system import EmailSend

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
signin_user = False
inloop_variable = 0

while inloop_variable == 0 and 7 <= current_time.hour < 24:
    inloop_variable = int(input("Welcome to the Parking Pal App\n\nPress 1 to register.\nPress 2 to signin.\nPress 3 if you forgot your password.\nPress 4 to exit.\n"))
    if inloop_variable == 1: # go to registration set up
        register_user = True
        break
    elif inloop_variable == 2: # go to check booking and email time remaining to self
        signin_user = True
        break
    elif inloop_variable == 3: # to get password
        email_to = input('Please enter your email address: ')
        # email = input("Enter email: ")
        with open("credentials.csv", "r") as f:
            stored_email, stored_pwd = f.read().split("\n")
            auth_hash = hashlib.md5(stored_pwd).hexdigest()
            auth = auth_hash.digest()
            password = auth
        f.close()
        if email_to == stored_email:
            subject = "Forgot Password"
            body_text = (f"Hi, this is the Parking Pal App. Your Password is {stored_pwd}.")
            send = email_system.EmailSend(email_to, subject, body_text)
            print(f"Email has been sent to {email_to} with your password.")
            break
        else:
            print("Login failed. Try again. \n")

    elif inloop_variable == 4: # exit the program
        print("\nBye!\n")
        break
    else:
        # error message 
        print("\nSorry, I don't recognise that input. Please try again.\n")
        time.sleep(1)
        inloop_variable == 0
else:
    if register_user == False and signin_user == False and inloop_variable == 0:
        int(input("""\nService hours are closed from 7:00pm to 7:00am.\nTo update your user details press 1\n:..."""))
        # log_in()
    else:
        inloop_variable = 0


# user registration

while register_user == True:
    email = input("Enter email address: ")
    password = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == password:
        new_user = get_user_info.CreateUser(email, 
                                            password,
                                            input("Please enter your first name: "), 
                                            input("Please enter your last name: "), 
                                            input("Please enter your car registration number: "))
        user_response = int(input(f"\nAre these details correct?\n{new_user.__dict__}.\n 1 to continue. 2 to try again."))
        if user_response == 1:
            inloop_variable = 0
            with open("credentials.csv", "w") as f:
                f.write(str(new_user.__dict__))
                f.close()
            print(f"Thanks, {new_user.first}. Now you're ready to buy tickets.") 
        else:
            inloop_variable == 1
            print("Ok, let's try that again.")
        pass
        # enc = conf_pwd.encode()
        # hash1 = hashlib.md5(enc).hexdigest()
        # with open("credentials.csv", "w") as f:
        #     f.write(email + "\n" + hash1)
        #     f.write(hash1)
        # f.close()
        # print("You're now successfully registered.")
    else:
        register_user == False
        print("\nPasswords don't match. Please start again.\n")
        time.sleep(1)
        
else: 
    signin_user = True
    email = input("Enter email: ")
    password = input("Enter password: ")
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.csv", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("You've logged in.")
    else:
        print("Login failed. Try again. \n")



# rego = []
# while register_user == True:
#     get_user_info.CreateUser()
#     user_input = str(input("Please enter your email address: "))
#     user_input = user_input.upper()
#     rego.append(user_input)
#     user_input = str(input("Please enter your password: "))
#     rego.append(user_input)
#     print(rego)

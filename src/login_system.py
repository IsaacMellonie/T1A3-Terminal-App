import hashlib, csv


def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        with open("login_details.txt", "w") as f:
            f.write(email + "\n")
            f.write(pwd)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")

def login(email, pwd):
    with open("login_details.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
        f.close()
    if email == stored_email and pwd == stored_pwd:
        print("Logged in Successfully!")
    else:
        print("Login failed! \n")


# while 1:
#     print()
#     print("1.Signup")
#     print("2.Login")
#     print("3.Exit")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         signup()
#     elif ch == 2:
#         login()
#     elif ch == 3:
#         break
#     else:
#         print("Wrong Choice!")


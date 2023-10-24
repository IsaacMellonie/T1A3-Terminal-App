import hashlib, time, csv

def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.csv", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close()
        print("You're now successfully registered.")
    else:
        print("\nPasswords don't match.\n")
        time.sleep(1)

def log_in():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.csv", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("You've logged in.")
    else:
        print("Login failed. Try again. \n")

while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        log_in()
    elif ch == 3:
        print("\nBye!\n")
        break
    else:
        print("Wrong Choice!")


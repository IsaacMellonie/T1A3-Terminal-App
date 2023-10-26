class CreateUser:
    def __init__(self, email, password, first, last, rego):
        self.email = email
        self.password = password
        self.first = first
        self.last = last
        self.rego = rego

    def user_info(self):
        print(f"{self.email}")
        print(f"{self.password}")
        print(f"{self.first}")
        print(f"{self.last}")
        print(f"{self.rego}")
        return

        # with open("credentials.csv", "w") as f:
        #     f.write(user_info.__dict__)
        # f.close()
        # print("You're now successfully registered.")



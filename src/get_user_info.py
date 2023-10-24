class CreateUser:
    def __init__(self, first, last, rego):
        self.first = first
        self.last = last
        self.rego = rego

    inloop_variable = 1
    details = []
    while inloop_variable == 1:
        first = input("Please enter your first name: ")
        last = input("Please enter your last name: ")
        rego = input("Please enter your car registration number: ")
        user_response = int(input(f"Are these details correct?\n{first} {last}, {rego}.\n 1 to continue. 2 to try again."))
        if user_response == 1:
            inloop_variable = 0
            print("Great! You're all set.") 
        else:
            inloop_variable = 1
            print("Ok, let's try that again.")
            

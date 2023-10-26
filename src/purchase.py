import datetime
from datetime import timedelta

today_date = datetime.datetime.now()
formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")

today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

# now = datetime.datetime.now()
# new_time = now + timedelta(minutes = 10)
# formatted_date = new_time.strftime("\n%d/%m/%Y \n%-I:%M %p")
# print(formatted_date)

class GetTime():
    def __init__(self, time):
        if 5 >= time:
            time = 5
        elif 120 <= time:
            time = 120

        now = datetime.datetime.now()
        new_time = now + timedelta(minutes = time)
        formatted_date = new_time.strftime("\n%d/%m/%Y \n%-I:%M %p")
        print(formatted_date)

        


    

    

# purchase_amount = round(int(input("Please enter the amount of minutes you'd lile to purchase.\nMax is 120 mins.\nMin is 5 mins.")))
amount = GetTime(round(int(input("Please enter the amount of minutes you'd like to purchase.\nMax is 120 mins.\nMin is 5 mins."))))

    



def get_price():
    if 19 <= current_time.hour:
     pass

import datetime
from datetime import timedelta

class GetTime():
    today_date = datetime.datetime.now()
    formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")
    today_date = datetime.datetime.now()
    current_time = datetime.datetime.now()
    current_time.hour
    def __init__(self, time):
        if 5 >= time:
            print("Number less than 5. Rounding up.")
            time = 5
        elif 120 <= time:
            print("Number more than 120. Rounding down.")
            time = 120
        charge = time * 0.25
        tax = time * 0.11
        total = tax + charge
        total_formatted = "{:.2f}".format(total)
        now = datetime.datetime.now()
        new_time = now + timedelta(minutes = time)
        formatted_date = new_time.strftime(f"--------------\n--------------\nTOTAL\n{time} minutes\n------------\nVALID UNTIL\n%d/%m/%Y\n%-I:%M %p\n\nCHARGE: ${total_formatted}\n--------------\n--------------")
        print(f"{formatted_date}\nThank you!")


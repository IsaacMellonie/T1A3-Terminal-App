import datetime
from datetime import timedelta

today_date = datetime.datetime.now()
formatted_date = today_date.strftime("\n%d/%m/%Y \n%-I:%M %p")

today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour

class GetTime():
    def __init__(self, time):
        if 5 >= time:
            time = 5
        elif 120 <= time:
            time = 120

        now = datetime.datetime.now()
        new_time = now + timedelta(minutes = time)
        formatted_date = new_time.strftime("-----------\n%d/%m/%Y \n%-I:%M %p\n-----------")
        print(f"Your purchase will expire on\n{formatted_date}")

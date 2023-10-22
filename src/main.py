import datetime


today_date = datetime.datetime.now()
formatted_date = today_date.strftime("%d/%m/%y \n%X %p")
print(formatted_date)

today_date = datetime.datetime.now()
current_time = datetime.datetime.now()
current_time.hour


if current_time.hour < 12:
    print("Goodmorning!")
elif 12 <= current_time.hour < 18:
    print("Good Afternoon!")
else:
    print("Good evenning!")
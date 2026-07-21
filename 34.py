
#This allows us to work with date and time using our system's clock.
import datetime

#To print out a date
date = datetime.date(2026, 7, 21)
#To print out the current date we use .now
today = datetime.date.today()

#To work with time, we'll use the time method
time = datetime.time(12,30, 0)
#To get the current time on our system clock this return a date and a time
now = datetime.datetime.now()

#To format the appearance of the string, w use the now.strftime method
now = now.strftime("%H: %M: %S %m: %d: %Y")

target_datetime = datetime.datetime(2026, 7, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed.")
else:
    print("Target date has not passed.")

#print(date)
#print(today)
#print(time)
#print(now)

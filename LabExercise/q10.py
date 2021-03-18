'''write a program to convert seconds to days, hours, minutes, and days'''

user_seconds = int(input("enter the seconds you want to convert:"))
seconds_into_minutes = user_seconds//60
seconds_into_hours = seconds_into_minutes//60
seconds_into_days = seconds_into_hours//24
print(f"the number of minutes is {seconds_into_minutes}")
print(f"the number of hours is {seconds_into_hours}")
print(f"the number of days is {seconds_into_days}")

# given the integer N- the number of minutes that is passed since midnight -
how many hours and minutes are displayed on the 24th digital clock?
the program should print two numbers: the number of hours (between 0 and 23)
and the number of minutes (between 0 and 59)
for example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am.
so, the program should print 2 30,

N = int(input("Enter the minutes passed since midnight: "))
hours = (N//60)
minutes = (N%60)
print(f"the hours is {hours} ")
print(f"the minutes is {minutes} ")
print(f"its {hours}:{minutes} now")
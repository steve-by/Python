# Import the datetime module and display the current date:
import datetime

# x = datetime.datetime.now()
# print(x) 

# Return the year and name of weekday:
# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A")) 

x = datetime.datetime.now()

print(x.strftime("%A, %dth %B %Y")) # day, date, month, year

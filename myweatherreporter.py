"""
1) Add the project title and file name.
   a) Use comments to label the program as "My Weather Reporter".
   b) Mention the file name as `my-weather-reporter.py`.

2) Take user input.
   a) Ask the user to enter their city name.
   b) Ask the user to enter today’s temperature.
   c) Convert the temperature input into a float.

3) Use an `if` statement.
   a) Check if the temperature is above 35.
   b) Print a warning message if it is very hot.

4) Use an `if-else` statement.
   a) Check if the temperature is above 25.
   b) Print an outdoor message if it is warm.
   c) Otherwise, print a jacket reminder.

5) Use an `if-elif-else` statement.
   a) Show "Scorching Hot" for temperatures above 35.
   b) Show "Warm and Sunny" for temperatures above 25.
   c) Show "Cool and Breezy" for temperatures above 15.
   d) Otherwise, show a cold weather message.

6) Import date and calendar modules.
   a) Import `datetime` to get the current date and time.
   b) Import `calendar` to display the yearly calendar.

7) Print the final weather report.
   a) Show the city name.
   b) Show the current date and time.
   c) Show the calendar for the current year.
"""

city =input("Enter your city name: ")
temperature = input("Enter today's temperature:")
temperature = float(temperature)

if temperature > 35:
    print("Warning: It is very hot today!")

elif temperature > 25:
        print("It's warm outside, enjoy your day!")

elif temperature > 15:
        print("It's cool outside, don't forget your jacket!")

else:
        print("It's quite cold outside, bundle up!")

import datetime 
import calendar

today = datetime.datetime.now()
print(f"Weather Report for {city} on {today}")
print(f"Current Temperature: {temperature}°C")
print(today)
print(calendar.calendar(today.year))


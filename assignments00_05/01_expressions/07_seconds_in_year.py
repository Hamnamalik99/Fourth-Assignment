# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice
#  print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes 
# in an hour, and 60 seconds per minute.

# Define constants
DAYS_IN_YEAR = 365  # Number of days in a year
HOURS_IN_DAY = 24  # Number of hours in a day
MINUTES_IN_HOUR = 60  # Number of minutes in an hour
SECONDS_IN_MINUTE = 60  # Number of seconds in a minute

# Calculate the total number of seconds in a year
seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

# Print the result in a nice format
print(f"There are {seconds_in_year} seconds in a year!")



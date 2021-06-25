# function to determine leap year in the gregorian calendar
# if a year is leap year, return Boolean true, otherwise return false
# if year is evenly divided by 4, then its a leap year
# if year is not evenly divided by 100 its not a leap year
# if year is evenly divided by 400 then its a leap year
# In the Gregorian Calendar, years 2000 and 2400 are leap years, while 1800,1900,2100,2200,2300 and 2500 are not leap years

def leap_year():
    year = int(input("Input any year: "))
    if (year % 4 == 0):
      if (year % 100 == 0):
        if (year % 400 == 0):
            print("It's a leap year")
        else:
            print("It's not a leap year")
      else:
        print("It's a leap year")
    else:
        print("It's not a leap year")

leap_year()

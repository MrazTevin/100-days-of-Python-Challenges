# function to determine leap year in the gregorian calendar
# if a year is leap year, return Boolean true, otherwise return false
# if the year can be evenly divided by 4, it's a leap year, unless: The year can be evenly divided by 100 it is# not a leap year,unless the year is also divisible by 400, then its a leap year
# In the Gregorian Calendar, years 2000 and 2400 are leap years, while 1800,1900,2100,2200,2300 and 2500 are not leap years

def leap_year(year):
    if (year%4==0 and year%100!=0):
        return True
    elif (year%100==0 and year%400==0):
        return True
    else:
        return False
yearInput = int(input("Enter any year i.e 2001 :"))
print(leap_year(yearInput))

#Age Calculator
import datetime    #Library to get current year
birth_year=int(input("Enter your birth year:"))#user input
age=datetime.datetime.now().year-birth_year  #current year - birth year = age
#Display Details
print("Current age:",age)
print("Current age in Months:",age*12)
print("Current age in Days:",age*365)
print("Current age in Hours:",age*365*24)
print("Current age in Mins:",age*365*24*60)
print("Years until age 100:",100-age)


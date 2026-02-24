# Leap Year Checker
year=int(input("Enter required year:"))   #user input
if year%4!=0:
    print("Not a leap year as not divisible by 4")  #check condition divisible by 4
    
elif year%100!=0:
    print("Leap year divisible by 4 but not 100")    #check condition divisible by 100
  
elif year%400==0:
    print("Year is a leap year as its divisible by 100 and 400")#check condition divisible by 400
  
else:
    print("Year is not a leap year as its divisible by 100 but not 400")#check condition divisible by 4
  
            
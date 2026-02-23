# Temperature Converter
while(True): #loop to repeat until exit
    #Menu Of conversion options
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1: #Celsius to Fahrenheit
        c=int(input("Enter Temp in Celcius:"))
        f=(c * 9/5) + 32
        print("Temperature in Fahrenheit is:",f)
    elif choice==2:#Fahrenheit to Celsius
        f=int(input("Enter Temp in Fahrenheit:"))
        c= (f - 32) * 5/9
        print("Temperature in Celsius is:",c)
    elif choice==3:#Celsius to Kelvin
        c=int(input("Enter Temp in Celsius:"))
        k= c + 273.15
        print("Temperature in Kelvin is:",k)
    elif choice==4:#Kelvin to Celsius
        k=int(input("Enter Temp in Kelvin:"))
        c=  k - 273.15
        print("Temperature in Celsius is:",c)
    elif choice==5:#Fahrenheit to Kelvin
        f=int(input("Enter Temp in Fahrenheit:"))
        k=  (f - 32) * 5/9 + 273.15
        print("Temperature in Celsius is:",k)
    elif choice==6:#Kelvin to Fahrenheit
        k=int(input("Enter Temp in Kelvin:"))
        f=  (k - 273.15) * 9/5 + 32
        print("Temperature in Celsius is:",f)
    elif choice==7:# Exit Statement
        print("Exit")
        break
    else: #Error edgecase
        print("Error")
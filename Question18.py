#Calculator Functions
def add(a, b): #addition functions
    print(a,"+",b,"=",a+b)
def subtract(a, b): #subtraction function
    print(a,"-",b,"=",a-b)
def multiply(a, b): #product function
    print(a,"X",b,"=",a*b)
def divide(a, b): #Division Function
    if b!=0:
        print(a,"/",b,"=",a/b)
    else:
        print("Cant divide by 0")
def modulus(a, b): #modulus function
    if b!=0:
        print(a,"%",b,"=",a%b)
    else:
        print("Cant divide by 0")
def power(a, b): #power function
    print(a,"^",b,"=",a**b)
    
def calculator(): #Menu function
    ch=0
    while(ch!=7):
        a=int(input("Enter first number:"))  #User input 1
        b=int(input("Enter second number:")) #user input 2
        #Menu
        print( "1. add(a, b)")
        print( "2. subtract(a, b)")
        print( "3. multiply(a, b)")
        print( "4. divide(a, b) - handle division by zero")
        print( "5. modulus(a, b)")
        print( "6. power(a, b))")
        print( "7 Exit")
        ch=int(input("Enter your choice"))
        if ch==1:
            add(a,b)
        elif ch==2:
            subtract(a,b)
        elif ch==3:
            multiply(a,b)
        elif ch==4:
            divide(a,b)
        elif ch==5:
            modulus(a,b)
        elif ch==6:
            power(a,b)
        elif ch==7:
            print("Exit")
        elif ch>=7 or ch<=0:
            print("Error")

calculator()
n1=int(input("Enter first number:")) #User input 1
n2=int(input("Enter second number:")) #User input 2
print(n1,"+",n2," =", n1+n2) #Addition
print(n1,"-",n2," =", n1-n2) #Subtraction
print(n1,"*",n2," =", n1*n2) #Multiplication
if n2!=0: #Check to see if it is dividing by 0
    print(n1,"/",n2," =", n1/n2) #Division
    print(n1,"%",n2," =", n1%n2) #Modulus
else:
    print("divisor cannot be 0")
print(n1,"^",n2," =", n1**n2) ##Exponent
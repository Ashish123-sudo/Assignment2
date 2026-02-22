n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
print(n1,"+",n2," =", n1+n2)
print(n1,"-",n2," =", n1-n2)
print(n1,"*",n2," =", n1*n2)
if n2!=0:
    print(n1,"/",n2," =", n1/n2)
    print(n1,"%",n2," =", n1%n2)
else:
    print("divisor cannot be 0")
print(n1,"^",n2," =", n1**n2)

# Multiplication Table Generator
a=int(input("Enter a number:"))    #number to find table of
b=int(input("Enter range (end):"))  #range to find till
print("Multiplication Table of",a)
for i in range(1,b+1):  #loop to find and display
    print(a,"X",i,"=",a*i)
    
    
print("----------------------------------------------------")
#Multiplication table of 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    print("----------------------------------------------------")
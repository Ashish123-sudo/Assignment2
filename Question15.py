# Prime Number Checker

#single prime checker
no=int(input("Enter a number:"))
if no<=2:
    print("Please enter number above 2")
else:
    flag=0
    for i in range(2,no):
        if no%i==0: #looping to check if no is divisible
            flag=1
            break
    if flag==0:  #check if flag represent prime
        print(no,"is a prime no")
    else:
        print(no,"is not a prime no")
    
#Displaying prime numbers between range
sr=int(input("Enter start range:"))
er=int(input("Enter end range:"))
l=[]

for i in range(sr,er):  #loop between range
    flag=0
    for j in range(2,i): #loop numbers to divide to check 
        if i%j==0 :
            flag=1
            break
    if flag==0 and i!=1:
        l.append(i)
    
print(*l)
        
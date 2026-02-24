# Factorial Calculator
num=int(input("Enter a number:"))
if num<=0:     #handeling 0 and negative numbers
    print("Enter number greater than 0:")
else:
    fact=1
    l=[]
    for i in range(1,num):  #finding factorial
        fact*=i
        l.append(i)
    print(num,"! =",end="")
    print(*l,sep=' x ',end="")   #displaying steps
    print(" =",fact)             #display answer
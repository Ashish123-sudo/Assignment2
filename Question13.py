#Sum and Average Calculator
no=int(input("How many numbers?"))  #number of elements to enter
l=[]
for i in range(no):
    print("Enter number",i+1,":")  #entering each element
    n=int(input())
    l.append(n)
summ=sum(l)  #computing sum
avg=summ/no   #computing average   
print("Sum:",summ)
print("Average:",avg)
print("Maximum:",max(l))   #dispaly maximum
print("Minimum:",min(l))   #display minimum
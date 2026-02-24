# Number Pattern Printer
#Menu
print("Pattern 1")
print("Pattern 2")
print("Pattern 3")
print("Pattern 4")
#user input
ch = int(input("Choose pattern (1-4): "))
ht = int(input("Enter height: "))
if ch==1: #pattern 1
     for i in range(1, ht + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
elif ch==2: #pattern 2
    for i in range(1, ht + 1):
        for j in range(i):
            print(i, end=" ")
        print()
elif ch==3: #pattern 3
    for i in range(ht, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
elif ch==4: #pattern 4
    for i in range(1, ht + 1):
        
        # ascending part
        for j in range(1, i + 1):
            print(j, end="")
        
        # descending part
        for j in range(i - 1, 0, -1):
            print(j, end="")
        
        print()

else: #wrong chpice
    print("Error")

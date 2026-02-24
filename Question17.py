# Palindrome Checker
item=input("Enter word or number:")  #User input
print("Original:",item)

if item.isalpha():   #if input is a word
    rev=""
    for i in item:  #loop to reverse
        rev=i+rev
    print("Reversed:",rev)
    reverse=rev
    if reverse==item:  #check palindrome
        print("Palindrome")
    else:
        print("Not Palindrome")
elif item.isdigit(): #if input is a number
    rev=0
    n=int(item)
    while (n>0):      #loop to reverse
        digit=n%10
        rev=rev*10+digit
        n=n//10
    print("Reversed:",rev)
    if rev==int(item):    #check palindrome
        print("Palindrome")
    else:
        print("Not Palindrome")
    

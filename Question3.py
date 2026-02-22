#String Manipulator
string1=input("Enter a String:") #User input
print("Original:",string1) #original string
print("Characters (with spaces):",len(string1)) # no of characters with spaces
count=0
for i in string1: #loop to go through string
   if i!=" ":
        count+=1
print("Characters (with spaces):",count) #no of characters with spaces
list1=string1.split() #converting string to list
count=len(list1)
print("Words:",count) #no of words in input
print("UPPERCASE:",string1.upper()) #converting to uppercase
print("lowercase:",string1.lower()) #converting to lowercase
print("lowercase:",string1.title()) #converting to titlecase
print("First word:",list1[0]) #outputting first word
print("Last word:",list1[-1]) #outputting Last word
reverse=""
for i in string1:
    reverse=i+reverse
print("Reversed:",reverse) #Reversed string
#Text Analysis Functions
def count_words(text):
    list1=text.split()
    print("Words:",len(list1))
    
def count_vowels(text):
    count=0
    vowels="aeiouAEIOU"
    for i in text:
        if i in vowels:
            count+=1
    print("Vowels:",count)
    
def count_consonants(text):
    count=0
    vowels="aeiouAEIOU"
    for i in text:
        if i not in vowels and i!=" ":
            count+=1
    print("Consonants:",count)
    
def reverse_text(text):
    reverse=""
    for i in text:
        reverse=i+reverse
    print("Reversed:",reverse)
    
def is_palindrome(text) :
    reverse=""
    for i in text:
        reverse=i+reverse
    if reverse==text:
        print("Input is a palindrome")
    else:
        print("Input is not a palindrome")
        
def  remove_vowels(text):
    newstring=""
    for i in text:
        if i in "aeiouAEIOU":
            continue
        newstring+=i
    print("Without vowels:",newstring)
    
def word_frequency(text):
    d={}
    list1=text.split()
    list2=[]
    for i in list1:
        if i not in list2:
            print("count of",i,"in ",text," is:",list1.count(i))
            list2.append(i)
        
def longest_word(text):
    list1=text.split()
    longest_word = max(list1,key=len)
    print(longest_word,"(",len(longest_word),")")
    
def analyze_text() :
    text1=input("Enter text:")
    text=text1.strip()
    count_words(text)
    count_vowels(text)
    count_consonants(text)
    reverse_text(text)
    is_palindrome(text)
    remove_vowels(text)
    word_frequency(text)
    longest_word(text)

analyze_text()
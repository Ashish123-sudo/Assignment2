import math

def factorial():
    n=int(input("Enter a number:"))
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial of",n,"=",fact)

def is_prime():
    n=int(input("Enter a number:"))
    flag=0
    if n==0:
        print("n is 0")
    for i in range(2,n):
        if(n%i==0):
            flag=1
    if(flag==0):
        print(n,"is prime")
    else:
        print(n,"is not prime")
        
def fibonacci():
    n=int(input("Enter a number:"))
    if n<=0:
        print("number greater than 0 required")
    elif n==1:
        print("1 fibonacci no is 0")
    elif n==2:
        print("2 fibonacci no is 1")
    else:
        a=0
        b=1
        for i in range(2,n):
            summ=a+b
            a=b
            b=summ
            
        print(n,"fibonacci number is:",summ)

def sum_of_digits():
    n=int(input("Enter a number:"))
    summ=0
    while(n>0):
        digit = n % 10  
        summ += digit     
        n //= 10   
    print("Summ of digits",summ)

def reverse_number():
    n=int(input("Enter a number:"))
    rev=0
    num=n
    while num != 0:
        digit = num % 10        
        rev = rev * 10 + digit 
        num=num//10
    print("Reverse of number",n,"is:",rev)

def is_armstrong():
    n=int(input("Enter a number:"))
    num=n
    total=0
    exp=len(str(num))
    while num != 0:
        digit = num % 10        
        total += digit ** exp
        num=num//10
    if total==n:
        print(n,"is a armstrong number")
    else:
        print(n,"is not a armstrong number")
    
def gcd():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    gcd = math.gcd(a, b)
    print(gcd)
    
def lcm():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    lcm = math.lcm(a, b)
    print(lcm)
    
def is_perfect_number():
    n=int(input("Enter a number:"))
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum = sum + i
    if (sum == n):
        print("Number is a Perfect Number.")
    else:
        print("Number is not a Perfect Number.") 

def math_menu():
    print("1. factorial(n) - return n!")
    print("2. is_prime(n) - return True if prime")
    print("3. fibonacci(n) - return nth Fibonacci number")
    print("4. sum_of_digits(n) - return sum of digits")
    print("5. reverse_number(n) - return number reversed")
    print("6. is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³)")
    print("7. gcd(a, b) - greatest common divisor")
    print("8. lcm(a, b) - least common multiple")
    print("9. is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3)")
    print("10. exit")
    print("Enter your choice:")
    ch=int(input())
    if ch==1:
        factorial()
    elif ch==2:
        is_prime()
    elif ch==3:
        fibonacci()
    elif ch==4:
        sum_of_digits()
    elif ch==5:
        reverse_number()
    elif ch==6:
        is_armstrong()
    elif ch==7:
        gcd()
    elif ch==8:
        lcm()
    elif ch==9:
        is_perfect_number()
    elif ch==10:
        print("exit")
        
        
    
math_menu()
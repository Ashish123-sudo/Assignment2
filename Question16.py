#Number Guessing Game
import random
r=random.randint(1,100)   #Getting  random number

while(True):
    ch=0   #no of chances used
    flag=0    #to check if answer is correct
    while(ch<7):
        guess=int(input("Enter your guess:"))
        if guess==r:    #Condition if guess is correct
            print("Congratulation! correct answer")
            flag=1
            break
        elif guess>r:   #Condition if guess is to high
            print("Your guess needs to be lower")
            print("Remaining Chances:",7-ch-1)
        elif guess<r:   #Condition if guess is to low
            print("Your guess needs to be higher")
            print("Remaining Chances:",7-ch-1)
        ch+=1
    if flag==0:
        print("Out of Guesses, Correct ans:",r)
    print("GAME OVER")
    print("Press any number to play again\n Press 0 to exit")
    restart=int(input(":"))   #Condition to play again
    if restart==0:
        print("Exit")
        break
    
    
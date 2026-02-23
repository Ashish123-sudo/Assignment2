# Grade Calculator

#user input for marks
sub1=int(input("Enter marks for subject 1:"))
sub2=int(input("Enter marks for subject 2:"))
sub3=int(input("Enter marks for subject 3:"))
sub4=int(input("Enter marks for subject 4:"))
sub5=int(input("Enter marks for subject 5:"))
total_marks=sub1+sub2+sub3+sub4+sub5  #total out of 500
print("Total marks (out of 500):",total_marks)
percentage=(total_marks/100)*5  #percentage computation
print("Percentage:",percentage)
print("Grade:")  #Assessing Grade
if (percentage<=100 and percentage>=90):
    print("A+ (Outstanding)")
elif (percentage<90 and percentage>=80):
    print("A (Excellent)")
elif (percentage<80 and percentage>=70):
    print("B (Good)")
elif (percentage<70 and percentage>=60):
    print("C (Average)")
elif (percentage<60 and percentage>=50):
    print("D (Pass)")
elif (percentage<50):
    print("F (Fail)")

#Assessing final result
if (sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40 ):
    print("Result:Pass")
else:
    print("Result:Fail")


'''write a program to calculate a garde of a student from his marks from 
the following scheme 
'''
marks=int(input("ENTER YOUR MARKS:"))
if (marks<0 or marks>100):
    print("PLEASE ENTER YOUR CORRECT MARKS!")
elif marks>=90:
    print("Grade Ex")
elif marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
else:
    print("Fail")    
